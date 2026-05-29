# 响应式设计方案使用指南

## 📱 断点设置

我们的响应式设计支持以下断点：

| 设备类型 | 宽度范围 | 断点变量 | 说明 |
|---------|---------|---------|------|
| 超小屏幕 | 320px - 479px | `--breakpoint-xs` | 小型手机 |
| 小屏幕 | 480px - 767px | `--breakpoint-sm` | 大型手机 |
| 中等屏幕 | 768px - 1023px | `--breakpoint-md` | 平板设备 |
| 大屏幕 | 1024px - 1279px | `--breakpoint-lg` | 小型笔记本 |
| 超大屏幕 | 1280px - 1535px | `--breakpoint-xl` | 标准桌面 |
| 最大屏幕 | ≥1536px | `--breakpoint-2xl` | 大型桌面 |

## 🎨 设计单位

### 使用相对单位

所有样式已转换为相对单位：

- **rem**: 主要用于间距、内边距、字体大小
- **%**: 用于流体布局和容器宽度
- **vw/vh**: 用于视口相关的尺寸
- **clamp()**: 用于流体字体大小

### 示例

```css
/* 之前（固定像素） */
padding: 16px;
font-size: 17px;
margin: 24px 0;

/* 现在（相对单位） */
padding: var(--spacing-m);
font-size: var(--typography-body);
margin: var(--spacing-xl) 0;
```

## 📐 流体布局

### 网格系统

```vue
<div class="grid grid-2">
  <!-- 自动适配的两列布局 -->
</div>

<div class="grid grid-3">
  <!-- 自动适配的三列布局 -->
</div>

<div class="grid grid-4">
  <!-- 自动适配的四列布局 -->
</div>
```

### 弹性盒子

```vue
<div class="flex flex-wrap gap-m">
  <!-- 自动换行的弹性容器 -->
</div>

<div class="flex flex-between">
  <!-- 两端对齐的弹性容器 -->
</div>

<div class="flex flex-center">
  <!-- 居中对齐的弹性容器 -->
</div>
```

## 🖋️ 排版优化

### 字体大小层级

```vue
<h1 class="text-large-title">大标题</h1>
<h2 class="text-title-1">一级标题</h2>
<h3 class="text-title-2">二级标题</h3>
<h4 class="text-title-3">三级标题</h4>
<p class="text-headline">正文标题</p>
<p class="text-body">正文内容</p>
<p class="text-footnote">脚注文本</p>
```

### 文本对齐

```vue
<p class="text-center">居中对齐</p>
<p class="text-left">左对齐</p>
<p class="text-right">右对齐</p>
```

### 文本颜色

```vue
<p class="text-primary">主要文本</p>
<p class="text-secondary">次要文本</p>
<p class="text-muted">淡化文本</p>
<p class="text-accent">强调文本</p>
```

## 🔘 交互元素

### 按钮尺寸

所有交互元素都遵循触摸友好的尺寸规范：

```vue
<button class="btn btn-sm">小按钮</button>
<button class="btn">标准按钮</button>
<button class="btn btn-lg">大按钮</button>
<button class="btn btn-icon">图标按钮</button>
```

**最小触摸目标**: `--min-touch-target` (默认 2.5rem = 40px)

### 表单输入

```vue
<input type="text" placeholder="输入框" />
<textarea placeholder="文本域"></textarea>
<select>
  <option>下拉选择</option>
</select>
```

## 📏 间距系统

### 外边距

```vue
<div class="mt-xs">上方小间距</div>
<div class="mt-m">上方中间距</div>
<div class="mt-2xl">上方大间距</div>

<div class="mb-xs">下方小间距</div>
<div class="mb-m">下方中间距</div>
<div class="mb-2xl">下方大间距</div>
```

### 内边距

```vue
<div class="p-xs">小内边距</div>
<div class="p-m">中间内边距</div>
<div class="p-2xl">大内边距</div>
```

### Gap 间距

```vue
<div class="flex gap-xs">
  <!-- 元素间小间距 -->
</div>

<div class="grid gap-m">
  <!-- 网格元素间中间距 -->
</div>
```

## 📦 容器系统

