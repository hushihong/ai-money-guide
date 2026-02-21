#!/bin/bash
# GitHub Pages部署脚本

echo "🚀 开始部署到GitHub Pages..."
echo ""

# 检查是否已初始化Git仓库
if [ ! -d ".git" ]; then
    echo "📦 初始化Git仓库..."
    git init
fi

# 添加所有文件
echo "📝 添加文件到Git..."
git add .

# 创建初始提交
if [ -z "$(git log --oneline -1)" ]; then
    echo "🌱 创建初始提交..."
    git commit -m "Initial commit: AI赚钱项目合集"
fi

# 询问用户GitHub仓库地址
echo ""
echo "请输入GitHub仓库地址（格式：https://github.com/用户名/仓库名.git）"
read -p "仓库地址: " repo_url

if [ -z "$repo_url" ]; then
    echo "❌ 仓库地址不能为空"
    exit 1
fi

# 添加远程仓库
echo "🔗 添加远程仓库..."
git remote add origin "$repo_url"

# 推送到GitHub
echo "🚀 推送到GitHub..."
git push -u origin main

echo ""
echo "✅ 部署成功！"
echo ""
echo "📖 下一步："
echo "1. 访问GitHub仓库设置页面"
echo "2. 找到Pages设置"
echo "3. 选择main分支，/ (root) 目录"
echo "4. 保存后等待1-2分钟"
echo "5. 访问 https://你的用户名.github.io/仓库名"
