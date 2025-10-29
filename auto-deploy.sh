#!/bin/bash

echo "🚀 AI角色扮演场景融合器 - 自动部署助手"
echo "======================================"
echo ""
echo "您的GitHub仓库: https://github.com/lzy-prog/ai-cosplay-fusion"
echo ""

# 检查操作系统
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    echo "🍎 检测到macOS系统"
    echo ""
    echo "正在打开部署页面..."
    
    # 打开Vercel部署页面
    open "https://vercel.com/new?import-project=https://github.com/lzy-prog/ai-cosplay-fusion"
    
    echo "✅ Vercel部署页面已打开"
    echo "📋 请按照以下步骤操作："
    echo "   1. 使用GitHub登录Vercel"
    echo "   2. 设置Root Directory为 'frontend'"
    echo "   3. 添加环境变量: NEXT_PUBLIC_API_URL=https://ai-cosplay-fusion-backend.onrender.com"
    echo "   4. 点击Deploy"
    echo ""
    
    sleep 5
    
    # 打开Render部署页面
    open "https://dashboard.render.com/new/web"
    
    echo "✅ Render部署页面已打开"
    echo "📋 请按照以下步骤操作："
    echo "   1. 使用GitHub登录Render"
    echo "   2. 连接仓库: lzy-prog/ai-cosplay-fusion"
    echo "   3. 设置Root Directory为 'backend'"
    echo "   4. 设置Environment为 'Python 3'"
    echo "   5. 添加环境变量: FLASK_ENV=production, PORT=10000"
    echo "   6. 点击Create Web Service"
    echo ""
    
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    echo "🐧 检测到Linux系统"
    echo ""
    echo "正在打开部署页面..."
    
    # 尝试不同的浏览器
    if command -v xdg-open &> /dev/null; then
        xdg-open "https://vercel.com/new?import-project=https://github.com/lzy-prog/ai-cosplay-fusion"
        sleep 5
        xdg-open "https://dashboard.render.com/new/web"
    elif command -v firefox &> /dev/null; then
        firefox "https://vercel.com/new?import-project=https://github.com/lzy-prog/ai-cosplay-fusion" &
        sleep 5
        firefox "https://dashboard.render.com/new/web" &
    elif command -v google-chrome &> /dev/null; then
        google-chrome "https://vercel.com/new?import-project=https://github.com/lzy-prog/ai-cosplay-fusion" &
        sleep 5
        google-chrome "https://dashboard.render.com/new/web" &
    else
        echo "❌ 未找到浏览器，请手动打开以下链接："
        echo "   Vercel: https://vercel.com/new?import-project=https://github.com/lzy-prog/ai-cosplay-fusion"
        echo "   Render: https://dashboard.render.com/new/web"
    fi
    
else
    echo "❓ 未识别的操作系统"
    echo "请手动打开以下链接："
    echo "   Vercel: https://vercel.com/new?import-project=https://github.com/lzy-prog/ai-cosplay-fusion"
    echo "   Render: https://dashboard.render.com/new/web"
fi

echo ""
echo "📚 详细部署说明请查看: DEPLOYMENT_GUIDE.md"
echo "🎉 部署完成后，您就可以通过URL访问应用了！"
