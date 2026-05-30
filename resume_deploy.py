#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
继续部署 - 上传更新后的脚本并执行
"""

import paramiko

SERVER = "47.109.77.176"
USER = "root"
PASSWORD = "20030218Ly"
REMOTE_PATH = "/var/www/ljbljb.com"

print("=" * 50)
print("   继续部署")
print("=" * 50)
print(f"服务器: {SERVER}")
print(f"远程路径: {REMOTE_PATH}")
print("=" * 50)
print()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print("[1/3] 连接服务器...")
try:
    ssh.connect(SERVER, username=USER, password=PASSWORD, timeout=30)
    print("✓ 连接成功！")
except Exception as e:
    print(f"✗ 连接失败: {e}")
    exit(1)
print()

print("[2/3] 上传更新后的部署脚本...")
sftp = ssh.open_sftp()
sftp.put("QUICK_DEPLOY.sh", f"{REMOTE_PATH}/QUICK_DEPLOY.sh")
sftp.close()
print("✓ 部署脚本上传完成！")
print()

print("[3/3] 执行部署脚本...")
commands = [
    f"cd {REMOTE_PATH}",
    "chmod +x QUICK_DEPLOY.sh",
    "./QUICK_DEPLOY.sh"
]

full_command = " && ".join(commands)
print(f"执行: {full_command}")
stdin, stdout, stderr = ssh.exec_command(full_command, get_pty=True)

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

ssh.close()

print()
print("=" * 50)
print("   部署完成！")
print("=" * 50)
print()
print("验证地址:")
print(f"  - 现有服务: https://ljblib.xyz")
print(f"  - 新服务: https://ljbljb.com")
print()
