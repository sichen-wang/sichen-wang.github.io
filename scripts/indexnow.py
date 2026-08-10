#!/usr/bin/env python3
"""把最近变更的页面通知给 IndexNow（Bing / Yandex / Seznam 等采纳该协议）。

只提交「刚改过」的网址：站点开了 ``enableGitInfo``，sitemap 里的 lastmod 取自
git 提交时间，所以按时间窗口筛选即可，不必解析 diff 再猜 Hugo 的 slug 规则
（中文标题的 slug 化很容易猜错）。IndexNow 协议本身也要求只提交变更的 URL。

Google 不参与该协议，且没有面向普通页面的合法提交接口（Indexing API 限
JobPosting / BroadcastEvent，sitemap ping 已废弃），因此 Google 侧仍需在
Search Console 手动 Request Indexing。

密钥文件按协议要求公开可访问，它不是机密 —— 所有权靠「能在自己域名下放这个
文件」来证明，所以无需配置 secrets。

用法::

    python3 scripts/indexnow.py --host sichen-wang.github.io --key <key>
    python3 scripts/indexnow.py --host ... --key ... --dry-run   # 只打印不提交
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import urllib.error
import urllib.request

ENDPOINT = "https://api.indexnow.org/IndexNow"
UA = "Mozilla/5.0 (compatible; indexnow-notifier/1.0)"

RE_URL_BLOCK = re.compile(r"<url>(.*?)</url>", re.S)
RE_LOC = re.compile(r"<loc>([^<]+)</loc>")
RE_LASTMOD = re.compile(r"<lastmod>([^<]+)</lastmod>")


def fetch(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


def recent_urls(sitemap: str, hours: float) -> list[str]:
    """挑出 lastmod 在 hours 小时内的 <loc>。"""
    cutoff = dt.datetime.now(dt.timezone.utc) - dt.timedelta(hours=hours)
    out: list[str] = []
    for block in RE_URL_BLOCK.findall(sitemap):
        loc = RE_LOC.search(block)
        mod = RE_LASTMOD.search(block)
        if not (loc and mod):
            continue
        try:
            ts = dt.datetime.fromisoformat(mod.group(1))
        except ValueError:
            continue
        if ts.tzinfo is None:
            ts = ts.replace(tzinfo=dt.timezone.utc)
        if ts >= cutoff:
            out.append(loc.group(1))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", required=True, help="站点主机名，如 sichen-wang.github.io")
    ap.add_argument("--key", required=True, help="IndexNow 密钥（对应 static/<key>.txt）")
    ap.add_argument("--hours", type=float, default=24.0, help="变更时间窗口，默认 24 小时")
    ap.add_argument("--limit", type=int, default=1000, help="单次提交上限，协议上限为 10000")
    ap.add_argument("--dry-run", action="store_true", help="只打印将提交的网址")
    args = ap.parse_args()

    sitemap_url = f"https://{args.host}/sitemap.xml"
    try:
        sitemap = fetch(sitemap_url)
    except (urllib.error.URLError, TimeoutError) as e:
        print(f"::warning::取 sitemap 失败（{e}），跳过 IndexNow 提交。")
        return 0

    urls = recent_urls(sitemap, args.hours)[: args.limit]
    if not urls:
        print(f"最近 {args.hours:g} 小时内没有变更的页面，跳过。")
        return 0

    print(f"提交 {len(urls)} 个网址：")
    for u in urls:
        print(f"  {u}")

    if args.dry_run:
        print("(dry-run，未实际提交)")
        return 0

    payload = json.dumps(
        {
            "host": args.host,
            "key": args.key,
            "keyLocation": f"https://{args.host}/{args.key}.txt",
            "urlList": urls,
        }
    ).encode("utf-8")

    req = urllib.request.Request(
        ENDPOINT,
        data=payload,
        headers={"Content-Type": "application/json; charset=utf-8", "User-Agent": UA},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            code = r.status
            body = r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        code = e.code
        body = e.read().decode("utf-8", "replace")
    except (urllib.error.URLError, TimeoutError) as e:
        print(f"::warning::IndexNow 请求失败（{e}），不影响站点部署。")
        return 0

    print(f"IndexNow 返回 HTTP {code}")
    if body.strip():
        print(body.strip()[:500])

    # 200 已接受；202 已接受、待校验密钥
    if code in (200, 202):
        print("已提交。")
    else:
        print(f"::warning::IndexNow 提交失败（HTTP {code}），不影响站点部署。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
