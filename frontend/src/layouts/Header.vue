<script setup lang="ts">
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'

defineProps<{
  theme: 'light' | 'dark'
  themeMode: 'light' | 'dark' | 'system'
}>()

const emit = defineEmits<{
  toggleTheme: []
}>()

const router = useRouter()
const route = useRoute()
const isMenuOpen = ref(false)
const isScrolled = ref(false)
const isTablet = ref(false)

const checkDevice = () => {
  isTablet.value = window.innerWidth >= 768 && window.innerWidth < 1024
}

const systemIconType = computed(() => {
  if (isTablet.value) return 'tablet'
  return 'mobile'
})

const navItems = [
  { name: '首页', path: '/', icon: '🏠' },
  { name: '博客', path: '/blog', icon: '📝' },
  { name: '代码片段', path: '/snippets', icon: '💻' },
  { name: '关于', path: '/about', icon: 'ℹ️' }
]

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

const navigate = (path: string) => {
  router.push(path)
  isMenuOpen.value = false
}

const handleScroll = () => {
  isScrolled.value = window.scrollY > 10
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
  checkDevice()
  window.addEventListener('resize', checkDevice)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
  window.removeEventListener('resize', checkDevice)
})
</script>

<template>
  <header class="header" :class="{ scrolled: isScrolled }">
    <div class="header-inner">
      <div class="logo" @click="navigate('/')">
        <div class="logo-icon">
          <svg width="28" height="28" viewBox="0 0 28 28" fill="none">
            <rect width="28" height="28" rx="8" fill="var(--tint)"/>
            <path d="M8 12h4v4H8v-4zm6 0h4v6h-4v-4zm6 0h4v4h-4v-4z" fill="white" opacity="0.9"/>
          </svg>
        </div>
        <span class="logo-text">个人编程分享</span>
      </div>
      
      <nav class="nav-desktop">
        <ul class="nav-list">
          <li v-for="item in navItems" :key="item.path">
            <button 
              @click="navigate(item.path)"
              :class="['nav-link', { active: route.path === item.path }]"
            >
              {{ item.name }}
            </button>
          </li>
        </ul>
      </nav>

      <div class="header-actions">
        <button 
          class="theme-toggle haptic" 
          @click="emit('toggleTheme')"
          :aria-label="themeMode === 'system' ? '切换到浅色模式' : theme === 'dark' ? '切换到浅色模式' : '切换到深色模式'"
          :title="themeMode === 'system' ? '点击切换到浅色模式' : theme === 'dark' ? '点击切换到浅色模式' : '点击切换到深色模式'"
        >
          <svg v-if="themeMode === 'system' && systemIconType === 'mobile'" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <rect x="6" y="1" width="12" height="22" rx="2" ry="2"></rect>
            <line x1="12" y1="19" x2="12" y2="21"></line>
          </svg>
          <svg v-else-if="themeMode === 'system' && systemIconType === 'tablet'" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <rect x="4" y="2" width="16" height="20" rx="2" ry="2"></rect>
            <line x1="12" y1="18" x2="12" y2="22"></line>
          </svg>
          <svg v-else-if="theme === 'dark'" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
          </svg>
          <svg v-else width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="5"></circle>
            <line x1="12" y1="1" x2="12" y2="3"></line>
            <line x1="12" y1="21" x2="12" y2="23"></line>
            <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
            <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
            <line x1="1" y1="12" x2="3" y2="12"></line>
            <line x1="21" y1="12" x2="23" y2="12"></line>
            <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
            <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
          </svg>
        </button>
        
        <button class="menu-btn haptic" @click="toggleMenu" aria-label="菜单">
          <div class="menu-icon">
            <span class="menu-line" :class="{ open: isMenuOpen }"></span>
            <span class="menu-line" :class="{ open: isMenuOpen }"></span>
            <span class="menu-line" :class="{ open: isMenuOpen }"></span>
          </div>
        </button>
      </div>
    </div>
    
    <transition name="sheet">
      <div v-if="isMenuOpen" class="mobile-menu">
        <div class="mobile-menu-content">
          <div class="mobile-menu-header">
            <button class="close-btn haptic" @click="toggleMenu">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <line x1="18" y1="6" x2="6" y2="18"></line>
                <line x1="6" y1="6" x2="18" y2="18"></line>
              </svg>
            </button>
          </div>
          <ul class="mobile-nav-list">
            <li v-for="item in navItems" :key="item.path">
              <button 
                @click="navigate(item.path)"
                :class="['mobile-nav-link', { active: route.path === item.path }]"
              >
                <span class="mobile-nav-icon">{{ item.icon }}</span>
                <span class="mobile-nav-text">{{ item.name }}</span>
                <svg v-if="route.path === item.path" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <polyline points="9 18 15 12 9 6"></polyline>
                </svg>
              </button>
            </li>
          </ul>
        </div>
        <div class="mobile-menu-overlay" @click="toggleMenu"></div>
      </div>
    </transition>
  </header>
</template>

<style scoped>
.header {
  position: sticky;
  top: 0;
  z-index: var(--z-sticky);
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 0.5px solid var(--separator);
  transition: all var(--duration-base) var(--spring);
}

.header.scrolled {
  box-shadow: var(--shadow-s);
  background: rgba(255, 255, 255, 0.92);
}

