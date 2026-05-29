export interface Post {
  id: number
  title: string
  content: string
  author: string
  createdAt: string
  updatedAt: string
  tags: string[]
}

export interface Snippet {
  id: number
  title: string
  code: string
  language: string
  description: string
  createdAt: string
}

export interface User {
  id: number
  name: string
  email: string
  bio: string
  github: string
  avatar: string
}

export interface ComputeResult {
  result: number
  computationTime: string
}

export interface Tag {
  name: string
  count: number
}