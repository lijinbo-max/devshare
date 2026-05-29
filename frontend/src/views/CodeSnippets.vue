<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import SnippetCard from '../components/feature/SnippetCard.vue'
import Skeleton from '../components/common/Skeleton.vue'
import { snippetApi } from '../services/api'
import type { Snippet } from '../types'

const snippets = ref<Snippet[]>([])
const loading = ref(true)
const selectedLanguage = ref('all')

const languages = ['all', 'Python', 'TypeScript', 'Rust', 'Java', 'JavaScript']

onMounted(async () => {
  try {
    const res = await snippetApi.getSnippets()
    snippets.value = res.data
  } catch (error) {
    console.error('Failed to fetch snippets:', error)
  } finally {
    loading.value = false
  }
})

const filteredSnippets = ref<Snippet[]>([])
watch([snippets, selectedLanguage], () => {
  if (selectedLanguage.value === 'all') {
    filteredSnippets.value = snippets.value
  } else {
    filteredSnippets.value = snippets.value.filter(
      snippet => snippet.language === selectedLanguage.value
    )
  }
}, { immediate: true })

const handleSnippetClick = (snippet: Snippet) => {
  console.log('Viewing snippet:', snippet.title)
}
</script>

<template>
  <div class="snippets">
    <div class="container">
      <div class="page-header">
        <h1 class="page-title">代码片段</h1>
        <p class="page-subtitle">收集和分享实用的代码片段</p>
      </div>

      <div class="filter-bar">
        <button 
          v-for="lang in languages" 
          :key="lang"
          :class="['filter-btn', { active: selectedLanguage === lang }, 'haptic']"
          @click="selectedLanguage = lang"
        >
          {{ lang === 'all' ? '全部' : lang }}
        </button>
      </div>

      <div class="snippets-grid">
        <template v-if="loading">
          <Skeleton v-for="i in 6" :key="i" type="snippet" />
        </template>
        <template v-else-if="filteredSnippets.length > 0">
          <SnippetCard 
            v-for="(snippet, index) in filteredSnippets" 
            :key="snippet.id" 
            :snippet="snippet"
            @click="handleSnippetClick"
            class="card-animate"
            :style="{ animationDelay: `${index * 50}ms` }"
          />
        </template>
        <div v-else class="empty-state">
          <svg class="empty-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polyline points="4 17 10 11 4 5"></polyline>
            <line x1="12" y1="19" x2="20" y2="19"></line>
          </svg>
          <h3>暂无该语言的代码片段</h3>
          <p>尝试选择其他语言</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.snippets {
  padding: var(--spacing-2xl) 0 var(--spacing-3xl);
  min-height: calc(100vh - 60px);
  padding-top: calc(var(--spacing-2xl) + env(safe-area-inset-top));
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--spacing-l);
}

.page-header {
  text-align: center;
  margin-bottom: var(--spacing-xl);
}

.page-title {
  font-size: var(--typography-title-1);
  color: var(--label);
  margin: 0 0 var(--spacing-xs);
  font-weight: 700;
  letter-spacing: -0.02em;
}

.page-subtitle {
  font-size: var(--typography-callout);
  color: var(--secondary-label);
  margin: 0;
}

.filter-bar {
  display: flex;
  gap: var(--spacing-xs);
  flex-wrap: wrap;
  justify-content: center;
  margin-bottom: var(--spacing-xl);
}

.filter-btn {
  padding: var(--spacing-xs) var(--spacing-m);
  border: 1px solid var(--separator);
  background: var(--secondary-system-background);
  border-radius: var(--corner-full);
  cursor: pointer;
  color: var(--secondary-label);
  font-weight: 500;
  font-size: var(--typography-footnote);
  transition: all var(--duration-base) var(--spring);
}

.filter-btn:hover {
  background: var(--tertiary-system-background);
  color: var(--label);
}

.filter-btn.active {
  background: var(--tint);
  color: white;
  border-color: var(--tint);
}

.snippets-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--spacing-l);
}

.card-animate {
  animation: fadeInUp 0.4s var(--spring) forwards;
  opacity: 0;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(12px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.empty-state {
  grid-column: 1 / -1;
  text-align: center;
  padding: var(--spacing-3xl) var(--spacing-xl);
  color: var(--secondary-label);
}

.empty-icon {
  width: 64px;
  height: 64px;
  margin-bottom: var(--spacing-m);
  color: var(--tertiary-label);
}

.empty-state h3 {
  font-size: var(--typography-title-3);
  font-weight: 600;
  color: var(--label);
  margin: 0 0 var(--spacing-xs);
  letter-spacing: -0.01em;
}

.empty-state p {
  font-size: var(--typography-subheadline);
  margin: 0;
}

@media (max-width: 1024px) {
  .snippets-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .snippets {
    padding: var(--spacing-xl) 0 var(--spacing-2xl);
  }
  
  .page-title {
    font-size: var(--typography-title-2);
  }
  
  .snippets-grid {
    grid-template-columns: 1fr;
  }
}
</style>
