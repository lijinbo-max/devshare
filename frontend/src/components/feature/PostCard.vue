<script setup lang="ts">
import type { Post } from '../../types'

defineProps<{
  post: Post
}>()

const emit = defineEmits<{
  click: [post: Post]
}>()

const formatDate = (dateString: string): string => {
  const date = new Date(dateString)
  return date.toLocaleDateString('zh-CN', { year: 'numeric', month: 'short', day: 'numeric' })
}
</script>

<template>
  <article class="post-card" @click="emit('click', post)">
    <div class="post-card-inner">
      <div class="post-card-header">
        <span class="badge badge-tint">
          {{ post.tags[0] || '技术' }}
        </span>
        <time class="post-date">{{ formatDate(post.createdAt) }}</time>
      </div>
      
      <h3 class="post-title">{{ post.title }}</h3>
      <p class="post-excerpt">{{ post.content }}</p>
      
      <div class="post-footer">
        <div class="author-info">
          <div class="author-avatar">
            {{ post.author.charAt(0) }}
          </div>
          <span class="author-name">{{ post.author }}</span>
        </div>
        <div class="post-tags">
          <span 
            v-for="tag in post.tags.slice(1, 3)" 
            :key="tag" 
            class="tag"
          >
            {{ tag }}
          </span>
        </div>
      </div>
    </div>
  </article>
</template>

<style scoped>
.post-card {
  background: var(--secondary-system-background);
  border-radius: var(--corner-xl);
  overflow: hidden;
  transition: all var(--duration-base) var(--spring);
  cursor: pointer;
}

.post-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-m);
}

.post-card:active {
  transform: translateY(0);
}

.post-card-inner {
  padding: var(--spacing-xl);
  display: flex;
  flex-direction: column;
  gap: var(--spacing-m);
  height: 100%;
}

.post-card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--spacing-s);
}

.post-date {
  font-size: var(--typography-caption-1);
  color: var(--tertiary-label);
  font-weight: 500;
  letter-spacing: 0.01em;
}

.post-title {
  font-size: var(--typography-title-3);
  font-weight: 600;
  color: var(--label);
  margin: 0;
  line-height: 1.3;
  letter-spacing: -0.02em;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.post-card:hover .post-title {
  color: var(--tint);
}

.post-excerpt {
  font-size: var(--typography-subheadline);
  color: var(--secondary-label);
  line-height: 1.5;
  margin: 0;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.post-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: var(--spacing-m);
  margin-top: auto;
  border-top: 0.5px solid var(--separator);
}

.author-info {
  display: flex;
  align-items: center;
  gap: var(--spacing-s);
}

.author-avatar {
  width: 28px;
  height: 28px;
  border-radius: var(--corner-full);
  background: var(--tint);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: var(--typography-caption-1);
  letter-spacing: 0.02em;
}

.author-name {
  font-size: var(--typography-footnote);
  font-weight: 500;
  color: var(--label);
}

.post-tags {
  display: flex;
  gap: var(--spacing-xs);
}

.tag {
  background: var(--tertiary-system-background);
  color: var(--secondary-label);
  padding: 4px 10px;
  border-radius: var(--corner-full);
  font-size: var(--typography-caption-2);
  font-weight: 500;
  transition: all var(--duration-fast) var(--spring);
}

.post-card:hover .tag {
  background: var(--system-fill);
  color: var(--label);
}

@media (max-width: 768px) {
  .post-card-inner {
    padding: var(--spacing-l);
  }
  
  .post-title {
    font-size: var(--typography-headline);
  }
  
  .post-footer {
    flex-direction: column;
    gap: var(--spacing-s);
    align-items: flex-start;
  }
}
</style>
