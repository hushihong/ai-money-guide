#!/bin/bash
# AI赚钱项目教程 - 一键部署脚本

set -e

echo "🚀 开始部署到GitHub Pages..."
echo ""

# 检查是否已登录GitHub
if ! git remote get-url origin 2>/dev/null | grep -q "github.com"; then
    echo "❌ 未检测到GitHub远程仓库"
    echo ""
    echo "请手动执行以下步骤："
    echo "1. 访问 https://github.com/new 创建新仓库（仓库名：ai-money-guide）"
    echo "2. 复制仓库URL"
    echo "3. 运行：git remote add origin <仓库URL>"
    echo "4. 运行：git push -u origin main"
    echo "5. 进入仓库Settings → Pages → 启用部署"
    exit 1
fi

# 添加GitHub Pages工作流
if [ ! -d ".github/workflows" ]; then
    mkdir -p .github/workflows
fi

# 创建部署配置
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

echo "✅ 工作流配置已创建"
echo ""

# 提交更改
echo "📝 提交更改..."
git add .
git commit -m "Add GitHub Pages deployment workflow" || echo "没有新更改"

# 推送到GitHub
echo "🚀 推送到GitHub..."
git push -u origin main || {
    echo "❌ 推送失败"
    echo ""
    echo "请确保已："
    echo "1. 创建GitHub仓库"
    echo "2. 添加远程仓库：git remote add origin <仓库URL>"
    echo "3. 推送代码：git push -u origin main"
    exit 1
}

echo ""
echo "✅ 部署完成！"
echo ""
echo "📋 下一步操作："
echo "1. 访问你的GitHub仓库"
echo "2. 进入 Settings → Pages"
echo "3. Source选择：Deploy from a branch"
echo "4. Branch选择：main，文件夹：/ (root)"
echo "5. 保存"
echo ""
echo "⏳ 等待1-2分钟后访问："
echo "https://你的用户名.github.io/ai-money-guide"
echo ""
echo "💰 添加赞助链接："
echo "1. 访问 https://www.buymeacoffee.com 注册"
echo "2. 创建页面并添加链接"
echo "3. 修改 index.html 中的赞助链接"
echo "4. 提交并推送：git commit -am 'Add sponsor links' && git push"
