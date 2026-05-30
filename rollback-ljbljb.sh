#!/bin/bash
set -e

echo "=========================================="
echo "  DevShare 回滚脚本 - ljbljb.com"
echo "=========================================="

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# 检查是否为 root
if [ "$EUID" -ne 0 ]; then 
    echo -e "${RED}请使用 root 权限运行此脚本${NC}"
    exit 1
fi

PROJECT_DIR="/var/www/ljbljb.com"

echo ""
echo -e "${YELLOW}警告: 此操作将停止新项目并禁用其配置${NC}"
read -p "确定要继续回滚吗? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "已取消回滚"
    exit 0
fi

# 1. 停止 Docker 服务
echo ""
echo -e "${YELLOW}[1/4] 停止新项目容器...${NC}"
if [ -f "$PROJECT_DIR/docker-compose.ljbljb.yml" ]; then
    cd "$PROJECT_DIR"
    docker-compose -f docker-compose.ljbljb.yml down || true
    echo -e "${GREEN}  ✓ 容器已停止${NC}"
else
    echo -e "${YELLOW}  ⚠ 配置文件不存在，跳过${NC}"
fi

# 2. 禁用 Nginx 配置
echo ""
echo -e "${YELLOW}[2/4] 禁用新项目 Nginx 配置...${NC}"
if [ -f "/etc/nginx/conf.d/ljbljb.com.conf" ]; then
    mv /etc/nginx/conf.d/ljbljb.com.conf /etc/nginx/conf.d/ljbljb.com.conf.disabled
    echo -e "${GREEN}  ✓ Nginx 配置已禁用${NC}"
else
    echo -e "${YELLOW}  ⚠ 配置文件不存在，跳过${NC}"
fi

# 3. 重新加载 Nginx
echo ""
echo -e "${YELLOW}[3/4] 重新加载 Nginx...${NC}"
if nginx -t; then
    nginx -s reload
    echo -e "${GREEN}  ✓ Nginx 已重新加载${NC}"
else
    echo -e "${RED}  ✗ Nginx 配置错误${NC}"
    echo "  尝试查找最新备份..."
    LATEST_BACKUP=$(ls -td /etc/nginx.backup.* 2>/dev/null | head -1)
    if [ -n "$LATEST_BACKUP" ]; then
        echo "  恢复备份: $LATEST_BACKUP"
        cp -r "$LATEST_BACKUP"/* /etc/nginx/
        nginx -t && nginx -s reload
    fi
fi

# 4. 验证现有服务
echo ""
echo -e "${YELLOW}[4/4] 验证现有服务...${NC}"
if curl -s -o /dev/null -w "%{http_code}" https://ljblib.xyz | grep -q "200\|301\|302"; then
    echo -e "${GREEN}  ✓ ljblib.xyz 服务正常${NC}"
else
    echo -e "${RED}  ✗ 现有服务可能有问题，请检查${NC}"
fi

echo ""
echo "=========================================="
echo -e "${GREEN}  回滚完成！${NC}"
echo "=========================================="
echo ""
echo "状态:"
echo "  - 新项目容器已停止"
echo "  - 新项目 Nginx 配置已禁用"
echo "  - 现有服务应正常运行"
echo ""
echo "如需清理数据卷 (谨慎操作):"
echo "  docker volume rm ljbljb_com_python_data"
echo "  docker volume rm ljbljb_com_java_data"
echo ""
