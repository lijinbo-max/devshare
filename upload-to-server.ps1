# DevShare 项目上传脚本 - ljbljb.com
# 用于将项目文件上传到服务器

param(
    [string]$Server = "47.103.77.176",
    [string]$User = "root",
    [string]$RemotePath = "/var/www/ljbljb.com"
)

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "  DevShare 项目上传脚本" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "服务器: $Server" -ForegroundColor Yellow
Write-Host "用户: $User" -ForegroundColor Yellow
Write-Host "目标路径: $RemotePath" -ForegroundColor Yellow
Write-Host ""

# 确认
$confirm = Read-Host "继续上传? (Y/N)"
if ($confirm -notmatch "^[Yy]") {
    Write-Host "已取消" -ForegroundColor Red
    exit 0
}

# 获取当前脚本所在目录
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptPath

Write-Host ""
Write-Host "[1/6] 创建远程目录..." -ForegroundColor Yellow
ssh "$User@$Server" "mkdir -p $RemotePath"

Write-Host ""
Write-Host "[2/6] 上传 frontend..." -ForegroundColor Yellow
scp -r frontend "$User@${Server}:${RemotePath}/"

Write-Host ""
Write-Host "[3/6] 上传 backend-python..." -ForegroundColor Yellow
scp -r backend-python "$User@${Server}:${RemotePath}/"

Write-Host ""
Write-Host "[4/6] 上传 backend-java..." -ForegroundColor Yellow
scp -r backend-java "$User@${Server}:${RemotePath}/"

Write-Host ""
Write-Host "[5/6] 上传 rust-module..." -ForegroundColor Yellow
scp -r rust-module "$User@${Server}:${RemotePath}/"

Write-Host ""
Write-Host "[6/6] 上传配置文件..." -ForegroundColor Yellow
scp docker-compose.ljbljb.yml "$User@${Server}:${RemotePath}/"
scp nginx.ljbljb.com.conf "$User@${Server}:${RemotePath}/"
scp deploy-ljbljb.sh "$User@${Server}:${RemotePath}/"
scp rollback-ljbljb.sh "$User@${Server}:${RemotePath}/"

# 设置执行权限
Write-Host ""
Write-Host "设置脚本执行权限..." -ForegroundColor Yellow
ssh "$User@$Server" "chmod +x ${RemotePath}/deploy-ljbljb.sh ${RemotePath}/rollback-ljbljb.sh"

Write-Host ""
Write-Host "==========================================" -ForegroundColor Green
Write-Host "  上传完成！" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green
Write-Host ""
Write-Host "下一步操作：" -ForegroundColor Cyan
Write-Host "  1. SSH 登录服务器: ssh $User@$Server" -ForegroundColor White
Write-Host "  2. 进入目录: cd $RemotePath" -ForegroundColor White
Write-Host "  3. 执行部署: ./deploy-ljbljb.sh" -ForegroundColor White
Write-Host ""
