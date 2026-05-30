#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查后端服务状态
"""

import paramiko

SERVER = "47.109.77.176"
USER = "root"
PASSWORD = "20030218Ly"

print("=" * 50)
print("   检查后端服务状态")
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

print("\n[1] 检查服务状态")
stdin, stdout, stderr = ssh.exec_command("systemctl status ljbljb.com-backend")
output = stdout.read().decode('utf-8', errors='ignore')
print(output)

print("\n[2] 查看最近日志")
stdin, stdout, stderr = ssh.exec_command("journalctl -u ljbljb.com-backend --no-pager -n 30")
output = stdout.read().decode('utf-8', errors='ignore')
print(output)

print("\n[3] 检查端口占用")
stdin, stdout, stderr = ssh.exec_command("netstat -tlnp | grep 8100 || ss -tlnp | grep 8100")
output = stdout.read().decode('utf-8', errors='ignore')
print(output)

print("\n[4] 手动启动测试")
stdin, stdout, stderr = ssh.exec_command("cd /var/www/ljbljb.com/backend-python && python3 -m uvicorn main:app --host 0.0.0.0 --port 8100 2>&1 | head -30")
output = stdout.read().decode('utf-8', errors='ignore')
print(output)

ssh.close()

print("\n" + "=" * 50)
