<script setup lang="ts">
defineProps<{
  type?: 'post' | 'snippet' | 'hero' | 'tech'
}>()
</script>

<template>
  <div class="skeleton-wrapper">
    <template v-if="type === 'hero'">
      <div class="skeleton-hero">
        <div class="skeleton-badge"></div>
        <div class="skeleton-title"></div>
        <div class="skeleton-description"></div>
        <div class="skeleton-actions">
          <div class="skeleton-btn primary"></div>
          <div class="skeleton-btn secondary"></div>
        </div>
      </div>
    </template>

    <template v-else-if="type === 'post'">
      <div class="skeleton-card">
        <div class="skeleton-card-header">
          <div class="skeleton-badge small"></div>
          <div class="skeleton-date"></div>
        </div>
        <div class="skeleton-title-line"></div>
        <div class="skeleton-title-line short"></div>
        <div class="skeleton-excerpt"></div>
        <div class="skeleton-excerpt"></div>
        <div class="skeleton-excerpt short"></div>
        <div class="skeleton-card-footer">
          <div class="skeleton-avatar"></div>
          <div class="skeleton-author"></div>
        </div>
      </div>
    </template>

    <template v-else-if="type === 'snippet'">
      <div class="skeleton-card">
        <div class="skeleton-card-header">
          <div class="skeleton-badge small"></div>
          <div class="skeleton-date"></div>
        </div>
        <div class="skeleton-title-line"></div>
        <div class="skeleton-description"></div>
        <div class="skeleton-code-block">
          <div class="skeleton-code-lines">
            <div class="skeleton-code-line"></div>
            <div class="skeleton-code-line"></div>
            <div class="skeleton-code-line short"></div>
            <div class="skeleton-code-line"></div>
            <div class="skeleton-code-line short"></div>
          </div>
        </div>
      </div>
    </template>

    <template v-else-if="type === 'tech'">
      <div class="skeleton-tech-card">
        <div class="skeleton-tech-icon"></div>
        <div class="skeleton-tech-title"></div>
        <div class="skeleton-tech-desc"></div>
      </div>
    </template>

    <template v-else>
      <div class="skeleton-default">
        <div class="skeleton-line"></div>
        <div class="skeleton-line"></div>
        <div class="skeleton-line short"></div>
      </div>
    </template>
  </div>
</template>

<style scoped>
.skeleton-wrapper {
  width: 100%;
}

.skeleton-hero {
  text-align: center;
  padding: var(--spacing-3xl) var(--spacing-xl);
}

.skeleton-badge {
  display: inline-block;
  width: 180px;
  height: 32px;
  border-radius: var(--corner-full);
  background: linear-gradient(90deg, var(--tertiary-system-background) 25%, var(--secondary-system-fill) 50%, var(--tertiary-system-background) 75%);
  background-size: 200% 100%;
  animation: skeleton-loading 1.5s infinite;
  margin-bottom: var(--spacing-xl);
}

.skeleton-badge.small {
  width: 100px;
  height: 24px;
}

.skeleton-title {
  width: 60%;
  height: 44px;
  margin: 0 auto var(--spacing-lg);
  border-radius: var(--corner-s);
  background: linear-gradient(90deg, var(--tertiary-system-background) 25%, var(--secondary-system-fill) 50%, var(--tertiary-system-background) 75%);
  background-size: 200% 100%;
  animation: skeleton-loading 1.5s infinite 0.1s;
}

.skeleton-title-line {
  height: 22px;
  border-radius: var(--corner-s);
  background: linear-gradient(90deg, var(--tertiary-system-background) 25%, var(--secondary-system-fill) 50%, var(--tertiary-system-background) 75%);
  background-size: 200% 100%;
  animation: skeleton-loading 1.5s infinite;
  margin-bottom: var(--spacing-sm);
}

.skeleton-title-line.short {
  width: 70%;
}

.skeleton-description {
  width: 70%;
  height: 18px;
  margin: 0 auto var(--spacing-md);
  border-radius: var(--corner-s);
  background: linear-gradient(90deg, var(--tertiary-system-background) 25%, var(--secondary-system-fill) 50%, var(--tertiary-system-background) 75%);
  background-size: 200% 100%;
  animation: skeleton-loading 1.5s infinite 0.2s;
}

.skeleton-excerpt {
  height: 16px;
  border-radius: var(--corner-s);
  background: linear-gradient(90deg, var(--tertiary-system-background) 25%, var(--secondary-system-fill) 50%, var(--tertiary-system-background) 75%);
  background-size: 200% 100%;
  animation: skeleton-loading 1.5s infinite;
  margin-bottom: var(--spacing-xs);
}

