# 超级简单部署指南

## 只需 3 步！

---

## 第一步：在本地 PowerShell 执行

打开 PowerShell，进入项目目录，复制粘贴：

```powershell
cd "c:\Users\A2681\Desktop\新建文件夹"
scp -r frontend backend-python backend-java rust-module QUICK_DEPLOY.sh root@47.103.77.176:/var/www/ljbljb.com/
```

*(注意：如果提示输入密码，输入你的服务器 root 密码)*

---

## 第二步：SSH 登录服务器

在 PowerShell 继续执行：

```powershell
ssh root@47.103.77.176
```

---

## 第三步：在服务器上执行一键部署

登录成功后，复制粘贴：

```bash
cd /var/www/ljbljb.com
chmod +x QUICK_DEPLOY.sh
./QUICK_DEPLOY.sh
```

---

## 部署完成后

### 配置 SSL 证书

```bash
certbot --nginx -d ljbljb.com -d www.ljbljb.com
```

### 验证

打开浏览器访问：
- https://ljblib.xyz  (确认现有服务正常)
- https://ljbljb.com  (确认新服务正常)

---

## 如果需要回滚

```bash
cd /var/www/ljbljb.com
docker-compose -f docker-compose.ljbljb.yml down
mv /etc/nginx/conf.d/ljbljb.com.conf /etc/nginx/conf.d/ljbljb.com.conf.disabled
nginx -s reload
```

---

## 常用命令

```bash
# 查看日志
cd /var/www/ljbljb.com
docker-compose -f docker-compose.ljbljb.yml logs -f

# 重启服务
docker-compose -f docker-compose.ljbljb.yml restart
```
