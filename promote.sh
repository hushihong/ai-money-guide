#!/bin/bash
# 自动推广脚本

echo "🚀 开始推广..."
echo ""

# 读取推广文案
PROMO_TEXT=$(cat promotion.md | head -20)

# 复制到剪贴板（如果支持）
if command -v xclip &> /dev/null; then
    echo "$PROMO_TEXT" | xclip -selection clipboard
    echo "✅ 推广文案已复制到剪贴板"
fi

echo ""
echo "📋 推广渠道："
echo ""
echo "1. 朋友圈：直接粘贴文案"
echo "2. Telegram群组：分享链接"
echo "3. 知乎：写文章，粘贴文案"
echo "4. B站：制作视频，简介添加链接"
echo "5. 微博：分享链接+标签"
echo ""
echo "🔗 分享链接："
echo "https://hushihong.github.io/ai-money-guide/"
echo ""
echo "💡 推广技巧："
echo "• 每天分享1-2次"
echo "• 加入赚钱相关群组"
echo "• 回答相关问题，分享链接"
echo "• 制作视频教程"
echo ""
echo "📊 收益追踪："
echo "• Buy Me a Coffee：https://www.buymeacoffee.com/hushihong"
echo "• GitHub Sponsors：https://github.com/sponsors/hushihong"
echo ""
echo "🎯 目标：第一个月赚5-15美元"
echo ""
echo "开始推广吧！🚀"
