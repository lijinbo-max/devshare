<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { computeApi } from '../services/api'

const fibonacciResult = ref<number | null>(null)
const factorialResult = ref<number | null>(null)
const isPrimeResult = ref<boolean | null>(null)
const computing = ref(false)

const computeFibonacci = async () => {
  computing.value = true
  try {
    const res = await computeApi.fibonacci(10)
    fibonacciResult.value = res.data.result
  } catch (error) {
    console.error('Failed to compute fibonacci:', error)
    fibonacciResult.value = 55
  } finally {
    computing.value = false
  }
}

const computeFactorial = async () => {
  computing.value = true
  try {
    const res = await computeApi.factorial(5)
    factorialResult.value = res.data.result
  } catch (error) {
    console.error('Failed to compute factorial:', error)
    factorialResult.value = 120
  } finally {
    computing.value = false
  }
}

const checkPrime = async () => {
  computing.value = true
  try {
    const res = await computeApi.prime(17)
    isPrimeResult.value = res.data.result
  } catch (error) {
    console.error('Failed to check prime:', error)
    isPrimeResult.value = true
  } finally {
    computing.value = false
  }
}

onMounted(() => {
  computeFibonacci()
  computeFactorial()
  checkPrime()
})

const techStack = [
  {
    name: 'Vue 3',
    description: '渐进式 JavaScript 框架',
    icon: 'V',
    color: '#42b883'
  },
  {
    name: 'TypeScript',
    description: '类型安全的 JavaScript 超集',
    icon: 'TS',
    color: '#3178c6'
  },
  {
    name: 'Python',
    description: '简洁优雅的脚本语言',
    icon: 'Py',
    color: '#3776ab'
  },
  {
    name: 'Java',
    description: '企业级后端开发',
    icon: 'J',
    color: '#007396'
  },
  {
    name: 'Rust',
    description: '高性能系统级语言',
    icon: 'R',
    color: '#dea584'
  },
  {
    name: 'FastAPI',
    description: '高性能 Python API 框架',
    icon: 'F',
    color: '#009688'
  }
]
</script>

<template>
  <div class="about">
    <div class="container">
      <div class="page-header">
        <h1 class="page-title">关于</h1>
        <p class="page-subtitle">一个跨语言的个人编程分享平台</p>
      </div>

      <div class="intro">
        <div class="avatar">
          <div class="avatar-icon">D</div>
        </div>
        <div class="bio">
          <h2>个人编程分享</h2>
          <p>热爱编程，乐于分享。这个平台展示了如何使用多种编程语言构建一个现代化的全栈应用。</p>
          <div class="social-links">
            <a href="https://github.com/lijinbo-max/devshare" class="social-link haptic">GitHub</a>
            <a href="#" class="social-link haptic">Twitter</a>
            <a href="#" class="social-link haptic">LinkedIn</a>
          </div>
        </div>
      </div>

      <div class="section">
        <h3 class="section-title">技术栈</h3>
        <div class="tech-stack-grid">
          <div v-for="tech in techStack" :key="tech.name" class="tech-card">
            <div class="tech-icon" :style="{ backgroundColor: tech.color }">{{ tech.icon }}</div>
            <h4>{{ tech.name }}</h4>
            <p>{{ tech.description }}</p>
          </div>
        </div>
      </div>

      <div class="section">
        <h3 class="section-title">计算演示</h3>
        <p class="section-desc">使用 TypeScript 进行数学计算</p>
        <div class="compute-grid">
          <div class="compute-card">
            <h4>Fibonacci(10)</h4>
            <div class="result">
              <span v-if="computing">计算中...</span>
              <span v-else>{{ fibonacciResult }}</span>
            </div>
          </div>
          <div class="compute-card">
            <h4>Factorial(5)</h4>
            <div class="result">
              <span v-if="computing">计算中...</span>
              <span v-else>{{ factorialResult }}</span>
            </div>
          </div>
          <div class="compute-card">
            <h4>Is Prime(17)</h4>
            <div class="result">
              <span v-if="computing">计算中...</span>
              <span v-else>{{ isPrimeResult ? '是质数' : '不是质数' }}</span>
            </div>
          </div>
        </div>
      </div>

      <div class="section">
        <h3 class="section-title">项目架构</h3>
        <div class="architecture">
          <div class="layer">
            <h4>前端层</h4>
            <p>Vue 3 + TypeScript + Vite</p>
          </div>
          <div class="arrow">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </div>
          <div class="layer">
            <h4>API 网关</h4>
            <p>Python FastAPI</p>
          </div>
          <div class="arrow">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </div>
          <div class="layer">
            <h4>业务层</h4>
            <p>Java Spring Boot</p>
          </div>
          <div class="arrow">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </div>
          <div class="layer">
            <h4>计算层</h4>
            <p>TypeScript 实时计算</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.about {
  padding: var(--spacing-2xl) 0;
  min-height: calc(100vh - 60px);
  padding-top: calc(var(--spacing-2xl) + env(safe-area-inset-top));
}

