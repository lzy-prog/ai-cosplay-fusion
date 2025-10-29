@echo off
echo 🚀 启动本地测试环境...
echo.

REM 检查Node.js
where node >nul 2>&1
if errorlevel 1 (
    echo ❌ 请先安装Node.js: https://nodejs.org/
    pause
    exit /b 1
)

REM 检查Python
where python >nul 2>&1
if errorlevel 1 (
    echo ❌ 请先安装Python 3: https://www.python.org/
    pause
    exit /b 1
)

echo ✅ 环境检查通过
echo.

REM 启动后端
echo 📦 启动后端服务...
cd backend
if not exist "venv" (
    echo 创建Python虚拟环境...
    python -m venv venv
)

call venv\Scripts\activate.bat
pip install -r requirements.txt --quiet

echo 🔧 后端服务启动在: http://localhost:5000
echo.

start "后端服务" cmd /k "venv\Scripts\activate.bat && python app.py"

REM 等待后端启动
timeout /t 3 /nobreak >nul

REM 启动前端
echo 📦 启动前端服务...
cd ..\frontend

if not exist "node_modules" (
    echo 安装前端依赖...
    npm install --quiet
)

echo 🔧 前端服务启动在: http://localhost:3000
echo.
echo 🎉 服务已启动！
echo.
echo ✅ 前端: http://localhost:3000
echo ✅ 后端: http://localhost:5000
echo.
echo 关闭窗口即可停止服务

start "前端服务" cmd /k "npm run dev"

pause
