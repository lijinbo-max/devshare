import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Blog from '../views/Blog.vue'
import PostDetail from '../views/PostDetail.vue'
import CodeSnippets from '../views/CodeSnippets.vue'
import About from '../views/About.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'Home', component: Home },
    { path: '/blog', name: 'Blog', component: Blog },
    { path: '/blog/:id', name: 'PostDetail', component: PostDetail },
    { path: '/snippets', name: 'CodeSnippets', component: CodeSnippets },
    { path: '/about', name: 'About', component: About }
  ]
})

export default router