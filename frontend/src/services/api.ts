import axios, { type AxiosInstance, type AxiosResponse, type AxiosError } from 'axios'

interface ApiConfig {
  baseURL: string
  timeout?: number
  headers?: Record<string, string>
}

export const createApiClient = (config: ApiConfig): AxiosInstance => {
  const { baseURL, timeout = 15000, headers = {} } = config

  const client = axios.create({
    baseURL,
    timeout,
    headers: {
      'Content-Type': 'application/json',
      ...headers
    }
  })

  client.interceptors.request.use(
    (config) => {
      const token = localStorage.getItem('token')
      if (token) {
        config.headers.Authorization = `Bearer ${token}`
      }
      return config
    },
    (error) => Promise.reject(error)
  )

  client.interceptors.response.use(
    (response: AxiosResponse) => response,
    (error: AxiosError) => {
      if (error.response?.status === 401) {
        localStorage.removeItem('token')
        window.location.href = '/login'
      }
      console.warn(`API error: ${error.message}`)
      return Promise.reject(error)
    }
  )

  return client
}

export const handleApiError = (error: unknown): string => {
  if (axios.isAxiosError(error)) {
    return error.response?.data?.message || error.message || '请求失败'
  }
  return '未知错误'
}

export const apiUrls = {
  posts: '/api/posts',
  snippets: '/api/snippets',
  users: '/api/users',
  compute: {
    fibonacci: '/compute/fibonacci',
    factorial: '/compute/factorial',
    prime: '/compute/is_prime'
  }
} as const

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000'
const JAVA_API_URL = import.meta.env.VITE_JAVA_API_URL || 'http://localhost:8080'
const RUST_API_URL = import.meta.env.VITE_RUST_API_URL || 'http://localhost:8081'

const pythonApi = createApiClient({ baseURL: API_BASE_URL })
const javaApi = createApiClient({ baseURL: JAVA_API_URL })
const rustApi = createApiClient({ baseURL: RUST_API_URL })

export const rustComputeApi = {
  fibonacci: (n: number) => rustApi.get<{ result: number; computation_time: string }>(`/compute/fibonacci/${n}`),
  factorial: (n: number) => rustApi.get<{ result: number; computation_time: string }>(`/compute/factorial/${n}`),
  isPrime: (n: number) => rustApi.get<{ result: boolean; computation_time: string }>(`/compute/is_prime/${n}`)
}

export const useRustApi = () => rustApi

