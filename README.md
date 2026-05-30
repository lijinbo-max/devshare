# DevShare - 个人编程分享平台

一个使用多种编程语言构建的现代化全栈个人编程分享平台，展示跨语言服务集成的最佳实践。

## ✨ 核心功能

- **博客文章管理** - 创建、阅读、更新、删除技术文章
- **代码片段展示** - 分享和展示各种编程语言的代码示例
- **高性能计算服务** - 基于 Rust 的斐波那契、阶乘、素数检测等计算功能
- **多语言服务集成** - Vue 3 前端、FastAPI、Spring Boot、Rust 服务协同工作
- **响应式设计** - 完美适配桌面、平板和移动设备
- **主题切换** - 支持浅色模式、深色模式和跟随系统模式
- **微信适配** - 针对微信浏览器优化，支持安全区域

## 🌐 在线访问

**生产环境**: https://ljbljb.com

## 🛠 技术栈

| 模块 | 技术 | 版本 | 端口 |
|------|------|------|------|
| 前端 | Vue 3 + TypeScript + Vite | Vue 3.5+ | 5173 |
| 后端 API | Python + FastAPI | Python 3.11+ | 8000 |
| 后端服务 | Java + Spring Boot | Java 21+ | 8080 |
| 高性能计算 | Rust + Axum | Rust 1.70+ | 8081 |

## 📁 项目结构

```
DevShare/
├── frontend/                     # Vue 3 + TypeScript 前端应用
│   ├── src/
│   │   ├── components/           # 组件目录
│   │   │   ├── common/          # 通用组件 (CodeBlock, Skeleton)
│   │   │   └── feature/         # 业务组件 (PostCard, SnippetCard)
│   │   ├── layouts/             # 布局组件 (Header)
│   │   ├── views/               # 页面视图
│   │   ├── hooks/               # 组合式函数 (useTheme)
│   │   ├── services/            # API 服务层
│   │   ├── utils/               # 工具函数 (storage)
│   │   ├── types/               # 类型定义
│   │   ├── router/              # 路由配置
│   │   ├── styles/              # 全局样式 (main.css, responsive.css)
│   │   ├── App.vue
│   │   └── main.ts
│   ├── public/
│   ├── dist/
│   ├── .env                     # 前端环境配置
│   └── package.json
├── backend-python/               # Python FastAPI 后端服务
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # 应用入口
│   │   ├── schemas.py           # Pydantic 模型
│   │   ├── database.py          # 数据库/内存存储
│   │   └── routers/             # 路由模块
│   │       ├── __init__.py
│   │       ├── posts.py
│   │       └── snippets.py
│   ├── .env                     # Python 环境配置
│   ├── requirements.txt
│   └── Dockerfile
├── backend-java/                 # Java Spring Boot 后端服务
│   ├── src/main/java/
│   ├── src/main/resources/
│   ├── .env                     # Java 环境配置
│   ├── pom.xml
│   └── Dockerfile
├── rust-module/                  # Rust 高性能计算服务
│   ├── src/
│   ├── .env                     # Rust 环境配置
│   ├── Cargo.toml
│   └── Dockerfile
├── upload_frontend.py           # 前端文件上传脚本
├── docker-compose.yml            # Docker 编排配置
├── .env.example                 # 环境变量示例
└── README.md                    # 项目说明文档
```

## 🚀 快速开始

### 环境要求

- **Node.js**: 18+ (当前测试版本: v24.15.0)
- **Python**: 3.11+ (当前测试版本: 3.14.5)
- **Java**: 21+ (当前测试版本: 21.0.11)
- **Rust**: 1.70+ (当前测试版本: 1.95.0)
- **Maven**: 3.9+

### 方式一：使用 Docker Compose (推荐)

```bash
docker-compose up
```

### 方式二：手动启动

#### 1. 启动前端服务

```bash
cd frontend
npm install
npm run dev
```
访问: http://localhost:5173

#### 2. 启动 Python 后端

```bash
cd backend-python
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
API 文档: http://localhost:8000/docs

#### 3. 启动 Java 后端

```bash
cd backend-java
mvn spring-boot:run
```
H2 控制台: http://localhost:8080/h2-console

#### 4. 启动 Rust 计算服务

```bash
cd rust-module
cargo run
```
访问: http://localhost:8081

## 🚀 部署到生产环境

### 前端部署

```bash
cd frontend
npm run build
python upload_frontend.py
```

### 部署说明

- **域名**: ljbljb.com (新项目)
- **旧域名**: ljblib.xyz (现有服务，已隔离)
- **SSL**: 使用 Let's Encrypt 证书
- **Nginx**: 配置虚拟主机实现多域名隔离

## 📡 API 接口文档

### Python FastAPI (端口 8000)

#### 文章管理

| 方法 | 路径 | 描述 |
|------|------|------|
| GET | `/api/posts` | 获取所有文章 |
| GET | `/api/posts/{id}` | 获取单篇文章 |
| POST | `/api/posts` | 创建新文章 |
| PUT | `/api/posts/{id}` | 更新文章 |
| DELETE | `/api/posts/{id}` | 删除文章 |

#### 代码片段

| 方法 | 路径 | 描述 |
|------|------|------|
| GET | `/api/snippets` | 获取所有代码片段 |
| GET | `/api/snippets/{id}` | 获取单个代码片段 |
| POST | `/api/snippets` | 创建新代码片段 |

### Rust 计算服务 (端口 8081)

| 方法 | 路径 | 描述 |
|------|------|------|
| GET | `/` | 健康检查 |
| GET | `/compute/fibonacci/{n}` | 计算斐波那契数 |
| GET | `/compute/factorial/{n}` | 计算阶乘 |
| GET | `/compute/is_prime/{n}` | 检测素数 |

## 📝 使用示例

### 获取所有文章

```bash
curl http://localhost:8000/api/posts
```

### 创建文章

```bash
curl -X POST http://localhost:8000/api/posts \
  -H "Content-Type: application/json" \
  -d '{
    "id": 7,
    "title": "新文章标题",
    "content": "文章内容",
    "author": "作者",
    "createdAt": "2024-01-16",
    "updatedAt": "2024-01-16",
    "tags": ["标签1", "标签2"]
  }'
```

### 计算斐波那契数

```bash
curl http://localhost:8081/compute/fibonacci/40
```

## 🤝 贡献指南

1. Fork 本仓库
2. 创建特性分支: `git checkout -b feature/AmazingFeature`
3. 提交更改: `git commit -m 'Add some AmazingFeature'`
4. 推送到分支: `git push origin feature/AmazingFeature`
5. 开启 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 📧 联系方式

如有问题或建议，请通过以下方式联系：

- 项目地址: [https://github.com/lijinbo-max/devshare](https://github.com/lijinbo-max/devshare)
- 邮箱: 2681244490@qq.com
- 在线演示: https://ljbljb.com

---

**DevShare** - 分享技术，连接开发者 👨‍💻
