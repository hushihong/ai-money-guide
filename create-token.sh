#!/bin/bash
# 创建GitHub Personal Access Token并部署

echo "🔑 创建GitHub Personal Access Token"
echo ""
echo "请按以下步骤操作："
echo ""
echo "1. 访问：https://github.com/settings/tokens/new"
echo "2. 设置："
echo "   - Note: AI Money Guide"
echo "   - Expiration: No expiration（推荐）"
echo "   - Select scopes: 勾选所有权限（至少需要repo权限）"
echo "3. 点击 'Generate token'"
echo "4. 复制生成的token（以ghp_开头的字符串）"
echo ""
read -p "粘贴token（以ghp_开头）: " github_token

if [ -z "$github_token" ]; then
    echo "❌ Token不能为空"
    exit 1
fi

# 保存token
echo "$github_token" > .github_token

# 创建仓库
echo "📦 创建GitHub仓库..."
curl -X POST -H "Authorization: token $github_token" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/user/repos \
  -d '{"name":"ai-money-guide","private":false,"auto_init":false}'

# 推送代码
echo "🚀 推送代码..."
git push -u origin master

# 配置GitHub Pages
echo "⚙️  配置GitHub Pages..."
curl -X PUT -H "Authorization: token $github_token" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/hushpcl/ai-money-guide/pages \
  -d '{"source":{"branch":"master","path":"/"}}'

echo ""
echo "✅ 部署完成！"
echo ""
echo "📋 下一步："
echo "1. 访问 https://github.com/hushpcl/ai-money-guide/settings/pages"
echo "2. 确认Source设置为：Deploy from a branch"
echo "3. Branch选择：master，文件夹：/ (root)"
echo "4. 保存"
echo ""
echo "⏳ 等待1-2分钟后访问："
echo "https://hushpcl.github.io/ai-money-guide"
