# DevShare 项目部署方案 - ljbljb.com

## 概述

本文档详细说明如何将 DevShare 项目部署到新域名 `ljbljb.com`，同时确保不会影响现有域名 `ljblib.xyz` 的服务。

---

## 一、服务器架构与资源隔离

### 1.1 服务器信息
- **服务器 IP**: 47.103.77.176
- **现有域名**: ljblib.xyz (生产环境)
- **新域名**: ljbljb.com (新项目)

### 1.2 目录结构规划

```
/var/www/
├── ljblib.xyz/              # 现有项目 (保持不变)
│   ├── frontend/
│   ├── backend-python/
│   ├── backend-java/
│   └── rust-module/
└── ljbljb.com/              # 新项目
    ├── frontend/
    ├── backend-python/
    ├── backend-java/
    └── rust-module/

/etc/nginx/
├── nginx.conf
└── conf.d/
    ├── ljblib.xyz.conf      # 现有配置 (保持不变)
    └── ljbljb.com.conf      # 新项目配置

/var/lib/docker/volumes/
├── ljblib_xyz_*             # 现有项目数据卷
└── ljbljb_com_*             # 新项目数据卷
```

### 1.3 端口分配策略

| 服务 | ljblib.xyz (现有) | ljbljb.com (新) |
|------|-------------------|-----------------|
| 前端 Nginx | 80/443 | 80/443 (独立 vhost) |
| 前端开发 (可选) | 5173 | 5273 |
| Python 后端 | 8000 | 8100 |
| Java 后端 | 8080 | 8180 |
| Rust 服务 | 8081 | 8181 |

---

## 二、域名解析配置

### 2.1 DNS 记录设置

在域名服务商处添加以下 DNS 记录：

| 类型 | 主机记录 | 记录值 | TTL |
|------|----------|--------|-----|
| A | @ | 47.103.77.176 | 600 |
| A | www | 47.103.77.176 | 600 |

### 2.2 验证 DNS 解析

```bash
# 在本地测试 DNS 解析
nslookup ljbljb.com
ping ljbljb.com
```

---

## 三、服务器环境准备

### 3.1 登录服务器

```bash
ssh root@47.103.77.176
```

### 3.2 检查现有服务状态

```bash
# 检查现有 Nginx 配置
ls -la /etc/nginx/conf.d/
nginx -t

# 检查现有 Docker 容器
docker ps -a

# 检查现有项目目录
ls -la /var/www/
```

### 3.3 创建新项目目录

```bash
# 创建新项目根目录
mkdir -p /var/www/ljbljb.com
chown -R $USER:$USER /var/www/ljbljb.com
chmod -R 755 /var/www/ljbljb.com

# 备份现有配置 (安全措施)
cp -r /etc/nginx /etc/nginx.backup.$(date +%Y%m%d)
```

---

## 四、项目文件上传

### 4.1 方式一：使用 SCP 上传 (推荐)

```bash
# 在本地执行 (Windows PowerShell)
cd "c:\Users\A2681\Desktop\新建文件夹"

# 上传项目文件
scp -r frontend root@47.103.77.176:/var/www/ljbljb.com/
scp -r backend-python root@47.103.77.176:/var/www/ljbljb.com/
scp -r backend-java root@47.103.77.176:/var/www/ljbljb.com/
scp -r rust-module root@47.103.77.176:/var/www/ljbljb.com/
scp docker-compose.yml root@47.103.77.176:/var/www/ljbljb.com/
```

### 4.2 方式二：使用 Git (如果代码已托管)

```bash
# 在服务器上
cd /var/www/ljbljb.com
git clone <your-repo-url> .
```

---

## 五、Docker Compose 配置 (新项目专用)

创建新项目专用的 docker-compose 配置文件：

```bash
# 在服务器上
cd /var/www/ljbljb.com
cp docker-compose.yml docker-compose.ljbljb.yml
```