const mockPosts = [
  {
    id: 1,
    title: 'Vue 3 Composition API 入门指南',
    content: 'Composition API 是 Vue 3 引入的新特性，它提供了更灵活的代码组织方式，让逻辑复用更加直观。通过 setup 函数和响应式 API，开发者可以更好地组织大型应用的代码结构。ref 和 reactive 是最常用的响应式工具，computed 用于创建计算属性，watch 用于监听数据变化。',
    author: '个人编程分享',
    createdAt: '2026-05-29',
    updatedAt: '2026-05-29',
    tags: ['Vue', 'JavaScript', '前端']
  },
  {
    id: 2,
    title: 'Python FastAPI 高性能 Web 框架',
    content: 'FastAPI 是一个现代、快速的 Web 框架，用于构建 API。它基于 Python 3.6+，具有自动交互式文档、高性能和易于使用等特点。FastAPI 支持异步编程，配合 Pydantic 进行数据验证，可以快速构建高质量的 RESTful API。',
    author: '个人编程分享',
    createdAt: '2026-05-28',
    updatedAt: '2026-05-28',
    tags: ['Python', 'FastAPI', '后端']
  },
  {
    id: 3,
    title: 'Rust 内存安全与所有权系统',
    content: 'Rust 的所有权系统是其最独特的特性之一，它使 Rust 能够在编译时保证内存安全，而无需垃圾回收器。所有权规则包括：每个值都有一个所有者、值在任意时刻只能有一个所有者、当所有者离开作用域时值被丢弃。',
    author: '个人编程分享',
    createdAt: '2026-05-27',
    updatedAt: '2026-05-27',
    tags: ['Rust', '系统编程', '内存安全']
  },
  {
    id: 4,
    title: 'TypeScript 类型体操入门',
    content: 'TypeScript 的类型系统非常强大，可以在编译时捕获很多错误。类型体操是指使用 TypeScript 的高级类型特性来解决复杂的类型问题，包括泛型、条件类型、映射类型、模板字面量类型等。',
    author: '个人编程分享',
    createdAt: '2026-05-26',
    updatedAt: '2026-05-26',
    tags: ['TypeScript', '前端', '类型系统']
  },
  {
    id: 5,
    title: 'Docker 容器化部署实践',
    content: 'Docker 是一个开源的应用容器引擎，可以让开发者打包应用及其依赖项到一个可移植的容器中。Dockerfile 是构建镜像的蓝图，docker-compose 可以编排多个容器。容器化可以确保应用在任何环境中都能一致地运行。',
    author: '个人编程分享',
    createdAt: '2026-05-25',
    updatedAt: '2026-05-25',
    tags: ['Docker', 'DevOps', '部署']
  },
  {
    id: 6,
    title: 'React Hooks 最佳实践',
    content: 'React Hooks 让函数组件能够使用状态和其他 React 特性。常用的 Hooks 包括 useState、useEffect、useContext、useReducer 等。遵循 Hooks 规则：只在函数组件顶层调用 Hooks，不要在循环、条件或嵌套函数中调用。',
    author: '个人编程分享',
    createdAt: '2026-05-24',
    updatedAt: '2026-05-24',
    tags: ['React', 'JavaScript', '前端']
  },
  {
    id: 7,
    title: 'Git 工作流最佳实践',
    content: 'Git 是分布式版本控制系统，合理的工作流可以提高团队协作效率。常见的工作流包括 Git Flow、GitHub Flow、Trunk-Based Development。推荐使用语义化提交信息，保持提交历史清晰可读。',
    author: '个人编程分享',
    createdAt: '2026-05-23',
    updatedAt: '2026-05-23',
    tags: ['Git', '版本控制', '协作']
  },
  {
    id: 8,
    title: 'Go 并发编程入门',
    content: 'Go 语言天生支持并发，goroutine 是轻量级线程，channel 用于 goroutine 之间的通信。通过 select 语句可以处理多个 channel，sync 包提供了互斥锁和原子操作等同步原语。',
    author: '个人编程分享',
    createdAt: '2026-05-22',
    updatedAt: '2026-05-22',
    tags: ['Go', '并发', '后端']
  }
]

const mockSnippets = [
  {
    id: 1,
    title: '快速排序算法',
    code: 'def quicksort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[len(arr) // 2]\n    left = [x for x in arr if x < pivot]\n    middle = [x for x in arr if x == pivot]\n    right = [x for x in arr if x > pivot]\n    return quicksort(left) + middle + quicksort(right)',
    language: 'Python',
    description: '经典的快速排序实现',
    createdAt: '2026-05-26'
  },
  {
    id: 2,
    title: 'Fibonacci 递归优化',
    code: 'fn fibonacci(n: u32) -> u32 {\n    match n {\n        0 => 0,\n        1 => 1,\n        _ => fibonacci(n - 1) + fibonacci(n - 2)\n    }\n}',
    language: 'Rust',
    description: 'Rust 递归 Fibonacci 实现',
    createdAt: '2026-05-25'
  },
  {
    id: 3,
    title: 'Vue 响应式数据',
    code: 'import { ref, computed } from \'vue\'\n\nconst count = ref(0)\nconst doubled = computed(() => count.value * 2)',
    language: 'TypeScript',
    description: 'Vue 3 响应式 API 示例',
    createdAt: '2026-05-24'
  },
  {
    id: 4,
    title: 'Go HTTP 服务器',
    code: 'package main\n\nimport (\n    \"fmt\"\n    \"net/http\"\n)\n\nfunc handler(w http.ResponseWriter, r *http.Request) {\n    fmt.Fprintf(w, \"Hello, World!\")\n}\n\nfunc main() {\n    http.HandleFunc(\"/\", handler)\n    http.ListenAndServe(\":8080\", nil)\n}',
    language: 'Go',
    description: 'Go 语言简单 HTTP 服务器',
    createdAt: '2026-05-23'
  },
  {
    id: 5,
    title: 'JavaScript 防抖函数',
    code: 'function debounce(fn, delay) {\n    let timer = null\n    return function(...args) {\n        if (timer) clearTimeout(timer)\n        timer = setTimeout(() => {\n            fn.apply(this, args)\n        }, delay)\n    }\n}',
    language: 'JavaScript',
    description: '防抖函数实现',
    createdAt: '2026-05-22'
  },
  {
    id: 6,
    title: 'Java Stream API',
    code: 'List<String> names = Arrays.asList(\"Alice\", \"Bob\", \"Charlie\");\n\nList<String> result = names.stream()\n    .filter(name -> name.length() > 3)\n    .map(String::toUpperCase)\n    .collect(Collectors.toList());',
    language: 'Java',
    description: 'Java 8 Stream API 示例',
    createdAt: '2026-05-21'
  },
  {
    id: 7,
    title: 'C++ 智能指针',
    code: '#include <memory>\n#include <iostream>\n\nint main() {\n    std::unique_ptr<int> ptr = std::make_unique<int>(42);\n    std::cout << *ptr << std::endl;\n    return 0;\n}',
    language: 'C++',
    description: 'C++11 智能指针使用',
    createdAt: '2026-05-20'
  },
  {
    id: 8,
    title: 'Ruby 块与迭代器',
    code: '(1..5).each do |n|\n  puts \"Number: #{n}\"\nend\n\nresult = (1..5).map { |x| x * 2 }',
    language: 'Ruby',
    description: 'Ruby 块和迭代器示例',
    createdAt: '2026-05-19'
  },
  {
    id: 9,
    title: 'Python 装饰器',
    code: 'def logger(func):\n    def wrapper(*args, **kwargs):\n        print(f\"Calling {func.__name__}\")\n        result = func(*args, **kwargs)\n        print(f\"Done {func.__name__}\")\n        return result\n    return wrapper\n\n@logger\ndef add(a, b):\n    return a + b',
    language: 'Python',
    description: 'Python 装饰器示例',
    createdAt: '2026-05-18'
  },
  {
    id: 10,
    title: 'TypeScript 泛型',
    code: 'function identity<T>(arg: T): T {\n    return arg\n}\n\ninterface Container<T> {\n    value: T\n    getValue(): T\n}',
    language: 'TypeScript',
    description: 'TypeScript 泛型使用',
    createdAt: '2026-05-17'
  }
]

