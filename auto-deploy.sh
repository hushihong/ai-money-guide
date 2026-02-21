#!/bin/bash
# 一键部署脚本 - 包含所有步骤

set -e

echo "🚀 AI赚钱项目教程 - 一键部署"
echo ""

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 检查是否已初始化Git
if [ ! -d ".git" ]; then
    echo "📦 初始化Git仓库..."
    git init
    git config user.name "AI Assistant"
    git config user.email "assistant@openclaw.ai"
fi

# 创建必要的目录
mkdir -p .github/workflows

# 创建部署工作流
cat > .github/workflows/deploy.yml << 'EOF'
name: Deploy to GitHub Pages

on:
  push:
    branches: ["main"]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Pages
        uses: actions/configure-pages@v5

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: '.'

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
EOF

echo -e "${GREEN}✅ 工作流配置已创建${NC}"
echo ""

# 检查远程仓库
if git remote get-url origin 2>/dev/null | grep -q "github.com"; then
    echo "🔗 远程仓库已配置："
    git remote get-url origin
    echo ""
else
    echo -e "${YELLOW}⚠️  未检测到远程仓库${NC}"
    echo ""
    echo "请执行以下步骤："
    echo "1. 访问 https://github.com/new 创建新仓库（仓库名：ai-money-guide）"
    echo "2. 复制仓库URL"
    echo "3. 运行：git remote add origin <仓库URL>"
    echo "4. 运行：git push -u origin main"
    echo ""
    read -p "完成后按回车继续..."
fi

# 提交所有文件
echo "📝 提交文件..."
git add .
git commit -m "Add AI赚钱项目教程" || echo "没有新更改"

# 推送到GitHub
if git remote get-url origin 2>/dev/null | grep -q "github.com"; then
    echo "🚀 推送到GitHub..."
    git push -u origin main || {
        echo -e "${RED}❌ 推送失败${NC}"
        echo ""
        echo "请确保已："
        echo "1. 创建GitHub仓库"
        echo "2. 添加远程仓库"
        echo "3. 配置Git认证"
        exit 1
    }
else
    echo -e "${YELLOW}⚠️  跳过推送（未配置远程仓库）${NC}"
fi

echo ""
echo -e "${GREEN}✅ 部署完成！${NC}"
echo ""
echo "📋 下一步操作："
echo ""
echo "1️⃣  访问你的GitHub仓库"
echo "2️⃣  进入 Settings → Pages"
echo "3️⃣  Source选择：Deploy from a branch"
echo "4️⃣  Branch选择：main，文件夹：/ (root)"
echo "5️⃣  保存"
echo ""
echo "⏳ 等待1-2分钟后访问："
echo -e "${YELLOW}https://你的用户名.github.io/ai-money-guide${NC}"
echo ""
echo "💰 添加赞助链接："
echo "   ./add-sponsor-links.sh"
echo "   然后运行：git commit -am 'Add sponsor links' && git push"
echo ""
echo "🎉 开始赚钱吧！"