编辑 `docker-compose.ljbljb.yml`，修改端口配置：

```yaml
version: '3.8'

services:
  frontend:
    build: ./frontend
    ports:
      - "5273:5173"
    volumes:
      - ./frontend:/app
      - /app/node_modules
    environment:
      - VITE_API_URL=http://localhost:8100
      - VITE_JAVA_API_URL=http://localhost:8180
    container_name: devshare_frontend_ljbljb
    restart: unless-stopped

  backend-python:
    build: ./backend-python
    ports:
      - "8100:8000"
    volumes:
      - ./backend-python:/app
      - ljbljb_com_python_data:/app/data
    environment:
      - DATABASE_URL=sqlite:///./data/devshare.db
    container_name: devshare_python_ljbljb
    restart: unless-stopped

  backend-java:
    build: ./backend-java
    ports:
      - "8180:8080"
    volumes:
      - ./backend-java:/app
      - ljbljb_com_java_data:/app/data
    container_name: devshare_java_ljbljb
    restart: unless-stopped

  rust-service:
    build: ./rust-module
    ports:
      - "8181:8081"
    volumes:
      - ./rust-module:/app
    container_name: devshare_rust_ljbljb
    restart: unless-stopped

volumes:
  ljbljb_com_python_data:
    name: ljbljb_com_python_data
  ljbljb_com_java_data:
    name: ljbljb_com_java_data
```

---

## 六、Nginx 虚拟主机配置

### 6.1 创建新项目 Nginx 配置

```bash
# 在服务器上
nano /etc/nginx/conf.d/ljbljb.com.conf
```

添加以下内容：

```nginx
server {
    listen 80;
    listen [::]:80;
    server_name ljbljb.com www.ljbljb.com;

    # 日志文件 (独立)
    access_log /var/log/nginx/ljbljb.com.access.log;
    error_log /var/log/nginx/ljbljb.com.error.log;

    # 前端静态文件
    location / {
        root /var/www/ljbljb.com/frontend/dist;
        index index.html;
        try_files $uri $uri/ /index.html;
    }

    # Python API 反向代理
    location /api/ {
        proxy_pass http://127.0.0.1:8100;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Java API 反向代理
    location /java-api/ {
        proxy_pass http://127.0.0.1:8180;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Rust 计算服务反向代理
    location /rust-api/ {
        proxy_pass http://127.0.0.1:8181;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Gzip 压缩
    gzip on;
    gzip_vary on;
    gzip_min_length 1024;
    gzip_types text/plain text/css text/xml text/javascript application/x-javascript application/xml+rss application/javascript application/json;
}
```

### 6.2 验证 Nginx 配置

```bash
# 测试配置文件语法
nginx -t

# 如果语法正确，重新加载 Nginx
nginx -s reload
```

**重要提示**：执行 `nginx -s reload` 不会中断现有服务，只会平滑加载新配置。

---

## 七、SSL/TLS 证书配置 (Let's Encrypt)

### 7.1 安装 Certbot

```bash
apt update
apt install certbot python3-certbot-nginx -y
```

### 7.2 获取证书

```bash
# 获取证书并自动配置 Nginx
certbot --nginx -d ljbljb.com -d www.ljbljb.com
```

Certbot 会自动修改 `/etc/nginx/conf.d/ljbljb.com.conf`，添加 HTTPS 配置。

### 7.3 验证自动续期

```bash
certbot renew --dry-run
```

---

## 八、数据库隔离策略

### 8.1 SQLite 数据库 (当前使用)

当前项目使用 SQLite，已通过 Docker volumes 实现隔离：

- 现有项目: `/var/lib/docker/volumes/ljblib_xyz_*`
- 新项目: `/var/lib/docker/volumes/ljbljb_com_*`

### 8.2 如果使用 MySQL/PostgreSQL

如需使用独立数据库，创建专用数据库：

