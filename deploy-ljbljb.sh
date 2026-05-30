#!/bin/bash
set -e

echo "=========================================="
echo "  DevShare 部署脚本 - ljbljb.com"
echo "=========================================="

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 检查是否为 root 用户
if [ "$EUID" -ne 0 ]; then 
    echo -e "${RED}请使用 root 权限运行此脚本${NC}"
    echo "使用: sudo $0"
    exit 1
fi

# 检查项目目录
PROJECT_DIR="/var/www/ljbljb.com"
if [ ! -d "$PROJECT_DIR" ]; then
    echo -e "${RED}项目目录不存在: $PROJECT_DIR${NC}"
    echo "请先上传项目文件到该目录"
    exit 1
fi

cd "$PROJECT_DIR"

# 1. 检查现有服务
echo ""
echo -e "${YELLOW}[1/8] 检查现有服务状态...${NC}"
if curl -s -o /dev/null -w "%{http_code}" https://ljblib.xyz | grep -q "200\|301\|302"; then
    echo -e "${GREEN}  ✓ ljblib.xyz 现有服务正常${NC}"
else
    echo -e "${RED}  ⚠ 警告: 现有服务可能有问题${NC}"
    read -p "是否继续部署? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# 2. 备份配置
echo ""
echo -e "${YELLOW}[2/8] 备份 Nginx 配置...${NC}"
BACKUP_DATE=$(date +%Y%m%d_%H%M%S)
cp -r /etc/nginx /etc/nginx.backup.$BACKUP_DATE
echo -e "${GREEN}  ✓ 已备份到: /etc/nginx.backup.$BACKUP_DATE${NC}"

# 3. 创建数据目录
echo ""
echo -e "${YELLOW}[3/8] 准备数据目录...${NC}"
mkdir -p "$PROJECT_DIR/backend-python/data"
chmod 755 "$PROJECT_DIR/backend-python/data"
echo -e "${GREEN}  ✓ 数据目录已准备${NC}"

# 4. 构建前端
echo ""
echo -e "${YELLOW}[4/8] 构建前端...${NC}"
cd "$PROJECT_DIR/frontend"
if [ ! -d "node_modules" ]; then
    echo "  安装依赖..."
    npm install
fi
npm run build
if [ -d "dist" ]; then
    echo -e "${GREEN}  ✓ 前端构建完成${NC}"
else
    echo -e "${RED}  ✗ 前端构建失败${NC}"
    exit 1
fi
cd "$PROJECT_DIR"

# 5. 复制 Nginx 配置
echo ""
echo -e "${YELLOW}[5/8] 配置 Nginx...${NC}"
if [ -f "nginx.ljbljb.com.conf" ]; then
    cp nginx.ljbljb.com.conf /etc/nginx/conf.d/ljbljb.com.conf
    echo -e "${GREEN}  ✓ Nginx 配置已复制${NC}"
else
    echo -e "${RED}  ✗ nginx.ljbljb.com.conf 文件不存在${NC}"
    exit 1
fi

# 6. 启动 Docker 服务
echo ""
echo -e "${YELLOW}[6/8] 启动 Docker 服务...${NC}"
if [ -f "docker-compose.ljbljb.yml" ]; then
    docker-compose -f docker-compose.ljbljb.yml up -d --build
    echo -e "${GREEN}  ✓ Docker 服务已启动${NC}"
else
    echo -e "${RED}  ✗ docker-compose.ljbljb.yml 文件不存在${NC}"
    exit 1
fi

# 7. 等待服务启动
echo ""
echo -e "${YELLOW}[7/8] 等待服务启动...${NC}"
sleep 15

# 检查容器状态
if docker-compose -f docker-compose.ljbljb.yml ps | grep -q "Up"; then
    echo -e "${GREEN}  ✓ 容器运行正常${NC}"
else
    echo -e "${RED}  ⚠ 警告: 部分容器可能未正常启动${NC}"
    docker-compose -f docker-compose.ljbljb.yml ps
fi

# 8. 验证 Nginx 并重新加载
echo ""
echo -e "${YELLOW}[8/8] 验证并加载 Nginx 配置...${NC}"
if nginx -t; then
    nginx -s reload
    echo -e "${GREEN}  ✓ Nginx 已重新加载${NC}"
else
    echo -e "${RED}  ✗ Nginx 配置错误${NC}"
    echo "  正在恢复备份..."
    cp -r /etc/nginx.backup.$BACKUP_DATE/* /etc/nginx/
    nginx -t && nginx -s reload
    exit 1
fi

echo ""
echo "=========================================="
echo -e "${GREEN}  部署完成！${NC}"
echo "=========================================="
echo ""
echo "验证部署:"
echo "  现有服务: https://ljblib.xyz"
echo "  新服务:   http://ljbljb.com"
echo ""
echo "下一步操作:"
echo "  1. 配置 SSL 证书: certbot --nginx -d ljbljb.com -d www.ljbljb.com"
echo "  2. 查看服务日志: cd $PROJECT_DIR && docker-compose -f docker-compose.ljbljb.yml logs -f"
echo "  3. 如遇问题，快速回滚: ./rollback-ljbljb.sh"
echo ""
echo "备份文件: /etc/nginx.backup.$BACKUP_DATE"
echo ""
