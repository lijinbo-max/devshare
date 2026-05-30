#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查服务器环境
"""

import paramiko

SERVER = "47.109.77.176"
USER = "root"
PASSWORD = "20030218Ly"

print("=" * 50)
print("   检查服务器环境")
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

commands = [
    ("检查 Python", "python3 --version 2>/dev/null || python --version 2>/dev/null || echo 'Python 未安装'"),
    ("检查 Node.js", "node --version 2>/dev/null || echo 'Node.js 未安装'"),
    ("检查 Java", "java --version 2>/dev/null || echo 'Java 未安装'"),
    ("检查 Rust", "rustc --version 2>/dev/null || echo 'Rust 未安装'"),
    ("检查 Nginx", "nginx -v 2>/dev/null || echo 'Nginx 未安装'"),
    ("检查 Docker", "docker --version 2>/dev/null || echo 'Docker 未安装'"),
    ("检查端口占用", "netstat -tlnp 2>/dev/null | head -20"),
    ("检查站点目录", "ls -la /var/www/"),
    ("检查 Nginx 配置", "ls -la /etc/nginx/sites-available/ 2>/dev/null || ls -la /etc/nginx/conf.d/ 2>/dev/null"),
]

for name, cmd in commands:
    print(f"\n[{name}]")
    stdin, stdout, stderr = ssh.exec_command(cmd)
    output = stdout.read().decode('utf-8', errors='ignore').strip()
    error = stderr.read().decode('utf-8', errors='ignore').strip()
    
    if output:
        print(output)
    if error:
        print(f"错误: {error}")

ssh.close()

print("\n" + "=" * 50)