.skeleton-excerpt.short {
  width: 60%;
}

.skeleton-actions {
  display: flex;
  justify-content: center;
  gap: var(--spacing-sm);
  margin-top: var(--spacing-xl);
}

.skeleton-btn {
  height: 44px;
  border-radius: var(--corner-l);
  background: linear-gradient(90deg, var(--tertiary-system-background) 25%, var(--secondary-system-fill) 50%, var(--tertiary-system-background) 75%);
  background-size: 200% 100%;
  animation: skeleton-loading 1.5s infinite;
}

.skeleton-btn.primary {
  width: 160px;
}

.skeleton-btn.secondary {
  width: 200px;
}

.skeleton-card {
  background: var(--secondary-system-background);
  border-radius: var(--corner-xl);
  padding: var(--spacing-xl);
}

.skeleton-card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--spacing-m);
}

.skeleton-date {
  width: 80px;
  height: 16px;
  border-radius: var(--corner-s);
  background: linear-gradient(90deg, var(--tertiary-system-background) 25%, var(--secondary-system-fill) 50%, var(--tertiary-system-background) 75%);
  background-size: 200% 100%;
  animation: skeleton-loading 1.5s infinite 0.15s;
}

.skeleton-card-footer {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  margin-top: var(--spacing-m);
  padding-top: var(--spacing-m);
  border-top: 0.5px solid var(--separator);
}

.skeleton-avatar {
  width: 32px;
  height: 32px;
  border-radius: var(--corner-full);
  background: linear-gradient(90deg, var(--tertiary-system-background) 25%, var(--secondary-system-fill) 50%, var(--tertiary-system-background) 75%);
  background-size: 200% 100%;
  animation: skeleton-loading 1.5s infinite;
}

.skeleton-author {
  width: 80px;
  height: 16px;
  border-radius: var(--corner-s);
  background: linear-gradient(90deg, var(--tertiary-system-background) 25%, var(--secondary-system-fill) 50%, var(--tertiary-system-background) 75%);
  background-size: 200% 100%;
  animation: skeleton-loading 1.5s infinite 0.1s;
}

.skeleton-code-block {
  background: var(--tertiary-system-background);
  border-radius: var(--corner-l);
  overflow: hidden;
  margin-top: var(--spacing-m);
}

.skeleton-code-lines {
  padding: var(--spacing-lg);
}

.skeleton-code-line {
  height: 16px;
  border-radius: var(--corner-s);
  background: var(--system-fill);
  margin-bottom: var(--spacing-xs);
}

.skeleton-code-line.short {
  width: 70%;
}

.skeleton-tech-card {
  background: var(--secondary-system-background);
  border-radius: var(--corner-xl);
  padding: var(--spacing-xl);
  text-align: center;
}

.skeleton-tech-icon {
  width: 56px;
  height: 56px;
  margin: 0 auto var(--spacing-m);
  border-radius: var(--corner-l);
  background: linear-gradient(90deg, var(--tertiary-system-background) 25%, var(--secondary-system-fill) 50%, var(--tertiary-system-background) 75%);
  background-size: 200% 100%;
  animation: skeleton-loading 1.5s infinite;
}

.skeleton-tech-title {
  height: 18px;
  width: 60%;
  margin: 0 auto var(--spacing-xs);
  border-radius: var(--corner-s);
  background: linear-gradient(90deg, var(--tertiary-system-background) 25%, var(--secondary-system-fill) 50%, var(--tertiary-system-background) 75%);
  background-size: 200% 100%;
  animation: skeleton-loading 1.5s infinite 0.1s;
}

.skeleton-tech-desc {
  height: 14px;
  width: 80%;
  margin: 0 auto;
  border-radius: var(--corner-s);
  background: linear-gradient(90deg, var(--tertiary-system-background) 25%, var(--secondary-system-fill) 50%, var(--tertiary-system-background) 75%);
  background-size: 200% 100%;
  animation: skeleton-loading 1.5s infinite 0.2s;
}

.skeleton-default {
  padding: var(--spacing-md);
}

.skeleton-line {
  height: 18px;
  border-radius: var(--corner-s);
  background: linear-gradient(90deg, var(--tertiary-system-background) 25%, var(--secondary-system-fill) 50%, var(--tertiary-system-background) 75%);
  background-size: 200% 100%;
  animation: skeleton-loading 1.5s infinite;
  margin-bottom: var(--spacing-sm);
}

.skeleton-line.short {
  width: 60%;
}

@keyframes skeleton-loading {
  0% {
    background-position: 200% 0;
  }
  100% {
    background-position: -200% 0;
  }
}
</style>
