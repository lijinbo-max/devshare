<script setup lang="ts">
import { ref, onMounted, watch, nextTick } from 'vue'
import Prism from 'prismjs'
import 'prismjs/themes/prism-tomorrow.css'
import 'prismjs/components/prism-python'
import 'prismjs/components/prism-rust'
import 'prismjs/components/prism-typescript'
import 'prismjs/components/prism-javascript'
import 'prismjs/components/prism-java'
import 'prismjs/components/prism-go'
import 'prismjs/components/prism-cpp'
import 'prismjs/components/prism-ruby'
import 'prismjs/components/prism-markup'
import 'prismjs/components/prism-css'
import 'prismjs/components/prism-php'
import 'prismjs/components/prism-swift'
import 'prismjs/components/prism-kotlin'
import 'prismjs/components/prism-scala'

const props = defineProps<{
  code: string
  language: string
}>()

const copied = ref(false)
const codeRef = ref<HTMLElement | null>(null)

const languageAliases: Record<string, string> = {
  'C++': 'cpp',
  'TypeScript': 'typescript',
  'JavaScript': 'javascript',
  'HTML': 'markup',
  'CSS': 'css'
}

const getLanguageColor = (language: string) => {
  const colors: Record<string, string> = {
    Python: '#3776ab',
    Rust: '#dea584',
    TypeScript: '#3178c6',
    JavaScript: '#f7df1e',
    Java: '#007396',
    Go: '#00add8',
    'C++': '#00599c',
    Ruby: '#cc342d',
    HTML: '#e34f26',
    CSS: '#1572b6',
    PHP: '#777bb4',
    Swift: '#fa7343',
    Kotlin: '#7f52ff',
    Scala: '#dc322f'
  }
  return colors[language] || '#06b6d4'
}

const getLanguageAlias = (language: string) => {
  return languageAliases[language] || language.toLowerCase()
}

const highlightCode = () => {
  nextTick(() => {
    if (codeRef.value) {
      Prism.highlightElement(codeRef.value)
    }
  })
}

onMounted(() => {
  highlightCode()
})

watch(() => props.code, () => {
  highlightCode()
})

const copyCode = async () => {
  try {
    await navigator.clipboard.writeText(props.code)
    copied.value = true
    setTimeout(() => {
      copied.value = false
    }, 2000)
  } catch (err) {
    console.error('Failed to copy:', err)
  }
}
</script>

<template>
  <div class="code-block">
    <div class="code-header">
      <div class="code-dots">
        <span class="dot red"></span>
        <span class="dot yellow"></span>
        <span class="dot green"></span>
      </div>
      <div class="code-info">
        <span class="language-tag" :style="{ backgroundColor: getLanguageColor(language) + '20', color: getLanguageColor(language) }">
          {{ language }}
        </span>
        <button 
          class="copy-btn" 
          @click="copyCode"
          :class="{ copied }"
          :aria-label="copied ? '已复制' : '复制代码'"
        >
          <svg v-if="!copied" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
            <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
          </svg>
          <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polyline points="20 6 9 17 4 12"></polyline>
          </svg>
          <span>{{ copied ? '已复制' : '复制' }}</span>
        </button>
      </div>
    </div>
    <div class="code-body">
      <pre><code ref="codeRef" :class="`language-${getLanguageAlias(language)}`">{{ code }}</code></pre>
    </div>
    <div class="copy-toast" v-if="copied">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <polyline points="20 6 9 17 4 12"></polyline>
      </svg>
      <span>代码已复制到剪贴板</span>
    </div>
  </div>
</template>

<style scoped>
.code-block {
  position: relative;
  background: #1e1e1e;
  border-radius: var(--border-radius-lg);
  overflow: hidden;
  font-family: var(--font-mono);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

[data-theme="dark"] .code-block {
  background: #0d1117;
}

.code-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #2d2d2d;
  padding: 0.5rem 1rem;
  border-bottom: 1px solid #3d3d3d;
}

[data-theme="dark"] .code-header {
  background: #161b22;
  border-bottom: 1px solid #30363d;
}

.code-dots {
  display: flex;
  gap: 6px;
}

.dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
}

.dot.red {
  background: #ff5f56;
}

.dot.yellow {
  background: #ffbd2e;
}

.dot.green {
  background: #27c93f;
}

.code-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.language-tag {
  padding: 0.25rem 0.75rem;
  border-radius: 4px;
  font-size: 0.7rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.copy-btn {
  display: flex;
  align-items: center;
  gap: 4px;
  background: rgba(255, 255, 255, 0.1);
  border: none;
  color: #94a3b8;
  padding: 0.375rem 0.75rem;
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 500;
  cursor: pointer;
  transition: all var(--transition-fast);
}

.copy-btn:hover {
  background: rgba(255, 255, 255, 0.15);
  color: #fff;
}

.copy-btn.copied {
  background: rgba(16, 185, 129, 0.2);
  color: #10b981;
}

.copy-btn svg {
  width: 14px;
  height: 14px;
}

.code-body {
  max-height: 500px;
  overflow-y: auto;
}

.code-body pre {
  margin: 0;
  padding: 1rem;
  overflow-x: auto;
}

.code-body code {
  font-size: 0.85rem;
  line-height: 1.6;
}

.code-body :deep(.token.comment),
.code-body :deep(.token.prolog),
.code-body :deep(.token.doctype),
.code-body :deep(.token.cdata) {
  color: #6a9955;
  font-style: italic;
}

.code-body :deep(.token.punctuation) {
  color: #d4d4d4;
}

.code-body :deep(.token.namespace) {
  opacity: 0.7;
}

.code-body :deep(.token.property),
.code-body :deep(.token.tag),
.code-body :deep(.token.constant),
.code-body :deep(.token.symbol),
.code-body :deep(.token.deleted) {
  color: #c586c0;
}

.code-body :deep(.token.boolean),
.code-body :deep(.token.number) {
  color: #b5cea8;
}

.code-body :deep(.token.selector),
.code-body :deep(.token.attr-name),
.code-body :deep(.token.string),
.code-body :deep(.token.char),
.code-body :deep(.token.builtin),
.code-body :deep(.token.inserted) {
  color: #ce9178;
}

.code-body :deep(.token.operator),
.code-body :deep(.token.entity),
.code-body :deep(.token.url),
.code-body :deep(.language-css .token.string),
.code-body :deep(.style .token.string) {
  color: #d4d4d4;
}

.code-body :deep(.token.atrule),
.code-body :deep(.token.attr-value),
.code-body :deep(.token.keyword) {
  color: #569cd6;
}

.code-body :deep(.token.function) {
  color: #dcdcaa;
}

.code-body :deep(.token.class-name) {
  color: #4ec9b0;
}

.code-body :deep(.token.variable) {
  color: #9cdcfe;
}

.copy-toast {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(16, 185, 129, 0.9);
  color: white;
  padding: 0.75rem 1.25rem;
  border-radius: var(--border-radius-md);
  font-size: 0.9rem;
  font-weight: 500;
  animation: toast-in 0.3s ease;
  z-index: 10;
}

.copy-toast svg {
  width: 18px;
  height: 18px;
}

@keyframes toast-in {
  from {
    opacity: 0;
    transform: translate(-50%, -50%) scale(0.9);
  }
  to {
    opacity: 1;
    transform: translate(-50%, -50%) scale(1);
  }
}

@media (max-width: 768px) {
  .code-header {
    padding: 0.5rem;
  }
  
  .copy-btn span {
    display: none;
  }
  
  .code-body pre {
    padding: 0.75rem;
  }
  
  .code-body code {
    font-size: 0.8rem;
  }
}
</style>