<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import { useRouter } from 'vue-router'
import PostCard from '../components/feature/PostCard.vue'
import Skeleton from '../components/common/Skeleton.vue'
import { blogApi } from '../services/api'
import type { Post } from '../types'

const router = useRouter()
const posts = ref<Post[]>([])
const loading = ref(true)
const searchQuery = ref('')

onMounted(async () => {
  try {
    const res = await blogApi.getPosts()
    posts.value = res.data
  } catch (error) {
    console.error('Failed to fetch posts:', error)
  } finally {
    loading.value = false
  }
})

const filteredPosts = ref<Post[]>([])
watch([posts, searchQuery], () => {
  if (!searchQuery.value) {
    filteredPosts.value = posts.value
  } else {
    const query = searchQuery.value.toLowerCase()
    filteredPosts.value = posts.value.filter(post => 
      post.title.toLowerCase().includes(query) ||
      post.content.toLowerCase().includes(query) ||
      post.tags.some(tag => tag.toLowerCase().includes(query))
    )
  }
}, { immediate: true })

const handlePostClick = (post: Post) => {
  router.push(`/blog/${post.id}`)
}
</script>

<template>
  <div class="blog">
    <div class="container">
      <div class="page-header">
        <h1 class="page-title">技术博客</h1>
        <p class="page-subtitle">分享编程心得与技术见解</p>
      </div>

      <div class="search-bar">
        <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="11" cy="11" r="8"></circle>
          <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
        </svg>
        <input 
          v-model="searchQuery"
          type="text" 
          placeholder="搜索文章..."
        />
      </div>

      <div class="posts-grid">
        <template v-if="loading">
          <Skeleton v-for="i in 6" :key="i" type="post" />
        </template>
        <template v-else-if="filteredPosts.length > 0">
          <PostCard 
            v-for="(post, index) in filteredPosts" 
            :key="post.id" 
            :post="post"
            @click="handlePostClick"
            class="card-animate"
            :style="{ animationDelay: `${index * 50}ms` }"
          />
        </template>
        <div v-else class="empty-state">
          <svg class="empty-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="12" y1="8" x2="12" y2="12"></line>
            <line x1="12" y1="16" x2="12.01" y2="16"></line>
          </svg>
          <h3>没有找到相关文章</h3>
          <p>尝试其他搜索词</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.blog {
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

.search-bar {
  position: relative;
  max-width: 500px;
  margin: 0 auto var(--spacing-xl);
}

.search-icon {
  position: absolute;
  left: var(--spacing-m);
  top: 50%;
  transform: translateY(-50%);
  width: 20px;
  height: 20px;
  color: var(--tertiary-label);
}

.search-bar input {
  width: 100%;
  padding: var(--spacing-m) var(--spacing-m) var(--spacing-m) 44px;
  border: 1px solid var(--separator);
  border-radius: var(--corner-l);
  font-size: var(--typography-body);
  background: var(--secondary-system-background);
  color: var(--label);
  transition: all var(--duration-base) var(--spring);
}

.search-bar input:focus {
  outline: none;
  border-color: var(--tint);
  box-shadow: 0 0 0 4px rgba(0, 122, 255, 0.1);
}

.search-bar input::placeholder {
  color: var(--tertiary-label);
}

.posts-grid {
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
  .posts-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .blog {
    padding: var(--spacing-xl) 0 var(--spacing-2xl);
  }
  
  .page-title {
    font-size: var(--typography-title-2);
  }
  
  .posts-grid {
    grid-template-columns: 1fr;
  }
}
</style>
