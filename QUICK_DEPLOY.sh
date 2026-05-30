#!/bin/bash
set -e

DOMAIN="ljbljb.com"
REMOTE_PATH="/var/www/ljbljb.com"
BACKUP_DIR="/var/backup/ljbljb.com"

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}! $1${NC}"
}

echo "=========================================="
echo "  DevShare 一键部署"
echo "=========================================="
echo ""

echo "[1/8] 检查现有服务..."
if curl -s -o /dev/null -w "%{http_code}" http://ljblib.xyz > /dev/null 2>&1; then
    print_success "ljblib.xyz 正常"
else
    print_warning "ljblib.xyz 暂时不可达"
fi
echo ""

echo "[2/8] 备份 Nginx 配置..."
mkdir -p "$BACKUP_DIR"
cp /etc/nginx/sites-available/* "$BACKUP_DIR/" 2>/dev/null || true
print_success "已备份"
echo ""

echo "[3/8] 安装必要依赖..."
echo "  检查 Python..."
if ! command -v python3 &> /dev/null; then
    echo "  安装 Python..."
    apt-get update && apt-get install -y python3 python3-pip
fi
print_success "Python 已就绪"

echo "  检查 Node.js..."
if ! command -v node &> /dev/null; then
    echo "  安装 Node.js..."
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
    apt-get install -y nodejs
fi
print_success "Node.js 已就绪"

echo "  安装 Python 依赖..."
cd "$REMOTE_PATH/backend-python"
pip3 install -r requirements.txt --quiet
print_success "Python 依赖安装完成"

echo "  构建前端..."
cd "$REMOTE_PATH/frontend"
npm install --quiet
npm run build --quiet
print_success "前端构建完成"
echo ""

echo "[4/8] 配置 Nginx..."
cat > /etc/nginx/sites-available/"$DOMAIN".conf <<EOF
server {
    listen 80;
    server_name $DOMAIN www.$DOMAIN;
    
    root $REMOTE_PATH/frontend/dist;
    index index.html;
    
    access_log /var/log/nginx/$DOMAIN-access.log;
    error_log /var/log/nginx/$DOMAIN-error.log;
    
    location / {
        try_files \$uri \$uri/ /index.html;
    }
    
    location /api/ {
        proxy_pass http://localhost:8100/;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF

if [ ! -f /etc/nginx/sites-enabled/"$DOMAIN".conf ]; then
    ln -sf /etc/nginx/sites-available/"$DOMAIN".conf /etc/nginx/sites-enabled/"$DOMAIN".conf
fi

nginx -t && systemctl reload nginx
print_success "Nginx 配置已写入"
echo ""

echo "[5/8] 创建 systemd 服务..."
cat > /etc/systemd/system/"$DOMAIN"-backend.service <<EOF
[Unit]
Description=DevShare Backend API
After=network.target

[Service]
User=root
WorkingDirectory=$REMOTE_PATH/backend-python
ExecStart=/usr/bin/python3 -m uvicorn main:app --host 0.0.0.0 --port 8100
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable "$DOMAIN"-backend
systemctl restart "$DOMAIN"-backend
print_success "后端服务已配置"
echo ""

echo "[6/8] 创建数据目录..."
mkdir -p "$REMOTE_PATH/backend-python/data"
print_success "数据目录已创建"
echo ""

echo "[7/8] 验证服务..."
sleep 3

if curl -s -o /dev/null -w "%{http_code}" http://localhost:8100/health > /dev/null 2>&1; then
    print_success "Python 后端正常"
else
    print_warning "Python 后端正在启动..."
    sleep 5
    if curl -s -o /dev/null -w "%{http_code}" http://localhost:8100/health > /dev/null 2>&1; then
        print_success "Python 后端正常"
    else
        print_error "Python 后端启动失败"
    fi
fi

echo ""
echo "[8/8] 检查 Nginx 状态..."
if systemctl is-active --quiet nginx; then
    print_success "Nginx 运行正常"
else
    print_error "Nginx 未运行"
    systemctl start nginx
fi
echo ""

echo "=========================================="
echo "  部署完成！"
echo "=========================================="
echo ""
echo "项目路径: $REMOTE_PATH"
echo "Nginx 配置: /etc/nginx/sites-available/$DOMAIN.conf"
echo "服务配置: /etc/systemd/system/$DOMAIN-backend.service"
echo ""
echo "验证地址:"
echo "  - 前端: http://$DOMAIN"
echo "  - API: http://$DOMAIN/api/"
echo ""
echo "配置 SSL:"
echo "  certbot --nginx -d $DOMAIN -d www.$DOMAIN"
echo ""
echo "管理命令:"
echo "  systemctl start $DOMAIN-backend"
echo "  systemctl stop $DOMAIN-backend"
echo "  systemctl restart $DOMAIN-backend"
echo "  systemctl status $DOMAIN-backend"
echo ""
echo "查看日志:"
echo "  journalctl -u $DOMAIN-backend -f"
echo "  tail -f /var/log/nginx/$DOMAIN-access.log"
echo ""
