#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复后端服务配置 - 版本2
"""

import paramiko

SERVER = "47.109.77.176"
USER = "root"
PASSWORD = "20030218Ly"
REMOTE_PATH = "/var/www/ljbljb.com"

print("=" * 50)
print("   修复后端服务配置")
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

print("\n[1] 创建 __init__.py")
stdin, stdout, stderr = ssh.exec_command("touch /var/www/ljbljb.com/backend-python/__init__.py")
stdout.read()
print("✓ __init__.py 创建成功")

print("\n[2] 更新 systemd 服务配置")
service_config = f"""[Unit]
Description=DevShare Backend API
After=network.target

[Service]
User=root
WorkingDirectory={REMOTE_PATH}/backend-python
ExecStart=/usr/bin/python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8100
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
"""

cmd = f"cat > /etc/systemd/system/ljbljb.com-backend.service << 'ENDOFCONFIG'\n{service_config}ENDOFCONFIG"
stdin, stdout, stderr = ssh.exec_command(cmd)
stdout.read()
print("✓ 服务配置已更新")

print("\n[3] 重新加载 systemd")
stdin, stdout, stderr = ssh.exec_command("systemctl daemon-reload")
stdout.read()
print("✓ systemd 已重新加载")

print("\n[4] 重启后端服务")
stdin, stdout, stderr = ssh.exec_command("systemctl restart ljbljb.com-backend")
stdout.read()
print("✓ 服务已重启")

print("\n[5] 等待服务启动...")
import time
time.sleep(5)

print("\n[6] 检查服务状态")
stdin, stdout, stderr = ssh.exec_command("systemctl status ljbljb.com-backend")
output = stdout.read().decode('utf-8', errors='ignore')
print(output)

print("\n[7] 测试 API")
stdin, stdout, stderr = ssh.exec_command("curl -s http://localhost:8100/health 2>/dev/null || echo 'API 测试失败'")
output = stdout.read().decode('utf-8', errors='ignore')
print(f"API 响应: {output}")

ssh.close()

print("\n" + "=" * 50)
