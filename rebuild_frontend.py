#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
重新构建前端并部署
"""

import paramiko
import subprocess

SERVER = "47.109.77.176"
USER = "root"
PASSWORD = "20030218Ly"
REMOTE_PATH = "/var/www/ljbljb.com"

print("=" * 50)
print("   重新构建前端")
print("=" * 50)
print()

print("[1/3] 构建前端...")
result = subprocess.run(
    ["npm", "run", "build"],
    cwd="frontend",
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print("✓ 前端构建成功")
else:
    print("✗ 前端构建失败")
    print(result.stderr)
    exit(1)

print("\n[2/3] 连接服务器...")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(SERVER, username=USER, password=PASSWORD, timeout=30)
    print("✓ 连接成功！")
except Exception as e:
    print(f"✗ 连接失败: {e}")
    exit(1)

print("\n[3/3] 上传前端文件...")
sftp = ssh.open_sftp()

local_dist = "frontend/dist"
remote_dist = f"{REMOTE_PATH}/frontend/dist"

def upload_dir(local_dir, remote_dir):
    import os
    for item in os.listdir(local_dir):
        local_item = os.path.join(local_dir, item)
        remote_item = f"{remote_dir}/{item}"
        
        if os.path.isdir(local_item):
            try:
                sftp.mkdir(remote_item)
            except:
                pass
            upload_dir(local_item, remote_item)
        else:
            print(f"  上传: {item}")
            sftp.put(local_item, remote_item)

upload_dir(local_dist, remote_dist)

sftp.close()
ssh.close()

print("\n✓ 前端文件上传完成！")
print()
print("=" * 50)
print("   部署完成！")
print("=" * 50)
print()
print("访问地址: https://ljbljb.com")
print()
