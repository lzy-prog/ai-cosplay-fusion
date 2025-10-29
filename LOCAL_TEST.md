# 🚀 本地快速测试指南

## 📋 前置要求

- **Node.js 18+**: [下载地址](https://nodejs.org/)
- **Python 3.8+**: [下载地址](https://www.python.org/)

## ⚡ 快速启动（一键启动）

### Mac/Linux用户
```bash
./start-local.sh
```

### Windows用户
```cmd
start-local.bat
```

## 📝 手动启动步骤

### 第一步：启动后端

```bash
cd backend

# 创建虚拟环境（首次运行）
python3 -m venv venv  # Mac/Linux
python -m venv venv   # Windows

# 激活虚拟环境
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate.bat # Windows

# 安装依赖
pip install -r requirements.txt

# 启动后端（端口5000）
python app.py
```

后端启动后会显示：
```
Running on http://0.0.0.0:5000
```

### 第二步：启动前端（新开一个终端）

```bash
cd frontend

# 安装依赖（首次运行）
npm install

# 启动前端（端口3000）
npm run dev
```

前端启动后会显示：
```
Ready in ... seconds
Local: http://localhost:3000
```

## 🎯 访问应用

打开浏览器，访问：
- **前端应用**: http://localhost:3000
- **后端API**: http://localhost:5000/api/health

## 🧪 测试步骤

1. **访问前端**
   - 打开 http://localhost:3000
   - 确认页面正常加载

2. **上传图片**
   - 点击上传区域或拖拽图片
   - 选择一张角色扮演照片

3. **查看结果**
   - 等待处理完成
   - 查看识别到的角色
   - 测试下载功能

## ✅ 验证后端是否运行

在浏览器访问：
```
http://localhost:5000/api/health
```

应该看到：
```json
{"message":"Backend is running","status":"ok"}
```

## 🛑 停止服务

- **Mac/Linux**: 在终端按 `Ctrl+C`
- **Windows**: 关闭命令窗口

## 🐛 常见问题

### 端口被占用
如果5000或3000端口被占用：
- 修改后端端口：编辑 `backend/app.py`，修改 `port=5000` 为其他端口
- 修改前端端口：运行 `npm run dev -p 3001`

### 依赖安装失败
```bash
# 清除缓存后重新安装
npm cache clean --force  # 前端
pip install --upgrade pip  # 后端
```

### Python虚拟环境问题
```bash
# 删除旧的虚拟环境重新创建
rm -rf backend/venv  # Mac/Linux
rmdir /s backend\venv  # Windows
```

## 🎉 完成！

一切正常后，您就可以在本地完整测试AI角色扮演场景融合器了！
