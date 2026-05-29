<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import PostCard from '../components/feature/PostCard.vue'
import SnippetCard from '../components/feature/SnippetCard.vue'
import Skeleton from '../components/common/Skeleton.vue'
import { blogApi, snippetApi } from '../services/api'
import type { Post, Snippet } from '../types'

const router = useRouter()
const posts = ref<Post[]>([])
const snippets = ref<Snippet[]>([])
const loading = ref(true)

onMounted(async () => {
  try {
    const [postsRes, snippetsRes] = await Promise.all([
      blogApi.getPosts(),
      snippetApi.getSnippets()
    ])
    posts.value = postsRes.data
    snippets.value = snippetsRes.data
  } catch (error) {
    console.error('Failed to fetch data:', error)
  } finally {
    loading.value = false
  }
})

const handlePostClick = (post: Post) => {
  router.push(`/blog/${post.id}`)
}

const handleSnippetClick = (snippet: Snippet) => {
  console.log('Snippet clicked:', snippet)
}
</script>

<template>
  <div class="home">
    <section class="hero">
      <div class="container">
        <div class="hero-content">
          <span class="hero-pill">跨语言全栈演示平台</span>
          <h1 class="hero-title">
            欢迎来到 <span class="hero-gradient">个人编程分享</span>
          </h1>
          <p class="hero-description">
            一个展示现代全栈开发的个人编程分享平台，使用 Vue 3、Python FastAPI、Java Spring Boot 和 TypeScript 构建
          </p>
          <div class="hero-actions">
            <button class="btn btn-primary btn-lg haptic" @click="router.push('/blog')">
              浏览博客
              <svg class="btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <line x1="5" y1="12" x2="19" y2="12"></line>
                <polyline points="12 5 19 12 12 19"></polyline>
              </svg>
            </button>
            <button class="btn btn-secondary btn-lg haptic" @click="router.push('/snippets')">
              查看代码片段
            </button>
          </div>
        </div>
      </div>
    </section>

    <section class="content">
      <div class="container">
        <div class="section-header">
          <div>
            <h2 class="section-title">最新博客</h2>
            <p class="section-subtitle">探索技术文章与教程</p>
          </div>
          <button class="btn btn-ghost btn-sm haptic" @click="router.push('/blog')">
            查看全部
            <svg class="btn-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="5" y1="12" x2="19" y2="12"></line>
              <polyline points="12 5 19 12 12 19"></polyline>
            </svg>
          </button>
        </div>
        
        <div class="posts-grid">
          <template v-if="loading">
            <Skeleton v-for="i in 3" :key="i" type="post" />
          </template>
          <template v-else>
            <PostCard 
              v-for="(post, index) in posts.slice(0, 3)" 
              :key="post.id" 
              :post="post"
              @click="handlePostClick"
              class="card-animate"
              :style="{ animationDelay: `${index * 100}ms` }"
            />
          </template>
        </div>

        <div class="section-header">
          <div>
            <h2 class="section-title">代码片段</h2>
            <p class="section-subtitle">精选实用代码示例</p>
          </div>
          <button class="btn btn-ghost btn-sm haptic" @click="router.push('/snippets')">
            查看全部
            <svg class="btn-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="5" y1="12" x2="19" y2="12"></line>
              <polyline points="12 5 19 12 12 19"></polyline>
            </svg>
          </button>
        </div>
        
        <div class="snippets-grid">
          <template v-if="loading">
            <Skeleton v-for="i in 3" :key="i" type="snippet" />
          </template>
          <template v-else>
            <SnippetCard 
              v-for="(snippet, index) in snippets.slice(0, 3)" 
              :key="snippet.id" 
              :snippet="snippet"
              @click="handleSnippetClick"
              class="card-animate"
              :style="{ animationDelay: `${(index + 3) * 100}ms` }"
            />
          </template>
        </div>

        <section class="tech-stack">
          <div class="tech-stack-header">
            <h2 class="section-title">技术栈</h2>
            <p class="section-subtitle">使用现代编程语言和框架构建的高性能全栈应用</p>
          </div>
          <div class="tech-grid">
            <div class="tech-card">
              <div class="tech-icon" style="background: #42b883;">
                Vue
              </div>
              <h3>前端框架</h3>
              <p>渐进式 JavaScript 框架</p>
            </div>
            <div class="tech-card">
              <div class="tech-icon" style="background: #3776ab;">
                Py
              </div>
              <h3>Python API</h3>
              <p>FastAPI 高性能 Web 框架</p>
            </div>
            <div class="tech-card">
              <div class="tech-icon" style="background: #007396;">
                Ja
              </div>
              <h3>Java 后端</h3>
              <p>Spring Boot 企业级框架</p>
            </div>
            <div class="tech-card">
              <div class="tech-icon" style="background: #3178c6;">
                TS
              </div>
              <h3>TypeScript</h3>
              <p>类型安全的 JavaScript</p>
            </div>
          </div>
        </section>
      </div>
    </section>
  </div>