### 标准容器

```vue
<div class="container">
  <!-- 最大宽度 1200px，居中显示 -->
</div>
```

### 全宽容器

```vue
<div class="container-fluid">
  <!-- 100% 宽度，自适应屏幕 -->
</div>
```

## 🎯 响应式显示控制

### 隐藏元素

```vue
<p class="hide-xs">在超小屏幕上隐藏</p>
<p class="hide-sm">在小屏幕上隐藏</p>
<p class="hide-md">在平板上隐藏</p>
<p class="hide-lg">在笔记本上隐藏</p>
<p class="hide-xl">在大屏幕上隐藏</p>
```

### 显示元素（配合隐藏使用）

```vue
<div class="hide-md show-md">
  <!-- 在平板及以上显示 -->
</div>
```

## 🎨 卡片组件

### 基础卡片

```vue
<div class="card">
  <h3>卡片标题</h3>
  <p>卡片内容</p>
</div>
```

### 卡片网格

```vue
<div class="grid grid-3 gap-l">
  <div class="card">
    <h3>卡片1</h3>
    <p>内容</p>
  </div>
  <div class="card">
    <h3>卡片2</h3>
    <p>内容</p>
  </div>
  <div class="card">
    <h3>卡片3</h3>
    <p>内容</p>
  </div>
</div>
```

## 🏷️ 徽章组件

```vue
<span class="badge badge-tint">蓝色徽章</span>
<span class="badge badge-green">绿色徽章</span>
<span class="badge badge-red">红色徽章</span>
```

## 📱 实际应用示例

### 文章卡片

```vue
<template>
  <article class="card p-l">
    <div class="flex flex-between mb-m">
      <span class="badge badge-tint">{{ category }}</span>
      <span class="text-footnote text-muted">{{ date }}</span>
    </div>
    <h3 class="text-title-2 mb-s">{{ title }}</h3>
    <p class="text-body text-secondary mb-l">{{ excerpt }}</p>
    <div class="flex gap-m">
      <button class="btn btn-sm">阅读更多</button>
      <button class="btn btn-sm btn-ghost">收藏</button>
    </div>
  </article>
</template>
```

### 导航菜单

```vue
<template>
  <nav class="container">
    <div class="flex flex-between p-m">
      <div class="flex gap-l">
        <a href="#">首页</a>
        <a href="#" class="hide-xs">博客</a>
        <a href="#" class="hide-xs">关于</a>
      </div>
      <button class="btn btn-sm">登录</button>
    </div>
  </nav>
</template>
```

### 响应式网格

```vue
<template>
  <section class="section">
    <div class="container">
      <h2 class="text-title-1 text-center mb-2xl">精选文章</h2>
      <div class="grid grid-3 gap-xl">
        <ArticleCard v-for="article in articles" :key="article.id" :article="article" />
      </div>
    </div>
  </section>
</template>
```

## 🔧 自定义断点

如果需要添加自定义断点，可以在组件样式中覆盖：

```vue
<style scoped>
@media (min-width: 400px) and (max-width: 600px) {
  .custom-component {
    font-size: 0.9rem;
    padding: 0.5rem;
  }
}
</style>
```

## ✅ 最佳实践

1. **使用设计系统变量**: 优先使用 CSS 变量而不是硬编码值
2. **移动优先**: 从最小屏幕开始设计，逐步增强
3. **触摸友好**: 确保所有交互元素至少 44x44px
4. **测试真实设备**: 在各种设备上测试布局
5. **性能优化**: 避免使用复杂的媒体查询嵌套
6. **内容可读性**: 确保文本行长度在 50-75 字符范围内

## 🧪 测试建议

在不同分辨率下测试：

- **320px**: iPhone SE
- **375px**: iPhone X/12/13
- **414px**: iPhone Plus/Max
- **768px**: iPad
- **1024px**: iPad Pro
- **1280px**: 小型笔记本
- **1920px**: 标准桌面

## 📚 相关文件

- `responsive.css` - 响应式样式定义
- `main.css` - 主样式文件
- 组件样式文件 - 在各自的 `.vue` 文件的 `<style scoped>` 中定义
