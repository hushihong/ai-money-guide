#!/bin/bash
# 快速部署脚本（需要GitHub Token）

set -e

echo "🚀 快速部署到GitHub Pages"
echo ""

# 检查token
if [ ! -f .github_token ]; then
    echo "❌ 未找到token文件"
    echo ""
    echo "请按以下步骤创建token："
    echo "1. 访问：https://github.com/settings/tokens/new"
    echo "2. Note: AI Money Guide"
    echo "3. Expiration: No expiration"
    echo "4. Scopes: 勾选所有权限（repo）"
    echo "5. 生成并复制token（以ghp_开头）"
    echo "6. 运行：echo '你的token' > .github_token"
    echo ""
    exit 1
fi

TOKEN=$(cat .github_token)

# 创建仓库
echo "📦 创建仓库..."
curl -s -X POST -H "Authorization: token $TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/user/repos \
  -d '{"name":"ai-money-guide","private":false,"auto_init":false}' > /dev/null

# 推送代码
echo "🚀 推送代码..."
git push -u origin master

# 配置GitHub Pages
echo "⚙️  配置GitHub Pages..."
curl -s -X PUT -H "Authorization: token $TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/hushpcl/ai-money-guide/pages \
  -d '{"source":{"branch":"master","path":"/"}}' > /dev/null

echo ""
echo "✅ 部署完成！"
echo ""
echo "📋 下一步："
echo "1. 访问：https://github.com/hushpcl/ai-money-guide/settings/pages"
echo "2. 确认Source设置为：Deploy from a branch"
echo "3. Branch选择：master，文件夹：/ (root)"
echo "4. 保存"
echo ""
echo "⏳ 等待1-2分钟后访问："
echo "https://hushpcl.github.io/ai-money-guide"
