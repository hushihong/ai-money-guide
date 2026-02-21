#!/bin/bash
# 添加赞助链接脚本

set -e

echo "🔗 添加赞助链接"
echo ""

# 获取GitHub用户名
read -p "请输入你的GitHub用户名: " github_username

if [ -z "$github_username" ]; then
    echo "❌ 用户名不能为空"
    exit 1
fi

# 备份原文件
cp index.html index.html.bak

# 替换Buy Me a Coffee链接
sed -i "s|https://www.buymeacoffee.com/你的用户名|https://www.buymeacoffee.com/$github_username|g" index.html

# 替换GitHub Sponsors链接
sed -i "s|https://github.com/sponsors/你的用户名|https://github.com/sponsors/$github_username|g" index.html

# 更新README中的链接
sed -i "s|https://github.com/你的用户名/ai-money-guide|https://github.com/$github_username/ai-money-guide|g" README.md

# 提交更改
echo "✅ 赞助链接已更新"
echo ""
echo "📋 提交并推送："
echo "git add index.html README.md"
echo "git commit -m 'Add sponsor links'"
echo "git push"
