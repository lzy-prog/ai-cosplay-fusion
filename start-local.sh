#!/bin/bash

echo "🚀 启动本地测试环境..."
echo ""

# 检查Node.js
if ! command -v node &> /dev/null; then
    echo "❌ 请先安装Node.js: https://nodejs.org/"
    exit 1
fi

# 检查Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 请先安装Python 3: https://www.python.org/"
    exit 1
fi

echo "✅ 环境检查通过"
echo ""

# 启动后端
echo "📦 启动后端服务..."
cd backend
if [ ! -d "venv" ]; then
    echo "创建Python虚拟环境..."
    python3 -m venv venv
fi

source venv/bin/activate
pip install -r requirements.txt --quiet

echo "🔧 后端服务启动在: http://localhost:5000"
echo ""

# 在后台启动后端
python3 app.py &
BACKEND_PID=$!

# 等待后端启动
sleep 3

# 启动前端
echo "📦 启动前端服务..."
cd ../frontend

if [ ! -d "node_modules" ]; then
    echo "安装前端依赖..."
    npm install --quiet
fi

echo "🔧 前端服务启动在: http://localhost:3000"
echo ""
echo "🎉 服务已启动！"
echo ""
echo "✅ 前端: http://localhost:3000"
echo "✅ 后端: http://localhost:5000"
echo ""
echo "按 Ctrl+C 停止所有服务"

# 等待用户中断
wait $BACKEND_PID
