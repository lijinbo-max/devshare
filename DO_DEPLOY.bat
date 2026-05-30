@echo off
chcp 65001 >nul
title DevShare 部署 - ljbljb.com
color 0A

echo ==========================================
echo    DevShare 一键部署工具
echo ==========================================
echo.
echo 服务器: 47.103.77.176
echo 用户: root
echo 密码: 20030218Ly
echo.
echo ==========================================
echo.
echo [提示] 每次提示输入密码时请输入: 20030218Ly
echo.
pause

cd /d "%~dp0"

echo.
echo [1/7] 正在创建服务器目录...
ssh root@47.103.77.176 "mkdir -p /var/www/ljbljb.com"
if errorlevel 1 (
    echo.
    echo [错误] 创建目录失败！
    pause
    exit /b 1
)
echo [成功] 目录创建完成！
echo.

echo [2/7] 正在上传 frontend...
scp -r frontend root@47.103.77.176:/var/www/ljbljb.com/
if errorlevel 1 (
    echo.
    echo [错误] 上传 frontend 失败！
    pause
    exit /b 1
)
echo [成功] frontend 上传完成！
echo.

echo [3/7] 正在上传 backend-python...
scp -r backend-python root@47.103.77.176:/var/www/ljbljb.com/
if errorlevel 1 (
    echo.
    echo [错误] 上传 backend-python 失败！
    pause
    exit /b 1
)
echo [成功] backend-python 上传完成！
echo.

echo [4/7] 正在上传 backend-java...
scp -r backend-java root@47.103.77.176:/var/www/ljbljb.com/
if errorlevel 1 (
    echo.
    echo [错误] 上传 backend-java 失败！
    pause
    exit /b 1
)
echo [成功] backend-java 上传完成！
echo.

echo [5/7] 正在上传 rust-module...
scp -r rust-module root@47.103.77.176:/var/www/ljbljb.com/
if errorlevel 1 (
    echo.
    echo [错误] 上传 rust-module 失败！
    pause
    exit /b 1
)
echo [成功] rust-module 上传完成！
echo.

echo [6/7] 正在上传部署脚本...
scp QUICK_DEPLOY.sh root@47.103.77.176:/var/www/ljbljb.com/
if errorlevel 1 (
    echo.
    echo [错误] 上传部署脚本失败！
    pause
    exit /b 1
)
echo [成功] 部署脚本上传完成！
echo.

echo ==========================================
echo    文件上传全部完成！
echo ==========================================
echo.
echo 下一步：将自动打开 SSH 连接...
echo.
echo 登录后请按顺序执行以下命令：
echo   1. cd /var/www/ljbljb.com
echo   2. chmod +x QUICK_DEPLOY.sh
echo   3. ./QUICK_DEPLOY.sh
echo.
echo 密码: 20030218Ly
echo.
pause

echo.
echo [7/7] 正在打开 SSH 连接...
echo.
ssh root@47.103.77.176

echo.
echo 部署会话已结束。
echo.
pause