</template>

<style scoped>
.home {
  min-height: 100vh;
  padding-top: calc(60px + env(safe-area-inset-top));
}

.hero {
  position: relative;
  padding: var(--spacing-3xl) 0;
  padding-bottom: var(--spacing-3xl);
}

.hero::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(0, 122, 255, 0.05) 0%, rgba(52, 199, 89, 0.05) 100%);
  z-index: -1;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--spacing-l);
}

.hero-content {
  text-align: center;
  max-width: 700px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--spacing-m);
}

.hero-pill {
  display: inline-flex;
  align-items: center;
  gap: var(--spacing-xs);
  background: var(--secondary-system-background);
  color: var(--secondary-label);
  padding: var(--spacing-xs) var(--spacing-m);
  border-radius: var(--corner-full);
  font-size: var(--typography-footnote);
  font-weight: 500;
  letter-spacing: 0.01em;
}

.hero-title {
  font-size: var(--typography-large-title);
  font-weight: 700;
  color: var(--label);
  margin: 0;
  line-height: 1.2;
  letter-spacing: -0.03em;
}

.hero-gradient {
  background: linear-gradient(135deg, var(--tint) 0%, var(--system-green) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-description {
  font-size: var(--typography-callout);
  color: var(--secondary-label);
  line-height: 1.6;
  margin: 0;
}

.hero-actions {
  display: flex;
  gap: var(--spacing-s);
  margin-top: var(--spacing-s);
}

.btn-icon {
  width: 20px;
  height: 20px;
  margin-left: var(--spacing-xs);
}

.btn-icon-sm {
  width: 16px;
  height: 16px;
  margin-left: var(--spacing-xs);
}

.content {
  padding: var(--spacing-3xl) 0;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: var(--spacing-l);
  gap: var(--spacing-m);
}

.section-title {
  font-size: var(--typography-title-1);
  font-weight: 700;
  color: var(--label);
  margin: 0;
  letter-spacing: -0.02em;
}

.section-subtitle {
  font-size: var(--typography-subheadline);
  color: var(--secondary-label);
  margin: var(--spacing-2xs) 0 0 0;
}

.posts-grid,
.snippets-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--spacing-l);
  margin-bottom: var(--spacing-3xl);
}

.card-animate {
  animation: fadeInUp 0.5s var(--spring) forwards;
  opacity: 0;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(16px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.tech-stack {
  background: var(--secondary-system-background);
  padding: var(--spacing-2xl);
  border-radius: var(--corner-xl);
  margin-top: var(--spacing-3xl);
}

.tech-stack-header {
  text-align: center;
  margin-bottom: var(--spacing-xl);
}

.tech-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: var(--spacing-l);
}

.tech-card {
  background: var(--system-background);
  padding: var(--spacing-xl);
  border-radius: var(--corner-l);
  text-align: center;
  transition: all var(--duration-base) var(--spring);
}

.tech-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-s);
}

.tech-icon {
  width: 56px;
  height: 56px;
  margin: 0 auto var(--spacing-m);
  color: white;
  font-size: 1.25rem;
  font-weight: 700;
  border-radius: var(--corner-l);
  display: flex;
  align-items: center;
  justify-content: center;
  letter-spacing: 0.02em;
}

.tech-card h3 {
  font-size: var(--typography-headline);
  font-weight: 600;
  margin: 0 0 var(--spacing-xs);
  color: var(--label);
  letter-spacing: -0.01em;
}

.tech-card p {
  font-size: var(--typography-footnote);
  color: var(--secondary-label);
  margin: 0;
}

@media (max-width: 1024px) {
  .posts-grid,
  .snippets-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .tech-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .hero {
    padding: var(--spacing-2xl) 0;
  }
  
  .hero-title {
    font-size: var(--typography-title-1);
  }
  
  .hero-description {
    font-size: var(--typography-body);
  }
  
  .hero-actions {
    flex-direction: column;
    width: 100%;
  }
  
  .hero-actions .btn {
    width: 100%;
  }
  
  .section-header {
    flex-direction: column;
    align-items: flex-start;
    gap: var(--spacing-m);
  }
  
  .posts-grid,
  .snippets-grid {
    grid-template-columns: 1fr;
  }
  
  .tech-stack {
    padding: var(--spacing-l);
  }
  
  .tech-grid {
    grid-template-columns: 1fr;
  }
}
</style>
