# 简单的部署脚本 - 请按顺序执行
$ErrorActionPreference = "Stop"

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "   DevShare 部署工具" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

$server = "47.103.77.176"
$user = "root"
$password = "20030218Ly"
$remotePath = "/var/www/ljbljb.com"

Write-Host "服务器: $server" -ForegroundColor Yellow
Write-Host "用户: $user" -ForegroundColor Yellow
Write-Host "远程路径: $remotePath" -ForegroundColor Yellow
Write-Host ""
Write-Host "重要提示: 每次提示输入密码时请输入: $password" -ForegroundColor Red
Write-Host ""

# 步骤 1: 创建目录
Write-Host "[1/8] 创建服务器目录..." -ForegroundColor Yellow
try {
    ssh ${user}@${server} "mkdir -p ${remotePath}"
    Write-Host "✓ 目录创建成功" -ForegroundColor Green
}
catch {
    Write-Host "✗ 目录创建失败" -ForegroundColor Red
    exit 1
}
Write-Host ""

# 步骤 2: 上传 frontend
Write-Host "[2/8] 上传 frontend..." -ForegroundColor Yellow
scp -r frontend ${user}@${server}:${remotePath}/
Write-Host "✓ frontend 上传成功" -ForegroundColor Green
Write-Host ""

# 步骤 3: 上传 backend-python
Write-Host "[3/8] 上传 backend-python..." -ForegroundColor Yellow
scp -r backend-python ${user}@${server}:${remotePath}/
Write-Host "✓ backend-python 上传成功" -ForegroundColor Green
Write-Host ""

# 步骤 4: 上传 backend-java
Write-Host "[4/8] 上传 backend-java..." -ForegroundColor Yellow
scp -r backend-java ${user}@${server}:${remotePath}/
Write-Host "✓ backend-java 上传成功" -ForegroundColor Green
Write-Host ""

# 步骤 5: 上传 rust-module
Write-Host "[5/8] 上传 rust-module..." -ForegroundColor Yellow
scp -r rust-module ${user}@${server}:${remotePath}/
Write-Host "✓ rust-module 上传成功" -ForegroundColor Green
Write-Host ""

# 步骤 6: 上传部署脚本
Write-Host "[6/8] 上传部署脚本..." -ForegroundColor Yellow
scp QUICK_DEPLOY.sh ${user}@${server}:${remotePath}/
Write-Host "✓ 部署脚本上传成功" -ForegroundColor Green
Write-Host ""

Write-Host "==========================================" -ForegroundColor Green
Write-Host "   文件上传完成！" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green
Write-Host ""
Write-Host "下一步：" -ForegroundColor Cyan
Write-Host "1. 运行以下命令登录服务器:" -ForegroundColor White
Write-Host "   ssh ${user}@${server}" -ForegroundColor Yellow
Write-Host ""
Write-Host "2. 登录后执行:" -ForegroundColor White
Write-Host "   cd ${remotePath}" -ForegroundColor Yellow
Write-Host "   chmod +x QUICK_DEPLOY.sh" -ForegroundColor Yellow
Write-Host "   ./QUICK_DEPLOY.sh" -ForegroundColor Yellow
Write-Host ""
Write-Host "密码: ${password}" -ForegroundColor Red
Write-Host ""
