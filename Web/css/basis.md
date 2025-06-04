# CSS 基础介绍

## 什么是 CSS？

CSS（层叠样式表，Cascading Style Sheets）是一种用于描述 HTML 或 XML 文档表现形式的样式表语言。CSS 描述了元素应该如何在屏幕、纸张或其他媒体上呈现。

## CSS 的重要性

- 分离内容与表现
- 提高网页加载速度
- 提供更好的可维护性
- 实现响应式设计
- 增强用户体验

## CSS 语法

CSS 规则由选择器和声明块组成：

```css
选择器 {
    属性: 值;
    属性: 值;
}
```

## 引入 CSS 的方式

1. **内联样式**：直接在 HTML 元素中使用 style 属性

    ```html
    <p style="color: red; font-size: 20px;">这是红色文本</p>
    ```

2. **内部样式表**：在 HTML 文档头部使用 `<style>` 标签

    ```html
    <head>
        <style>
            p {
                color: blue;
                font-size: 16px;
            }
        </style>
    </head>
    ```

3. **外部样式表**：使用单独的 CSS 文件，通过 `<link>` 标签引入

    ```html
    <head>
        <link rel="stylesheet" href="styles.css">
    </head>
    ```

## CSS 选择器

- **元素选择器**：`p { }`
- **ID 选择器**：`#id { }`
- **类选择器**：`.class { }`
- **属性选择器**：`[attribute=value] { }`
- **伪类选择器**：`:hover { }`

## CSS 盒模型

所有 HTML 元素都可以看作一个盒子，包含：

- Content（内容）
- Padding（内边距）
- Border（边框）
- Margin（外边距）

## 常用 CSS 属性

- `color`: 文本颜色
- `background-color`: 背景颜色
- `font-size`: 字体大小
- `font-family`: 字体
- `margin`, `padding`: 外边距和内边距
- `display`: 显示方式
- `position`: 定位方式

## CSS 单位

- 绝对单位：px, pt, cm, mm
- 相对单位：em, rem, %, vh, vw

## 媒体查询

响应式设计的核心，允许根据不同设备特性应用不同样式：

```css
@media (max-width: 600px) {
    .container {
        width: 100%;
    }
}
```