[data-theme="dark"] .header {
  background: rgba(0, 0, 0, 0.8);
}

[data-theme="dark"] .header.scrolled {
  background: rgba(0, 0, 0, 0.92);
}

.header-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--spacing-l);
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 60px;
  gap: var(--spacing-l);
}

.logo {
  display: flex;
  align-items: center;
  gap: var(--spacing-s);
  cursor: pointer;
  transition: all var(--duration-fast) var(--spring);
}

.logo:hover {
  opacity: 0.8;
}

.logo:active {
  transform: scale(0.98);
}

.logo-icon {
  display: flex;
  align-items: center;
  justify-content: center;
}

.logo-text {
  font-size: var(--typography-headline);
  font-weight: 600;
  letter-spacing: -0.02em;
  color: var(--label);
}

.nav-desktop {
  flex: 1;
  display: flex;
  justify-content: center;
}

.nav-list {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
  gap: var(--spacing-xs);
}

.nav-link {
  display: block;
  padding: var(--spacing-xs) var(--spacing-m);
  color: var(--secondary-label);
  font-weight: 500;
  font-size: var(--typography-callout);
  border-radius: var(--corner-s);
  transition: all var(--duration-fast) var(--spring);
  letter-spacing: -0.01em;
}

.nav-link:hover {
  background: var(--system-fill);
  color: var(--label);
}

.nav-link.active {
  background: var(--tertiary-system-fill);
  color: var(--label);
  font-weight: 600;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: var(--spacing-xs);
}

.theme-toggle {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: var(--corner-m);
  color: var(--label);
  transition: all var(--duration-fast) var(--spring);
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
  touch-action: manipulation;
  z-index: 10;
}

.theme-toggle:hover {
  background: var(--system-fill);
}

.theme-toggle:active {
  transform: scale(0.95);
}

.menu-btn {
  display: none;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: var(--corner-m);
  color: var(--label);
}

.menu-btn:hover {
  background: var(--system-fill);
}

.menu-icon {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 8px;
}

.menu-line {
  display: block;
  width: 18px;
  height: 2px;
  background: var(--label);
  border-radius: 2px;
  transition: all var(--duration-base) var(--spring);
}

.menu-line.open:nth-child(1) {
  transform: rotate(45deg) translate(4px, 4px);
}

.menu-line.open:nth-child(2) {
  opacity: 0;
  transform: scaleX(0.5);
}

.menu-line.open:nth-child(3) {
  transform: rotate(-45deg) translate(4px, -4px);
}

.mobile-menu {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: var(--z-modal);
  display: flex;
  justify-content: flex-start;
}

.mobile-menu-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
}

.mobile-menu-content {
  position: relative;
  width: 100%;
  max-width: 280px;
  height: 100vh;
  background: var(--system-background);
  box-shadow: var(--shadow-xl);
  padding: var(--spacing-l);
  padding-top: calc(var(--spacing-l) + 60px);
  display: flex;
  flex-direction: column;
  gap: var(--spacing-xl);
  overflow-y: auto;
}

.mobile-menu-header {
  display: flex;
  justify-content: flex-end;
  padding: var(--spacing-xs) 0;
}

.close-btn {
  width: 36px;
  height: 36px;
  border-radius: var(--corner-s);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--label);
}

.close-btn:hover {
  background: var(--system-fill);
}

.mobile-nav-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: var(--spacing-2xs);
}

.mobile-nav-link {
  display: flex;
  align-items: center;
  gap: var(--spacing-m);
  padding: var(--spacing-s) var(--spacing-m);
  color: var(--label);
  border-radius: var(--corner-m);
  transition: all var(--duration-fast) var(--spring);
  text-align: left;
  width: 100%;
}

.mobile-nav-link:hover {
  background: var(--secondary-system-background);
}

.mobile-nav-link.active {
  background: var(--secondary-system-background);
  color: var(--tint);
}

.mobile-nav-link.active svg {
  margin-left: auto;
}

.mobile-nav-icon {
  font-size: 24px;
  line-height: 1;
}

.mobile-nav-text {
  font-weight: 500;
  font-size: var(--typography-headline);
  letter-spacing: -0.01em;
}

.sheet-enter-active,
.sheet-leave-active {
  transition: all var(--duration-slow) var(--spring);
}

.sheet-enter-from .mobile-menu-content,
.sheet-leave-to .mobile-menu-content {
  transform: translateX(100%);
}

.sheet-enter-from .mobile-menu-overlay,
.sheet-leave-to .mobile-menu-overlay {
  opacity: 0;
}

@media (max-width: 768px) {
  .nav-desktop {
    display: none;
  }
  
  .menu-btn {
    display: flex;
  }
  
  .header-inner {
    padding: 0 var(--spacing-m);
    height: 56px;
    position: relative;
    z-index: 1;
  }
  
  .logo-text {
    font-size: var(--typography-callout);
    max-width: 120px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  
  .logo-icon svg {
    width: 24px;
    height: 24px;
  }
  
  .header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: var(--z-fixed);
    background: rgba(255, 255, 255, 0.95);
  }
  
  [data-theme="dark"] .header {
    background: rgba(0, 0, 0, 0.95);
  }
}
</style>
