@echo off
echo 🎭 AI角色扮演场景融合器
echo ================================

REM 检查Node.js
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 请先安装Node.js (https://nodejs.org/)
    pause
    exit /b 1
)

REM 检查Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 请先安装Python 3.8+
    pause
    exit /b 1
)

echo ✅ 环境检查通过

REM 安装前端依赖
echo 📦 安装前端依赖...
cd frontend
if not exist "node_modules" (
    npm install
)

REM 安装后端依赖
echo 📦 安装后端依赖...
cd ..\backend
if not exist "venv" (
    echo 🔧 创建Python虚拟环境...
    python -m venv venv
)

echo 🔧 激活虚拟环境并安装依赖...
call venv\Scripts\activate.bat
pip install -r requirements.txt

REM 创建必要的目录
if not exist "uploads" mkdir uploads
if not exist "results" mkdir results

echo 🚀 启动服务...
echo.
echo 前端服务: http://localhost:3000
echo 后端服务: http://localhost:5000
echo.
echo 按 Ctrl+C 停止服务
echo.

REM 启动后端服务
start "Backend" cmd /k "venv\Scripts\activate.bat && python app.py"

REM 等待后端启动
timeout /t 3 /nobreak >nul

REM 启动前端服务
cd ..\frontend
start "Frontend" cmd /k "npm run dev"

echo ✅ 服务已启动
pause
