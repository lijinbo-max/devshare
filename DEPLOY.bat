@echo off
chcp 65001 >nul
echo ==========================================
echo    DevShare 一键部署 - ljbljb.com
echo ==========================================
echo.

cd /d "%~dp0"

echo [1/4] 正在创建服务器目录...
ssh root@47.103.77.176 "mkdir -p /var/www/ljbljb.com"
if %errorlevel% neq 0 (
    echo.
    echo ❌ 错误：无法连接到服务器或创建目录
    pause
    exit /b 1
)
echo ✓ 目录创建成功
echo.

echo [2/4] 正在上传项目文件...
echo.
echo 正在上传 frontend...
scp -r frontend root@47.103.77.176:/var/www/ljbljb.com/
if %errorlevel% neq 0 (
    echo.
    echo ❌ 错误：上传 frontend 失败
    pause
    exit /b 1
)
echo ✓ frontend 上传成功
echo.

echo 正在上传 backend-python...
scp -r backend-python root@47.103.77.176:/var/www/ljbljb.com/
if %errorlevel% neq 0 (
    echo.
    echo ❌ 错误：上传 backend-python 失败
    pause
    exit /b 1
)
echo ✓ backend-python 上传成功
echo.

echo 正在上传 backend-java...
scp -r backend-java root@47.103.77.176:/var/www/ljbljb.com/
if %errorlevel% neq 0 (
    echo.
    echo ❌ 错误：上传 backend-java 失败
    pause
    exit /b 1
)
echo ✓ backend-java 上传成功
echo.

echo 正在上传 rust-module...
scp -r rust-module root@47.103.77.176:/var/www/ljbljb.com/
if %errorlevel% neq 0 (
    echo.
    echo ❌ 错误：上传 rust-module 失败
    pause
    exit /b 1
)
echo ✓ rust-module 上传成功
echo.

echo 正在上传部署脚本...
scp QUICK_DEPLOY.sh root@47.103.77.176:/var/www/ljbljb.com/
if %errorlevel% neq 0 (
    echo.
    echo ❌ 错误：上传部署脚本失败
    pause
    exit /b 1
)
echo ✓ 部署脚本上传成功
echo.

echo [3/4] 文件上传完成！
echo.
echo ==========================================
echo.
echo 下一步：请 SSH 登录服务器并执行部署
echo.
echo SSH 命令：ssh root@47.103.77.176
echo.
echo 登录后执行：
echo   cd /var/www/ljbljb.com
echo   chmod +x QUICK_DEPLOY.sh
echo   ./QUICK_DEPLOY.sh
echo.
echo ==========================================
echo.
echo 按任意键打开 SSH 会话...
pause >nul

echo.
echo [4/4] 正在打开 SSH 会话...
echo.
ssh root@47.103.77.176

echo.
echo 部署会话已结束
pause
