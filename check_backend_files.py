#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查后端目录结构
"""

import paramiko

SERVER = "47.109.77.176"
USER = "root"
PASSWORD = "20030218Ly"

print("=" * 50)
print("   检查后端目录结构")
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

print("\n[1] 查看后端目录")
stdin, stdout, stderr = ssh.exec_command("ls -la /var/www/ljbljb.com/backend-python/")
output = stdout.read().decode('utf-8', errors='ignore')
print(output)

print("\n[2] 查看目录结构")
stdin, stdout, stderr = ssh.exec_command("find /var/www/ljbljb.com/backend-python -type f -name '*.py' | head -20")
output = stdout.read().decode('utf-8', errors='ignore')
print(output)

print("\n[3] 查看 __init__.py")
stdin, stdout, stderr = ssh.exec_command("ls -la /var/www/ljbljb.com/backend-python/__init__.py 2>/dev/null || echo '不存在'")
output = stdout.read().decode('utf-8', errors='ignore')
print(output)

print("\n[4] 查看主文件")
stdin, stdout, stderr = ssh.exec_command("cat /var/www/ljbljb.com/backend-python/main.py 2>/dev/null || cat /var/www/ljbljb.com/backend-python/app.py 2>/dev/null || echo '未找到主文件'")
output = stdout.read().decode('utf-8', errors='ignore')
print(output[:2000])

ssh.close()

print("\n" + "=" * 50)
