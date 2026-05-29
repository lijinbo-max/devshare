from typing import List
from datetime import datetime
from app.schemas import Post, Snippet


posts_db: List[Post] = [
    Post(
        id=1,
        title="Vue 3 Composition API 入门指南",
        content="Composition API 是 Vue 3 引入的新特性，它提供了更灵活的代码组织方式。通过 ref、reactive、computed 等响应式 API，我们可以更好地组织组件逻辑。Composition API 解决了 Options API 在处理复杂组件时的代码分散问题，让相关逻辑可以组织在一起。",
        author="DevShare",
        createdAt="2026-05-29",
        updatedAt="2026-05-29",
        tags=["Vue", "JavaScript", "前端"]
    ),
    Post(
        id=2,
        title="Python FastAPI 高性能 Web 框架",
        content="FastAPI 是一个现代、快速的 Web 框架，用于构建 API。它基于 Starlette 和 Pydantic，提供了自动文档、类型提示支持和异步支持。FastAPI 的性能非常出色，可以与 Node.js 和 Go 相媲美。",
        author="DevShare",
        createdAt="2026-05-28",
        updatedAt="2026-05-28",
        tags=["Python", "FastAPI", "后端"]
    ),
    Post(
        id=3,
        title="Rust 内存安全与所有权系统",
        content="Rust 的所有权系统是其最独特的特性之一，它使 Rust 能够在编译时保证内存安全，而不需要垃圾收集器。所有权规则包括：每个值都有一个所有者，值在任意时刻只能有一个所有者，当所有者离开作用域，值将被丢弃。",
        author="DevShare",
        createdAt="2026-05-27",
        updatedAt="2026-05-27",
        tags=["Rust", "系统编程", "内存安全"]
    ),
    Post(
        id=4,
        title="Java Spring Boot 最佳实践",
        content="Spring Boot 简化了 Spring 应用的开发过程。通过自动配置和约定优于配置的原则，我们可以快速构建生产级应用。本文介绍了一些最佳实践，包括依赖管理、配置管理、数据库连接池配置等。",
        author="DevShare",
        createdAt="2026-05-26",
        updatedAt="2026-05-26",
        tags=["Java", "Spring", "后端"]
    ),
    Post(
        id=5,
        title="TypeScript 类型体操入门",
        content="TypeScript 的类型系统非常强大，可以表达复杂的类型关系。类型体操是指使用 TypeScript 的类型系统来解决各种类型问题，包括条件类型、映射类型、模板字面量类型等。",
        author="DevShare",
        createdAt="2026-05-25",
        updatedAt="2026-05-25",
        tags=["TypeScript", "前端", "类型系统"]
    ),
    Post(
        id=6,
        title="Docker 容器化部署实战",
        content="Docker 容器化技术已经成为现代应用部署的标准。本文介绍了如何使用 Docker 构建和部署多语言应用，包括 Dockerfile 编写、Docker Compose 配置和最佳实践。",
        author="DevShare",
        createdAt="2026-05-24",
        updatedAt="2026-05-24",
        tags=["Docker", "DevOps", "部署"]
    )
]

snippets_db: List[Snippet] = [
    Snippet(
        id=1,
        title="快速排序算法",
        code="def quicksort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[len(arr) // 2]\n    left = [x for x in arr if x < pivot]\n    middle = [x for x in arr if x == pivot]\n    right = [x for x in arr if x > pivot]\n    return quicksort(left) + middle + quicksort(right)",
        language="Python",
        description="经典的快速排序实现，使用分治策略",
        createdAt="2026-05-26"
    ),
    Snippet(
        id=2,
        title="Fibonacci 递归优化",
        code="fn fibonacci(n: u32) -> u32 {\n    match n {\n        0 => 0,\n        1 => 1,\n        _ => fibonacci(n - 1) + fibonacci(n - 2)\n    }\n}",
        language="Rust",
        description="Rust 递归 Fibonacci 实现",
        createdAt="2026-05-25"
    ),
    Snippet(
        id=3,
        title="Vue 响应式数据",
        code="import { ref, computed } from 'vue'\n\nconst count = ref(0)\nconst doubled = computed(() => count.value * 2)\n\nfunction increment() {\n  count.value++\n}",
        language="TypeScript",
        description="Vue 3 Composition API 响应式示例",
        createdAt="2026-05-24"
    ),
    Snippet(
        id=4,
        title="Java Stream API",
        code="List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);\nint sum = numbers.stream()\n    .filter(n -> n % 2 == 0)\n    .mapToInt(Integer::intValue)\n    .sum();\nSystem.out.println(sum);",
        language="Java",
        description="Java 8 Stream API 示例",
        createdAt="2026-05-23"
    ),
    Snippet(
        id=5,
        title="防抖函数",
        code="function debounce(fn, delay) {\n  let timeout = null\n  return function(...args) {\n    clearTimeout(timeout)\n    timeout = setTimeout(() => fn(...args), delay)\n  }\n}",
        language="JavaScript",
        description="JavaScript 防抖函数实现",
        createdAt="2026-05-22"
    ),
    Snippet(
        id=6,
        title="Rust HashMap",
        code="use std::collections::HashMap;\n\nlet mut map = HashMap::new();\nmap.insert(\"key\", \"value\");\n\nif let Some(value) = map.get(\"key\") {\n    println!(\"Value: {}\", value);\n}",
        language="Rust",
        description="Rust HashMap 基本操作",
        createdAt="2026-05-21"
    )
]


def get_all_posts() -> List[Post]:
    return posts_db


def get_post_by_id(post_id: int) -> Post | None:
    return next((p for p in posts_db if p.id == post_id), None)


def create_post(post: Post) -> Post:
    posts_db.append(post)
    return post


def update_post(post_id: int, updated_post: Post) -> Post | None:
    index = next((i for i, p in enumerate(posts_db) if p.id == post_id), None)
    if index is not None:
        posts_db[index] = updated_post
        return updated_post
    return None


def delete_post(post_id: int) -> bool:
    index = next((i for i, p in enumerate(posts_db) if p.id == post_id), None)
    if index is not None:
        posts_db.pop(index)
        return True
    return False


def get_all_snippets() -> List[Snippet]:
    return snippets_db


def get_snippet_by_id(snippet_id: int) -> Snippet | None:
    return next((s for s in snippets_db if s.id == snippet_id), None)


def create_snippet(snippet: Snippet) -> Snippet:
    snippets_db.append(snippet)
    return snippet
