<script setup lang="ts">
import Header from './layouts/Header.vue'
import { useTheme } from './hooks'

const { currentTheme, themeMode, toggleTheme } = useTheme()
</script>

<template>
  <div class="app">
    <Header @toggle-theme="toggleTheme" :theme="currentTheme" :theme-mode="themeMode" />
    <main>
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>
    <footer class="footer">
      <div class="container">
        <div class="footer-main">
          <div class="footer-brand">
            <div class="brand-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="12 18 19.5 12 12 6"></polyline>
                <polyline points="12 18 4.5 12 12 6"></polyline>
              </svg>
            </div>
            <div class="brand-info">
              <h3>DevShare</h3>
              <p>跨语言编程分享平台</p>
            </div>
          </div>
          
          <nav class="footer-nav">
            <ul>
              <li><a href="/blog">技术博客</a></li>
              <li><a href="/snippets">代码片段</a></li>
              <li><a href="/about">关于我们</a></li>
              <li><a href="https://github.com/lijinbo-max/devshare" target="_blank" rel="noopener noreferrer">GitHub</a></li>
            </ul>
          </nav>
        </div>
        
        <div class="footer-bottom">
          <div class="footer-info">
            <p class="copyright">© 2026 DevShare. All rights reserved.</p>
            <a href="https://beian.miit.gov.cn" class="icp-link" target="_blank" rel="noopener noreferrer">
              蜀ICP备2026021872号-3
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                <polyline points="15 3 21 3 21 9"></polyline>
                <line x1="10" y1="14" x2="21" y2="3"></line>
              </svg>
            </a>
          </div>
          <div class="social-links">
            <a href="https://github.com/lijinbo-max/devshare" class="social-link" target="_blank" rel="noopener noreferrer" aria-label="GitHub">
              <svg viewBox="0 0 24 24" fill="currentColor">
                <path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.09.682-.216.682-.487 0-.237-.009-.868-.013-1.7-2.782.603-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.031 1.531 1.031.892 1.53 2.341 1.087 2.91.831.092-.646.35-1.086.636-1.336-2.22-.253-4.555-1.113-4.555-4.943 0-1.091.39-1.984 1.029-2.683-.103-.253-.446-1.272.098-2.647 0 0 .84-.269 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.114 2.504.336 1.909-1.295 2.747-1.026 2.747-1.026.546 1.375.203 2.394.1 2.647.64.699 1.028 1.592 1.028 2.683 0 3.842-2.339 4.687-4.566 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .277.18.589.688.481C19.138 20.176 22 16.438 22 12.017 22 6.484 17.522 2 12 2z" clip-rule="evenodd"/>
              </svg>
            </a>
            <a href="https://weibo.com" class="social-link" target="_blank" rel="noopener noreferrer" aria-label="微博">
              <svg viewBox="0 0 24 24" fill="currentColor">
                <path d="M10.098 20.323c-3.977.391-7.414-1.406-7.672-4.02-.259-2.609 2.759-5.047 6.74-5.441 3.979-.394 7.413 1.404 7.671 4.018.259 2.6-2.759 5.049-6.739 5.443zM9.05 17.219c-.384.414-1.208.461-1.64.072-.432-.389-.479-1.204-.096-1.618.383-.413 1.207-.46 1.639-.071.433.39.48 1.205.097 1.617zm1.048-1.627c-.221.367-.768.472-1.12.203-.352-.27-.4-.776-.179-1.143.222-.366.769-.471 1.121-.202.352.269.4.775.178 1.142zm4.58-1.791c-1.572-.089-3.02.512-3.886 1.486-.866.974-1.21 2.436-.844 3.883.18.698.733 1.216 1.403 1.379.018.005.036.01.054.015 1.418.401 3.02-.449 4.073-1.709.338-.415.591-.904.728-1.419.213-.761.138-1.56-.225-2.27-.369-.725-1.066-1.263-1.908-1.375zm-1.633 1.233c-.111.242-.416.348-.641.203-.225-.146-.303-.451-.192-.693.111-.243.416-.349.642-.203.225.145.303.45.191.693zm2.746 1.124c-.23.184-.584.151-.762-.079-.179-.23-.146-.584.083-.763.23-.183.584-.15.762.08.179.23.146.584-.083.762z"/>
              </svg>
            </a>
            <a href="https://gitee.com" class="social-link" target="_blank" rel="noopener noreferrer" aria-label="Gitee">
              <svg viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/>
              </svg>
            </a>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<style scoped>
.app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background: var(--system-background);
  transition: background-color var(--duration-base) var(--spring);
}

main {
  flex: 1;
}

.footer {
  background: var(--secondary-system-background);
  color: var(--label);
  padding: var(--spacing-2xl) 0;
  margin-top: auto;
  border-top: 0.5px solid var(--separator);
  transition: all var(--duration-base) var(--spring);
}

.footer-main {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--spacing-xl);
}

.footer-brand {
  display: flex;
  align-items: center;
  gap: var(--spacing-m);
}

.brand-icon {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, var(--tint), var(--system-cyan));
  color: #FFFFFF;
  border-radius: var(--corner-m);
  flex-shrink: 0;
}

.brand-icon svg {
  width: 18px;
  height: 18px;
}

.brand-info h3 {
  font-size: var(--typography-headline);
  font-weight: 600;
  margin-bottom: 2px;
  letter-spacing: -0.01em;
}

.brand-info p {
  color: var(--secondary-label);
  font-size: var(--typography-footnote);
  margin: 0;
}

.footer-nav ul {
  display: flex;
  gap: var(--spacing-xl);
  list-style: none;
  padding: 0;
  margin: 0;
}

.footer-nav a {
  color: var(--secondary-label);
  font-size: var(--typography-callout);
  font-weight: 500;
  transition: all var(--duration-fast) var(--spring);
}

.footer-nav a:hover {
  color: var(--tint);
}

.footer-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: var(--spacing-xl);
  border-top: 0.5px solid var(--separator);
  flex-wrap: wrap;
  gap: var(--spacing-m);
}

.footer-info {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-2xs);
}

.copyright {
  color: var(--tertiary-label);
  font-size: var(--typography-caption-1);
}

.icp-link {
  display: inline-flex;
  align-items: center;
  gap: var(--spacing-xs);
  color: var(--secondary-label);
  font-size: var(--typography-caption-1);
  font-weight: 500;
  text-decoration: none;
  transition: all var(--duration-fast) var(--spring);
  padding: var(--spacing-2xs) var(--spacing-xs);
  border-radius: var(--corner-s);
}

.icp-link:hover {
  color: var(--tint);
  background: var(--system-fill);
  text-decoration: none;
}

.icp-link svg {
  width: 14px;
  height: 14px;
}

.social-links {
  display: flex;
  gap: var(--spacing-m);
}

.social-link {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--system-fill);
  border-radius: var(--corner-s);
  color: var(--secondary-label);
  transition: all var(--duration-fast) var(--spring);
}

.social-link:hover {
  background: var(--tint);
  color: #FFFFFF;
  transform: translateY(-2px);
}

.social-link svg {
  width: 14px;
  height: 14px;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity var(--duration-base) var(--spring);
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

@media (max-width: 768px) {
  .footer-main {
    flex-direction: column;
    gap: var(--spacing-l);
    text-align: center;
  }
  
  .footer-nav ul {
    flex-wrap: wrap;
    justify-content: center;
    gap: var(--spacing-l);
  }
  
  .footer-bottom {
    flex-direction: column;
    gap: var(--spacing-m);
    text-align: center;
  }
}
</style>
