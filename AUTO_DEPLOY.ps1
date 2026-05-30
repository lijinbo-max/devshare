# DevShare 自动化部署脚本
param(
    [string]$Server = "47.103.77.176",
    [string]$User = "root",
    [string]$Password = "20030218Ly",
    [string]$RemotePath = "/var/www/ljbljb.com"
)

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "   DevShare 自动化部署 - ljbljb.com" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

# 设置工作目录
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptPath

# 函数：使用 plink 或 ssh 执行命令
function Invoke-SSHCommand {
    param([string]$Command)
    
    # 尝试使用 plink (PuTTY)
    $plinkPath = Get-Command plink -ErrorAction SilentlyContinue
    if ($plinkPath) {
        Write-Host "使用 plink 执行: $Command" -ForegroundColor Gray
        echo $Password | & plink -ssh -pw $Password ${User}@${Server} $Command
    }
    else {
        # 尝试使用 sshpass 或其他方式
        Write-Host "使用 ssh 执行: $Command" -ForegroundColor Gray
        echo $Password | & ssh ${User}@${Server} $Command
    }
}

# 函数：使用 pscp 或 scp 上传文件
function Invoke-SCPUpload {
    param([string]$Source, [string]$Destination)
    
    $pscpPath = Get-Command pscp -ErrorAction SilentlyContinue
    if ($pscpPath) {
        Write-Host "使用 pscp 上传: $Source -> $Destination" -ForegroundColor Gray
        echo $Password | & pscp -pw $Password -r $Source ${User}@${Server}:$Destination
    }
    else {
        Write-Host "使用 scp 上传: $Source -> $Destination" -ForegroundColor Gray
        echo $Password | & scp -r $Source ${User}@${Server}:$Destination
    }
}

Write-Host "[1/6] 创建服务器目录..." -ForegroundColor Yellow
try {
    Invoke-SSHCommand "mkdir -p $RemotePath"
    Write-Host "✓ 目录创建成功" -ForegroundColor Green
}
catch {
    Write-Host "✗ 目录创建失败: $_" -ForegroundColor Red
    exit 1
}
Write-Host ""

Write-Host "[2/6] 上传项目文件..." -ForegroundColor Yellow
Write-Host "正在上传 frontend..." -ForegroundColor Gray
Invoke-SCPUpload "frontend" "$RemotePath/"
Write-Host "✓ frontend 上传成功" -ForegroundColor Green
Write-Host ""

Write-Host "正在上传 backend-python..." -ForegroundColor Gray
Invoke-SCPUpload "backend-python" "$RemotePath/"
Write-Host "✓ backend-python 上传成功" -ForegroundColor Green
Write-Host ""

Write-Host "正在上传 backend-java..." -ForegroundColor Gray
Invoke-SCPUpload "backend-java" "$RemotePath/"
Write-Host "✓ backend-java 上传成功" -ForegroundColor Green
Write-Host ""

Write-Host "正在上传 rust-module..." -ForegroundColor Gray
Invoke-SCPUpload "rust-module" "$RemotePath/"
Write-Host "✓ rust-module 上传成功" -ForegroundColor Green
Write-Host ""

Write-Host "正在上传部署脚本..." -ForegroundColor Gray
Invoke-SCPUpload "QUICK_DEPLOY.sh" "$RemotePath/"
Write-Host "✓ 部署脚本上传成功" -ForegroundColor Green
Write-Host ""

Write-Host "[3/6] 文件上传完成！" -ForegroundColor Green
Write-Host ""
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "下一步：请 SSH 登录服务器并执行部署" -ForegroundColor Cyan
Write-Host ""
Write-Host "SSH 命令：ssh ${User}@${Server}" -ForegroundColor White
Write-Host ""
Write-Host "登录后执行：" -ForegroundColor White
Write-Host "  cd $RemotePath" -ForegroundColor White
Write-Host "  chmod +x QUICK_DEPLOY.sh" -ForegroundColor White
Write-Host "  ./QUICK_DEPLOY.sh" -ForegroundColor White
Write-Host ""
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "现在正在打开 SSH 会话..." -ForegroundColor Yellow
Write-Host ""

# 打开 SSH 会话
try {
    echo $Password | & ssh ${User}@${Server}
}
catch {
    Write-Host "请手动执行: ssh ${User}@${Server}" -ForegroundColor Yellow
}
