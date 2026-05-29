<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import type { Post } from '../types'
import { blogApi } from '../services/api'
import { marked } from 'marked'
import DOMPurify from 'dompurify'

const route = useRoute()
const router = useRouter()
const post = ref<Post | null>(null)
const loading = ref(true)

const renderedContent = computed(() => {
  if (!post.value) return ''
  const markdownHtml = (marked(post.value.content) as string)
  return DOMPurify.sanitize(markdownHtml)
})

const postId = Number(route.params.id)

onMounted(async () => {
  try {
    const res = await blogApi.getPost(postId)
    post.value = res.data
  } catch (error) {
    console.error('Failed to fetch post:', error)
  } finally {
    loading.value = false
  }
})

const goBack = () => {
  router.push('/blog')
}
</script>

<template>
  <div class="post-detail">
    <div class="container">
      <button class="back-btn haptic" @click="goBack">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polyline points="15 18 9 12 15 6"></polyline>
        </svg>
        返回博客列表
      </button>
      
      <div v-if="loading" class="loading-container">
        <div class="spinner"></div>
        <p>加载中...</p>
      </div>
      
      <div v-else-if="post" class="post-content">
        <div class="post-header">
          <h1>{{ post.title }}</h1>
          <div class="post-meta">
            <div class="post-info">
              <div class="author-avatar">{{ post.author.charAt(0) }}</div>
              <div class="post-info-text">
                <span class="author">{{ post.author }}</span>
                <span class="date">{{ new Date(post.createdAt).toLocaleDateString('zh-CN', { year: 'numeric', month: 'long', day: 'numeric' }) }}</span>
              </div>
            </div>
            <div class="tags">
              <span v-for="tag in post.tags" :key="tag" class="tag">{{ tag }}</span>
            </div>
          </div>
        </div>
        <div class="content" v-html="renderedContent"></div>
      </div>
      
      <div v-else class="not-found">
        <h2>文章未找到</h2>
        <button @click="goBack" class="btn btn-primary">返回博客列表</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.post-detail {
  padding: var(--spacing-2xl) 0;
  min-height: calc(100vh - 60px);
  padding-top: calc(var(--spacing-2xl) + env(safe-area-inset-top));
}

.container {
  max-width: 750px;
  margin: 0 auto;
  padding: 0 var(--spacing-l);
}

.back-btn {
  display: inline-flex;
  align-items: center;
  gap: var(--spacing-xs);
  background: var(--secondary-system-background);
  border: 0.5px solid var(--separator);
  color: var(--label);
  font-size: var(--typography-callout);
  cursor: pointer;
  margin-bottom: var(--spacing-xl);
  padding: var(--spacing-sm) var(--spacing-m);
  border-radius: var(--corner-l);
  font-weight: 500;
  transition: all var(--duration-base) var(--spring);
  box-shadow: var(--shadow-s);
}

.back-btn:hover {
  background: var(--tertiary-system-background);
  box-shadow: var(--shadow-m);
}

.back-btn:active {
  transform: scale(0.98);
}

.post-header {
  margin-bottom: var(--spacing-2xl);
}

.post-header h1 {
  font-size: var(--typography-large-title);
  color: var(--label);
  margin: 0 0 var(--spacing-xl);
  font-weight: 700;
  line-height: 1.2;
  letter-spacing: -0.03em;
}

.post-meta {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-m);
  padding-bottom: var(--spacing-xl);
  border-bottom: 0.5px solid var(--separator);
}

.post-info {
  display: flex;
  align-items: center;
  gap: var(--spacing-m);
}

.author-avatar {
  width: 40px;
  height: 40px;
  border-radius: var(--corner-full);
  background: var(--tint);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: var(--typography-callout);
}

.post-info-text {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-2xs);
}

.author {
  font-weight: 600;
  color: var(--label);
  font-size: var(--typography-callout);
}

.date {
  color: var(--secondary-label);
  font-size: var(--typography-footnote);
}

.tags {
  display: flex;
  gap: var(--spacing-xs);
  flex-wrap: wrap;
}

.tag {
  background: var(--tertiary-system-background);
  color: var(--secondary-label);
  padding: var(--spacing-2xs) var(--spacing-sm);
  border-radius: var(--corner-full);
  font-size: var(--typography-footnote);
  font-weight: 500;
}

.post-content {
  padding: var(--spacing-2xl) 0;
}

.content {
  line-height: 1.7;
  color: var(--label);
  font-size: var(--typography-headline);
}

.content h1 {
  font-size: var(--typography-title-2);
  margin: var(--spacing-2xl) 0 var(--spacing-l);
  color: var(--label);
  font-weight: 700;
  letter-spacing: -0.02em;
}

.content h2 {
  font-size: var(--typography-title-3);
  margin: var(--spacing-xl) 0 var(--spacing-m);
  color: var(--label);
  font-weight: 600;
  letter-spacing: -0.01em;
}

.content h3 {
  font-size: var(--typography-headline);
  margin: var(--spacing-l) 0 var(--spacing-s);
  color: var(--label);
  font-weight: 600;
}

.content p {
  margin: var(--spacing-md) 0;
  color: var(--label);
}

.content ul, .content ol {
  margin: var(--spacing-md) 0;
  padding-left: var(--spacing-xl);
  color: var(--label);
}

.content li {
  margin: var(--spacing-sm) 0;
}

.content code {
  background: var(--tertiary-system-background);
  color: var(--tint);
  padding: 0.2rem 0.4rem;
  border-radius: var(--corner-s);
  font-family: var(--font-mono);
  font-size: 0.9em;
}

.content pre {
  background: var(--secondary-system-background);
  color: var(--label);
  padding: var(--spacing-lg);
  border-radius: var(--corner-l);
  overflow-x: auto;
  margin: var(--spacing-md) 0;
  border: 0.5px solid var(--separator);
}

.content pre code {
  background: none;
  padding: 0;
  color: inherit;
  font-family: var(--font-mono);
  font-size: var(--typography-footnote);
}

.content blockquote {
  border-left: 3px solid var(--tint);
  padding-left: var(--spacing-md);
  margin: var(--spacing-md) 0;
  color: var(--secondary-label);
  font-style: italic;
  padding: var(--spacing-md) var(--spacing-lg);
  border-radius: 0 var(--corner-l) var(--corner-l) 0;
  background: var(--secondary-system-background);
}

.content a {
  color: var(--tint);
  text-decoration: none;
  font-weight: 500;
  transition: color var(--duration-base);
}

.content a:hover {
  text-decoration: underline;
}

.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: var(--spacing-3xl);
  gap: var(--spacing-md);
  color: var(--tertiary-label);
}

.not-found {
  text-align: center;
  padding: var(--spacing-3xl);
}

.not-found h2 {
  color: var(--secondary-label);
  margin-bottom: var(--spacing-lg);
  font-size: var(--typography-title-2);
}

@media (max-width: 768px) {
  .post-detail {
    padding: var(--spacing-xl) 0;
  }
  
  .post-header h1 {
    font-size: var(--typography-title-1);
  }
  
  .content {
    font-size: var(--typography-callout);
  }
}
</style>
