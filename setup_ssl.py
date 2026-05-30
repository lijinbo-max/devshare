#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置 SSL 证书
"""

import paramiko

SERVER = "47.109.77.176"
USER = "root"
PASSWORD = "20030218Ly"

print("=" * 50)
print("   配置 SSL 证书")
print("=" * 50)
print(f"服务器: {SERVER}")
print("=" * 50)
print()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(SERVER, username=USER, password=PASSWORD, timeout=30)
    print("✓ 连接成功！")
except Exception as e:
    print(f"✗ 连接失败: {e}")
    exit(1)

print("\n[1] 检查 certbot 是否已安装")
stdin, stdout, stderr = ssh.exec_command("which certbot 2>/dev/null || echo '未安装'")
output = stdout.read().decode('utf-8', errors='ignore').strip()
if output == '未安装':
    print("  安装 certbot...")
    stdin, stdout, stderr = ssh.exec_command("apt-get update && apt-get install -y certbot python3-certbot-nginx")
    output = stdout.read().decode('utf-8', errors='ignore')
    print("✓ certbot 安装完成")
else:
    print(f"✓ certbot 已安装: {output}")

print("\n[2] 配置 SSL 证书")
print("  执行 certbot...")
stdin, stdout, stderr = ssh.exec_command("certbot --nginx -d ljbljb.com -d www.ljbljb.com --non-interactive --agree-tos -m admin@ljbljb.com", get_pty=True)

print("-" * 50)
while True:
    line = stdout.readline()
    if not line:
        break
    print(line, end='')
print("-" * 50)

error = stderr.read().decode('utf-8', errors='ignore')
if error:
    print(f"错误: {error}")

print("\n[3] 验证 SSL 配置")
stdin, stdout, stderr = ssh.exec_command("curl -s -I https://ljbljb.com 2>/dev/null | head -5")
output = stdout.read().decode('utf-8', errors='ignore')
print(output)

print("\n[4] 检查 Nginx 配置")
stdin, stdout, stderr = ssh.exec_command("cat /etc/nginx/sites-available/ljbljb.com.conf | head -50")
output = stdout.read().decode('utf-8', errors='ignore')
print(output)

ssh.close()

print("\n" + "=" * 50)
print("   SSL 配置完成！")
print("=" * 50)
print()
print("访问地址:")
print("  - 前端: https://ljbljb.com")
print("  - API: https://ljbljb.com/api/")
print()
