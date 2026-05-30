#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
尝试不同的密码方式
"""
import paramiko
import sys

SERVER = "47.103.77.176"
USER = "root"
PASSWORD = "20030218Ly"

print("尝试连接服务器...")
print(f"服务器: {SERVER}")
print(f"用户: {USER}")
print(f"密码长度: {len(PASSWORD)}")
print()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    print("尝试方式 1: 普通密码...")
    ssh.connect(SERVER, username=USER, password=PASSWORD, timeout=10, auth_timeout=10)
    print("✓ 成功！")
    
    stdin, stdout, stderr = ssh.exec_command("whoami && pwd")
    print("输出:", stdout.read().decode())
    
    ssh.close()
    print()
    print("连接成功！现在可以继续部署！")
    
except Exception as e:
    print(f"✗ 失败: {e}")
    print()
    print("请尝试使用 DO_DEPLOY.bat 手动输入密码，或者检查密码是否正确")
    print()
    print("密码应该是: 20030218Ly")
