# DevShare 部署到 ljbljb.com - 快速开始

## 📋 资源隔离概览

| 项目 | 域名 | 端口范围 | 目录 | 数据卷 |
|------|------|----------|------|--------|
| 现有项目 | ljblib.xyz | 5173, 8000, 8080, 8081 | /var/www/ljblib.xyz/ | ljblib_xyz_* |
| 新项目 | ljbljb.com | 5273, 8100, 8180, 8181 | /var/www/ljbljb.com/ | ljbljb_com_* |

## 🚀 快速部署步骤

### 第一步：DNS 解析
在域名服务商处添加 A 记录：
- `ljbljb.com` → `47.103.77.176`
- `www.ljbljb.com` → `47.103.77.176`

### 第二步：上传文件 (Windows)
在 PowerShell 中执行：
```powershell
cd "c:\Users\A2681\Desktop\新建文件夹"
.\upload-to-server.ps1
```

### 第三步：服务器上部署
SSH 登录服务器后执行：
```bash
ssh root@47.103.77.176
cd /var/www/ljbljb.com
./deploy-ljbljb.sh
```

### 第四步：配置 SSL 证书
```bash
certbot --nginx -d ljbljb.com -d www.ljbljb.com
```

### 第五步：验证
打开两个浏览器窗口：
1. https://ljblib.xyz (确认现有服务正常)
2. https://ljbljb.com (确认新服务正常)

## 📁 文件说明

| 文件名 | 用途 |
|--------|------|
| `DEPLOYMENT_GUIDE.md` | 完整部署文档 |
| `docker-compose.ljbljb.yml` | 新项目 Docker 配置 |
| `nginx.ljbljb.com.conf` | 新项目 Nginx 配置 |
| `deploy-ljbljb.sh` | 一键部署脚本 |
| `rollback-ljbljb.sh` | 快速回滚脚本 |
| `upload-to-server.ps1` | Windows 上传脚本 |

## ⚠️ 重要安全措施

1. **部署前备份**：脚本会自动备份 `/etc/nginx` 目录
2. **先验证现有服务**：脚本先检查 ljblib.xyz 是否正常
3. **隔离配置**：两个项目使用独立的端口、目录、数据卷
4. **快速回滚**：`./rollback-ljbljb.sh` 可随时回滚

## 🔧 常用命令

### 查看新项目日志
```bash
cd /var/www/ljbljb.com
docker-compose -f docker-compose.ljbljb.yml logs -f
```

### 重启新项目服务
```bash
cd /var/www/ljbljb.com
docker-compose -f docker-compose.ljbljb.yml restart
```

### 查看 Nginx 错误日志
```bash
tail -f /var/log/nginx/ljbljb.com.error.log
```

## 🚨 紧急回滚

如果出现问题，立即执行：
```bash
cd /var/www/ljbljb.com
./rollback-ljbljb.sh
```

这将：
1. 停止新项目容器
2. 禁用新项目 Nginx 配置
3. 重新加载 Nginx
4. 验证现有服务

## 📊 端口映射

| 容器内端口 | 新项目 (ljbljb.com) | 说明 |
|------------|---------------------|------|
| 5173 | 5273 | 前端开发服务器 |
| 8000 | 8100 | Python FastAPI |
| 8080 | 8180 | Java Spring Boot |
| 8081 | 8181 | Rust Axum |

**注意**：这些内部端口不对外暴露，通过 Nginx 反向代理访问。

## 📝 详细文档

参阅 `DEPLOYMENT_GUIDE.md` 获取完整的部署说明、故障排查和高级配置。
