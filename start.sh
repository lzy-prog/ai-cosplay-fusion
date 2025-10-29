#!/bin/bash

# AI角色扮演场景融合器启动脚本

echo "🎭 AI角色扮演场景融合器"
echo "================================"

# 检查Node.js
if ! command -v node &> /dev/null; then
    echo "❌ 请先安装Node.js (https://nodejs.org/)"
    exit 1
fi

# 检查Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 请先安装Python 3.8+"
    exit 1
fi

echo "✅ 环境检查通过"

# 安装前端依赖
echo "📦 安装前端依赖..."
cd frontend
if [ ! -d "node_modules" ]; then
    npm install
fi

# 安装后端依赖
echo "📦 安装后端依赖..."
cd ../backend
if [ ! -d "venv" ]; then
    echo "🔧 创建Python虚拟环境..."
    python3 -m venv venv
fi

echo "🔧 激活虚拟环境并安装依赖..."
source venv/bin/activate
pip install -r requirements.txt

# 创建必要的目录
mkdir -p uploads results

echo "🚀 启动服务..."
echo ""
echo "前端服务: http://localhost:3000"
echo "后端服务: http://localhost:5000"
echo ""
echo "按 Ctrl+C 停止服务"
echo ""

# 启动后端服务
python app.py &
BACKEND_PID=$!

# 等待后端启动
sleep 3

# 启动前端服务
cd ../frontend
npm run dev &
FRONTEND_PID=$!

# 等待用户中断
wait

# 清理进程
echo "🛑 停止服务..."
kill $BACKEND_PID $FRONTEND_PID 2>/dev/null
echo "✅ 服务已停止"