export const blogApi = {
  getPosts: async () => {
    try {
      const response = await pythonApi.get('/api/posts')
      return response
    } catch (error) {
      console.log('Using mock posts data')
      return { data: mockPosts }
    }
  },
  getPost: async (id: number) => {
    try {
      const response = await pythonApi.get(`/api/posts/${id}`)
      return response
    } catch (error) {
      console.log('Using mock post data for id:', id)
      const post = mockPosts.find(p => p.id === id) || mockPosts[0]
      return { data: post }
    }
  },
  createPost: (data: any) => pythonApi.post('/api/posts', data),
  updatePost: (id: number, data: any) => pythonApi.put(`/api/posts/${id}`, data),
  deletePost: (id: number) => pythonApi.delete(`/api/posts/${id}`)
}

export const snippetApi = {
  getSnippets: async () => {
    try {
      const response = await pythonApi.get('/api/snippets')
      return response
    } catch (error) {
      console.log('Using mock snippets data')
      return { data: mockSnippets }
    }
  },
  getSnippet: async (id: number) => {
    try {
      const response = await pythonApi.get(`/api/snippets/${id}`)
      return response
    } catch (error) {
      console.log('Using mock snippet data for id:', id)
      const snippet = mockSnippets.find(s => s.id === id) || mockSnippets[0]
      return { data: snippet }
    }
  },
  createSnippet: (data: any) => pythonApi.post('/api/snippets', data)
}

export const userApi = {
  getUser: (id: number) => javaApi.get(`/api/users/${id}`),
  createUser: (data: any) => javaApi.post('/api/users', data),
  updateUser: (id: number, data: any) => javaApi.put(`/api/users/${id}`, data)
}

export const computeApi = {
  fibonacci: (n: number) => {
    const fib = (num: number): number => num <= 1 ? num : fib(num - 1) + fib(num - 2)
    return Promise.resolve({ data: { result: fib(n) } })
  },
  factorial: (n: number) => {
    const fact = (num: number): number => num <= 1 ? 1 : num * fact(num - 1)
    return Promise.resolve({ data: { result: fact(n) } })
  },
  prime: (n: number) => {
    const isPrime = (num: number): boolean => {
      if (num <= 1) return false
      if (num <= 3) return true
      if (num % 2 === 0 || num % 3 === 0) return false
      for (let i = 5; i * i <= num; i += 6) {
        if (num % i === 0 || num % (i + 2) === 0) return false
      }
      return true
    }
    return Promise.resolve({ data: { result: isPrime(n) } })
  }
}

export default {
  blogApi,
  snippetApi,
  computeApi,
  userApi
}
