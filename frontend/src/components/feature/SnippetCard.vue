<script setup lang="ts">
import type { Snippet } from '../../types'
import CodeBlock from '../common/CodeBlock.vue'

defineProps<{
  snippet: Snippet
}>()

const emit = defineEmits<{
  click: [snippet: Snippet]
}>()

const getLanguageColor = (language: string) => {
  const colors: Record<string, string> = {
    Python: '#3776ab',
    Rust: '#dea584',
    TypeScript: '#3178c6',
    JavaScript: '#f7df1e',
    Java: '#007396',
    Go: '#00add8',
    'C++': '#00599c',
    Ruby: '#cc342d'
  }
  return colors[language] || '#007AFF'
}

const formatDate = (dateString: string) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('zh-CN', { year: 'numeric', month: 'short', day: 'numeric' })
}
</script>

<template>
  <article class="snippet-card" @click="emit('click', snippet)">
    <div class="snippet-card-inner">
      <div class="snippet-header">
        <div 
          class="language-badge" 
          :style="{ backgroundColor: getLanguageColor(snippet.language) + '15', color: getLanguageColor(snippet.language) }"
        >
          <span class="language-dot" :style="{ backgroundColor: getLanguageColor(snippet.language) }"></span>
          {{ snippet.language }}
        </div>
        <time class="snippet-date">{{ formatDate(snippet.createdAt) }}</time>
      </div>
      
      <h3 class="snippet-title">{{ snippet.title }}</h3>
      <p class="snippet-description">{{ snippet.description }}</p>
      
      <div class="code-preview">
        <CodeBlock :code="snippet.code" :language="snippet.language" />
      </div>
    </div>
  </article>
</template>

<style scoped>
.snippet-card {
  background: var(--secondary-system-background);
  border-radius: var(--corner-xl);
  overflow: hidden;
  transition: all var(--duration-base) var(--spring);
  cursor: pointer;
}

.snippet-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-m);
}

.snippet-card:active {
  transform: translateY(0);
}

.snippet-card-inner {
  padding: var(--spacing-xl);
  display: flex;
  flex-direction: column;
  gap: var(--spacing-m);
  height: 100%;
}

.snippet-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--spacing-s);
}

.language-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  border-radius: var(--corner-full);
  font-size: var(--typography-caption-1);
  font-weight: 600;
  letter-spacing: 0.02em;
}

.language-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}

.snippet-date {
  font-size: var(--typography-caption-1);
  color: var(--tertiary-label);
  font-weight: 500;
  letter-spacing: 0.01em;
}

.snippet-title {
  font-size: var(--typography-headline);
  font-weight: 600;
  color: var(--label);
  margin: 0;
  line-height: 1.3;
  letter-spacing: -0.02em;
}

.snippet-card:hover .snippet-title {
  color: var(--tint);
}

.snippet-description {
  font-size: var(--typography-subheadline);
  color: var(--secondary-label);
  line-height: 1.5;
  margin: 0;
}

.code-preview {
  margin-top: var(--spacing-s);
  border-radius: var(--corner-m);
  overflow: hidden;
}

@media (max-width: 768px) {
  .snippet-card-inner {
    padding: var(--spacing-l);
  }
  
  .snippet-title {
    font-size: var(--typography-callout);
  }
}
</style>