```sql
-- 为新项目创建独立数据库
CREATE DATABASE devshare_ljbljb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'devshare_ljbljb'@'localhost' IDENTIFIED BY 'your_secure_password';
GRANT ALL PRIVILEGES ON devshare_ljbljb.* TO 'devshare_ljbljb'@'localhost';
FLUSH PRIVILEGES;
```

---

## 九、构建与部署流程

### 9.1 构建前端

```bash
# 在服务器上
cd /var/www/ljbljb.com/frontend

# 安装依赖
npm install

# 构建生产版本
npm run build

# 验证 dist 目录
ls -la dist/
```

### 9.2 启动 Docker 服务

```bash
cd /var/www/ljbljb.com

# 使用新项目专用配置启动
docker-compose -f docker-compose.ljbljb.yml up -d

# 查看容器状态
docker-compose -f docker-compose.ljbljb.yml ps

# 查看日志
docker-compose -f docker-compose.ljbljb.yml logs -f
```

### 9.3 验证服务端口

```bash
# 检查端口是否监听
netstat -tlnp | grep -E '5273|8100|8180|8181'

# 或使用 ss
ss -tlnp | grep -E '5273|8100|8180|8181'
```

---

## 十、测试验证流程

### 10.1 首先验证现有服务 (重要！)

在部署新项目前，**必须**确认现有服务正常：

```bash
# 测试现有域名
curl -I https://ljblib.xyz

# 浏览器访问确认
# 打开: https://ljblib.xyz
```

### 10.2 验证新项目服务

#### 10.2.1 本地端口测试

```bash
# 测试 Python 后端
curl http://127.0.0.1:8100/docs

# 测试 Java 后端
curl http://127.0.0.1:8180/actuator/health

# 测试 Rust 服务
curl http://127.0.0.1:8181/
```

#### 10.2.2 域名访问测试

```bash
# 测试 HTTP
curl -I http://ljbljb.com

# 测试 HTTPS
curl -I https://ljbljb.com

# 测试 API 端点
curl https://ljbljb.com/api/posts
curl https://ljbljb.com/rust-api/
```

#### 10.2.3 浏览器测试

访问以下 URL 进行验证：

| 测试项 | URL | 预期结果 |
|--------|-----|----------|
| 首页 | https://ljbljb.com | 正常显示 DevShare 首页 |
| Python API 文档 | https://ljbljb.com/api/docs | Swagger UI 正常 |
| 静态资源 | https://ljbljb.com/assets/index-*.css | CSS 正常加载 |

### 10.3 并行验证 (两个域名同时)

打开两个浏览器窗口：
- 窗口1: https://ljblib.xyz (确认现有服务正常)
- 窗口2: https://ljbljb.com (确认新服务正常)

---

## 十一、防火墙配置

```bash
# 确保防火墙允许 HTTP/HTTPS
ufw allow 80/tcp
ufw allow 443/tcp

# 如果需要限制新服务端口仅本地访问 (推荐)
ufw deny in 8100/tcp
ufw deny in 8180/tcp
ufw deny in 8181/tcp
ufw deny in 5273/tcp

ufw reload
```

---

## 十二、监控与日志

### 12.1 日志位置

| 日志类型 | 路径 |
|----------|------|
| Nginx 访问日志 | `/var/log/nginx/ljbljb.com.access.log` |
| Nginx 错误日志 | `/var/log/nginx/ljbljb.com.error.log` |
| Python 后端日志 | `docker logs devshare_python_ljbljb` |
| Java 后端日志 | `docker logs devshare_java_ljbljb` |
| Rust 服务日志 | `docker logs devshare_rust_ljbljb` |

### 12.2 查看实时日志

```bash
# 查看所有服务日志
cd /var/www/ljbljb.com
docker-compose -f docker-compose.ljbljb.yml logs -f

# 查看特定服务日志
docker logs -f devshare_frontend_ljbljb
```

---

## 十三、回滚方案

如果部署出现问题，按以下步骤回滚：