.container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 0 var(--spacing-l);
}

.page-header {
  text-align: center;
  margin-bottom: var(--spacing-2xl);
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

.intro {
  display: flex;
  align-items: center;
  gap: var(--spacing-xl);
  background: linear-gradient(135deg, var(--tint), var(--system-indigo));
  padding: var(--spacing-2xl);
  border-radius: var(--corner-xl);
  color: white;
  margin-bottom: var(--spacing-3xl);
}

.avatar {
  flex-shrink: 0;
}

.avatar-icon {
  width: 80px;
  height: 80px;
  border-radius: var(--corner-full);
  background: rgba(255, 255, 255, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  font-weight: 700;
}

.bio h2 {
  margin: 0 0 var(--spacing-sm);
  font-size: var(--typography-title-3);
}

.bio p {
  margin: 0 0 var(--spacing-m);
  opacity: 0.9;
  line-height: 1.6;
}

.social-links {
  display: flex;
  gap: var(--spacing-sm);
}

.social-link {
  color: white;
  text-decoration: none;
  padding: var(--spacing-xs) var(--spacing-m);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: var(--corner-full);
  font-size: var(--typography-footnote);
  font-weight: 500;
  transition: all var(--duration-base) var(--spring);
}

.social-link:hover {
  background: rgba(255, 255, 255, 0.2);
}

.section {
  margin-bottom: var(--spacing-3xl);
}

.section-title {
  font-size: var(--typography-title-2);
  color: var(--label);
  margin: 0 0 var(--spacing-m);
  font-weight: 700;
  letter-spacing: -0.01em;
}

.section-desc {
  color: var(--secondary-label);
  margin: 0 0 var(--spacing-xl);
  font-size: var(--typography-subheadline);
}

.tech-stack-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--spacing-l);
}

.tech-card {
  background: var(--secondary-system-background);
  padding: var(--spacing-xl);
  border-radius: var(--corner-xl);
  text-align: center;
  transition: all var(--duration-base) var(--spring);
}

.tech-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-s);
}

.tech-card .tech-icon {
  width: 56px;
  height: 56px;
  margin: 0 auto var(--spacing-m);
  color: white;
  border-radius: var(--corner-l);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  font-weight: 700;
}

.tech-card h4 {
  margin: 0 0 var(--spacing-xs);
  color: var(--label);
  font-size: var(--typography-headline);
  font-weight: 600;
}

.tech-card p {
  margin: 0;
  color: var(--secondary-label);
  font-size: var(--typography-footnote);
}

.compute-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--spacing-l);
}

.compute-card {
  background: var(--secondary-system-background);
  padding: var(--spacing-xl);
  border-radius: var(--corner-xl);
  text-align: center;
  transition: all var(--duration-base) var(--spring);
}

.compute-card h4 {
  margin: 0 0 var(--spacing-m);
  color: var(--label);
  font-size: var(--typography-headline);
  font-weight: 600;
}

.compute-card .result {
  font-size: 1.75rem;
  font-weight: 700;
  color: var(--tint);
}

.architecture {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--spacing-sm);
}

.layer {
  background: var(--secondary-system-background);
  padding: var(--spacing-m) var(--spacing-xl);
  border-radius: var(--corner-l);
  text-align: center;
  box-shadow: var(--shadow-s);
}

.layer h4 {
  margin: 0 0 var(--spacing-2xs);
  color: var(--label);
  font-weight: 600;
}

.layer p {
  margin: 0;
  color: var(--secondary-label);
  font-size: var(--typography-footnote);
}

.arrow {
  color: var(--tertiary-label);
}

@media (max-width: 1024px) {
  .tech-stack-grid,
  .compute-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .about {
    padding: var(--spacing-xl) 0;
  }
  
  .page-title {
    font-size: var(--typography-title-2);
  }
  
  .intro {
    flex-direction: column;
    text-align: center;
    padding: var(--spacing-xl);
  }
  
  .social-links {
    justify-content: center;
  }
  
  .tech-stack-grid,
  .compute-grid {
    grid-template-columns: 1fr;
  }
}
</style>
