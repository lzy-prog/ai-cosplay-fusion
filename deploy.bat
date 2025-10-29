@echo off
echo 🚀 AI角色扮演场景融合器 - 一键部署
echo ==================================

REM 检查必要的工具
where git >nul 2>&1
if errorlevel 1 (
    echo ❌ 请先安装 Git
    echo    https://git-scm.com/
    pause
    exit /b 1
)

where node >nul 2>&1
if errorlevel 1 (
    echo ❌ 请先安装 Node.js
    echo    https://nodejs.org/
    pause
    exit /b 1
)

echo ✅ 环境检查通过

REM 检查是否在Git仓库中
if not exist ".git" (
    echo 📦 初始化Git仓库...
    git init
    git add .
    git commit -m "Initial commit: AI Cosplay Fusion"
)

REM 检查GitHub远程仓库
git remote get-url origin >nul 2>&1
if errorlevel 1 (
    echo 📝 请先创建GitHub仓库并设置远程地址:
    echo    git remote add origin https://github.com/yourusername/ai-cosplay-fusion.git
    echo    git push -u origin main
    echo.
    echo 然后重新运行此脚本
    pause
    exit /b 1
)

echo 📤 推送代码到GitHub...
git add .
git commit -m "Deploy: Update for production deployment" 2>nul
git push origin main

echo.
echo 🎯 部署步骤:
echo ============
echo.
echo 1️⃣ 前端部署 (Vercel):
echo    • 访问: https://vercel.com
echo    • 点击 'New Project'
echo    • 导入GitHub仓库
echo    • 设置根目录为 'frontend'
echo    • 添加环境变量:
echo      NEXT_PUBLIC_API_URL=https://ai-cosplay-fusion-backend.onrender.com
echo    • 点击 'Deploy'
echo.
echo 2️⃣ 后端部署 (Render):
echo    • 访问: https://render.com
echo    • 点击 'New +' → 'Web Service'
echo    • 连接GitHub仓库
echo    • 配置:
echo      - Name: ai-cosplay-fusion-backend
echo      - Root Directory: backend
echo      - Environment: Python 3
echo      - Build Command: pip install -r requirements.txt
echo      - Start Command: python app.py
echo    • 添加环境变量:
echo      FLASK_ENV=production
echo      PORT=10000
echo    • 点击 'Create Web Service'
echo.
echo 3️⃣ 等待部署完成 (约5-10分钟)
echo.
echo 4️⃣ 访问应用:
echo    • 前端: https://your-app-name.vercel.app
echo    • 后端: https://ai-cosplay-fusion-backend.onrender.com
echo.
echo 🎉 部署完成！
echo.
echo 📚 详细说明请查看: DEPLOYMENT.md
pause