### 13.1 快速回滚

```bash
# 1. 停止新项目容器
cd /var/www/ljbljb.com
docker-compose -f docker-compose.ljbljb.yml down

# 2. 禁用新项目 Nginx 配置
mv /etc/nginx/conf.d/ljbljb.com.conf /etc/nginx/conf.d/ljbljb.com.conf.disabled

# 3. 重新加载 Nginx
nginx -t && nginx -s reload

# 4. 验证现有服务
curl https://ljblib.xyz
```

### 13.2 完整回滚 (如需)

```bash
# 恢复 Nginx 备份
cp -r /etc/nginx.backup.$(date +%Y%m%d)/* /etc/nginx/
nginx -t && nginx -s reload
```

---

## 十四、维护与更新

### 14.1 更新新项目

```bash
cd /var/www/ljbljb.com

# 拉取最新代码
git pull origin main

# 重新构建前端
cd frontend
npm install
npm run build
cd ..

# 重启服务
docker-compose -f docker-compose.ljbljb.yml up -d --build
```

### 14.2 安全注意事项

- 两个项目的 `.env` 文件必须独立配置，使用不同的密钥
- 定期更新 Docker 镜像和系统包
- 监控资源使用，防止新项目影响现有服务

---

## 十五、检查清单

部署前检查：
- [ ] 备份现有 Nginx 配置
- [ ] 确认现有服务运行正常
- [ ] DNS 解析已生效
- [ ] 服务器有足够磁盘空间

部署中检查：
- [ ] 项目文件已上传到正确目录
- [ ] 端口配置无冲突
- [ ] Nginx 配置语法正确
- [ ] `nginx -s reload` 执行成功

部署后检查：
- [ ] 新域名可访问
- [ ] 所有 API 端点正常
- [ ] 现有域名 ljblib.xyz 依然正常
- [ ] SSL 证书生效
- [ ] 日志无错误

---

## 附录 A：快速部署脚本

创建一键部署脚本 `deploy-ljbljb.sh`：

```bash
#!/bin/bash
set -e

echo "=== DevShare 部署脚本 - ljbljb.com ==="

# 1. 检查现有服务
echo "[1/7] 检查现有服务状态..."
curl -s -o /dev/null -w "%{http_code}" https://ljblib.xyz || { echo "警告: 现有服务可能有问题"; }

# 2. 备份配置
echo "[2/7] 备份 Nginx 配置..."
cp -r /etc/nginx /etc/nginx.backup.$(date +%Y%m%d)

# 3. 构建前端
echo "[3/7] 构建前端..."
cd /var/www/ljbljb.com/frontend
npm install
npm run build

# 4. 启动 Docker 服务
echo "[4/7] 启动 Docker 服务..."
cd /var/www/ljbljb.com
docker-compose -f docker-compose.ljbljb.yml up -d

# 5. 等待服务启动
echo "[5/7] 等待服务启动..."
sleep 10

# 6. 验证 Nginx 配置
echo "[6/7] 验证 Nginx 配置..."
nginx -t
nginx -s reload

# 7. 验证部署
echo "[7/7] 验证部署..."
echo "测试 ljblib.xyz (现有):"
curl -s -o /dev/null -w "  HTTP: %{http_code}\n" https://ljblib.xyz
echo "测试 ljbljb.com (新):"
curl -s -o /dev/null -w "  HTTP: %{http_code}\n" https://ljbljb.com

echo "=== 部署完成 ==="
```

使用方法：
```bash
chmod +x deploy-ljbljb.sh
./deploy-ljbljb.sh
```

---

## 联系与支持

如有问题，请检查：
1. Nginx 错误日志: `/var/log/nginx/ljbljb.com.error.log`
2. Docker 容器日志: `docker logs <container_name>`
3. 确保端口无冲突: `netstat -tlnp`

---

**文档版本**: 1.0  
**最后更新**: 2026-05-29
