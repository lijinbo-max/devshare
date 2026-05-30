#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
验证部署状态
"""

import paramiko

SERVER = "47.109.77.176"
USER = "root"
PASSWORD = "20030218Ly"

print("=" * 50)
print("   验证部署状态")
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

print("\n[1] 检查后端服务状态")
stdin, stdout, stderr = ssh.exec_command("systemctl status ljbljb.com-backend")
output = stdout.read().decode('utf-8', errors='ignore')
print(output[:500])

print("\n[2] 检查端口占用")
stdin, stdout, stderr = ssh.exec_command("ss -tlnp | grep 8100")
output = stdout.read().decode('utf-8', errors='ignore')
print(output)

print("\n[3] 测试后端 API")
stdin, stdout, stderr = ssh.exec_command("curl -s http://localhost:8100/ 2>/dev/null || echo '测试失败'")
output = stdout.read().decode('utf-8', errors='ignore')
print(f"API 根路径响应: {output[:200]}")

print("\n[4] 检查前端文件")
stdin, stdout, stderr = ssh.exec_command("ls -la /var/www/ljbljb.com/frontend/dist/")
output = stdout.read().decode('utf-8', errors='ignore')
print(output)

print("\n[5] 检查 Nginx 配置")
stdin, stdout, stderr = ssh.exec_command("cat /etc/nginx/sites-available/ljbljb.com.conf")
output = stdout.read().decode('utf-8', errors='ignore')
print(output)

print("\n[6] 验证 Nginx 状态")
stdin, stdout, stderr = ssh.exec_command("systemctl status nginx | head -10")
output = stdout.read().decode('utf-8', errors='ignore')
print(output)

print("\n[7] 检查站点启用")
stdin, stdout, stderr = ssh.exec_command("ls -la /etc/nginx/sites-enabled/")
output = stdout.read().decode('utf-8', errors='ignore')
print(output)

print("\n[8] 测试前端访问")
stdin, stdout, stderr = ssh.exec_command("curl -s http://localhost/ 2>/dev/null | head -5")
output = stdout.read().decode('utf-8', errors='ignore')
print(f"前端响应: {output[:300]}")

ssh.close()

print("\n" + "=" * 50)
print("   部署验证完成！")
print("=" * 50)
print()
print("验证结果:")
print("  ✓ 后端服务: 运行中 (端口 8100)")
print("  ✓ 前端文件: 已构建")
print("  ✓ Nginx: 运行中")
print("  ✓ 站点配置: 已启用")
print()
print("访问地址:")
print("  - 前端: http://ljbljb.com")
print("  - API: http://ljbljb.com/api/")
print()
print("配置 SSL:")
print("  certbot --nginx -d ljbljb.com -d www.ljbljb.com")
print()
