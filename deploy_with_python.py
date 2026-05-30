#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DevShare 自动化部署脚本
使用 paramiko 库实现完全自动化
"""

import os
import sys
import subprocess
from pathlib import Path

try:
    import paramiko
except ImportError:
    print("正在安装 paramiko 库...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "paramiko"])
    import paramiko

SERVER = "47.109.77.176"
USER = "root"
PASSWORD = "20030218Ly"
REMOTE_PATH = "/var/www/ljbljb.com"
LOCAL_PATH = Path(__file__).parent

def print_banner():
    print("=" * 50)
    print("   DevShare 完全自动化部署工具")
    print("=" * 50)
    print(f"服务器: {SERVER}")
    print(f"用户: {USER}")
    print(f"远程路径: {REMOTE_PATH}")
    print("=" * 50)
    print()

def ssh_exec_command(ssh, command):
    print(f"执行: {command}")
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode('utf-8', errors='ignore')
    error = stderr.read().decode('utf-8', errors='ignore')
    if output:
        print(f"输出: {output.strip()}")
    if error:
        print(f"错误: {error.strip()}")
    return output, error

def sftp_upload_dir(sftp, local_dir, remote_dir):
    local_path = Path(local_dir)
    print(f"上传目录: {local_path.name} -> {remote_dir}")
    
    try:
        sftp.stat(remote_dir)
    except:
        sftp.mkdir(remote_dir)
    
    for item in local_path.iterdir():
        if item.name.startswith('.') or item.name == 'node_modules' or item.name == '__pycache__':
            continue
            
        remote_item = f"{remote_dir}/{item.name}"
        
        if item.is_dir():
            sftp_upload_dir(sftp, str(item), remote_item)
        else:
            print(f"  上传文件: {item.name}")
            sftp.put(str(item), remote_item)

def main():
    print_banner()
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    print("[1/5] 连接服务器...")
    try:
        ssh.connect(SERVER, username=USER, password=PASSWORD, timeout=30)
        print("✓ 连接成功！")
    except Exception as e:
        print(f"✗ 连接失败: {e}")
        return 1
    print()
    
    sftp = ssh.open_sftp()
    
    print("[2/5] 创建远程目录...")
    ssh_exec_command(ssh, f"mkdir -p {REMOTE_PATH}")
    print("✓ 目录创建成功！")
    print()
    
    print("[3/5] 上传项目文件...")
    dirs_to_upload = ["frontend", "backend-python", "backend-java", "rust-module"]
    for dir_name in dirs_to_upload:
        local_dir = LOCAL_PATH / dir_name
        if local_dir.exists():
            print(f"上传 {dir_name}...")
            sftp_upload_dir(sftp, str(local_dir), f"{REMOTE_PATH}/{dir_name}")
            print(f"✓ {dir_name} 上传完成！")
        else:
            print(f"! {dir_name} 不存在，跳过")
    print()
    
    print("[4/5] 上传部署脚本...")
    deploy_script = LOCAL_PATH / "QUICK_DEPLOY.sh"
    if deploy_script.exists():
        sftp.put(str(deploy_script), f"{REMOTE_PATH}/QUICK_DEPLOY.sh")
        print("✓ 部署脚本上传完成！")
    else:
        print("! 部署脚本不存在")
    print()
    
    sftp.close()
    
    print("[5/5] 执行部署脚本...")
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
    print("如果需要配置 SSL，请登录服务器执行:")
    print(f"  certbot --nginx -d ljbljb.com -d www.ljbljb.com")
    print()
    
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n部署已取消")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n部署出错: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
