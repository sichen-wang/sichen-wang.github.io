---
# Leave the homepage title empty to use the site title
title: ''
summary: ''
date: 2022-10-24
type: landing

design:
  # 区块间距设为 0：本页只有一个区块，它已经自己占满一屏高并垂直居中，
  # 再加 6rem 的上下间距会把内容整体推低、并让首屏多出无谓的滚动
  spacing: '0'

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: home
      text: ''
      # 不再放 Download CV 大按钮：头像下方的 CV 图标已指向同一份英文 CV
      headings:
        about: ''
        education: ''
        interests: ''
    design:
      
      # Use the new Gradient Mesh which automatically adapts to the selected theme colors
      background:
        gradient_mesh:
          enable: true

      # Name heading sizing to accommodate long or short names
      name:
        size: md # Options: xs, sm, md, lg (default), xl

      # Avatar customization
      avatar:
        size: medium # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: circle # Options: circle (default), square, rounded
---
