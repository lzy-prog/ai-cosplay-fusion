# 🚀 快速部署指南

## 📋 部署概览

您的AI角色扮演场景融合器已经配置好部署！只需要几个简单步骤就能通过URL访问。

## ⚡ 一键部署

### Linux/Mac用户
```bash
./deploy.sh
```

### Windows用户
```cmd
deploy.bat
```

## 🎯 手动部署步骤

### 1️⃣ 准备GitHub仓库
```bash
# 如果还没有GitHub仓库
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/ai-cosplay-fusion.git
git push -u origin main
```

### 2️⃣ 部署前端 (Vercel)
1. 访问 [vercel.com](https://vercel.com)
2. 点击 "New Project"
3. 导入您的GitHub仓库
4. 设置根目录为 `frontend`
5. 添加环境变量:
   - `NEXT_PUBLIC_API_URL`: `https://ai-cosplay-fusion-backend.onrender.com`
6. 点击 "Deploy"

### 3️⃣ 部署后端 (Render)
1. 访问 [render.com](https://render.com)
2. 点击 "New +" → "Web Service"
3. 连接您的GitHub仓库
4. 配置服务:
   - **Name**: `ai-cosplay-fusion-backend`
   - **Root Directory**: `backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
5. 添加环境变量:
   - `FLASK_ENV`: `production`
   - `PORT`: `10000`
6. 点击 "Create Web Service"

## 🌐 访问您的应用

部署完成后，您将获得以下URL：
- **前端应用**: `https://your-app-name.vercel.app`
- **后端API**: `https://ai-cosplay-fusion-backend.onrender.com`

## 🔧 环境变量说明

### 前端环境变量 (Vercel)
```
NEXT_PUBLIC_API_URL=https://ai-cosplay-fusion-backend.onrender.com
```

### 后端环境变量 (Render)
```
FLASK_ENV=production
PORT=10000
HUGGINGFACE_API_TOKEN=your_token_here (可选，用于更好的背景生成)
```

## 🧪 测试部署

### 健康检查
```bash
# 测试后端
curl https://ai-cosplay-fusion-backend.onrender.com/api/health

# 测试前端
curl https://your-app-name.vercel.app
```

### 功能测试
1. 访问前端URL
2. 上传一张角色扮演照片
3. 等待AI处理完成
4. 下载融合结果

## 🎉 部署完成！

恭喜！您的AI角色扮演场景融合器现在已经可以通过URL访问了。

### 功能特性
- ✅ 智能角色识别
- ✅ AI背景生成
- ✅ 精准人物抠图
- ✅ 智能图像融合
- ✅ 现代化界面
- ✅ 移动端支持

### 支持的角色
- 皮卡丘、鸣人、孙悟空
- 蜘蛛侠、蝙蝠侠、超人
- 钢铁侠、美国队长
- 米老鼠、艾莎

## 📞 需要帮助？

如果遇到问题，请检查：
1. GitHub仓库是否正确推送
2. 环境变量是否正确配置
3. 服务是否成功部署
4. 网络连接是否正常

详细说明请查看 `DEPLOYMENT.md` 文件。
