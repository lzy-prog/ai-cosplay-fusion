# 🚀 AI角色扮演场景融合器 - 完整部署指南

## 📋 部署概览

您的项目已经准备好部署！代码已推送到GitHub: https://github.com/lzy-prog/ai-cosplay-fusion

## 🎯 部署步骤

### 第一步：部署前端到Vercel

1. **访问 Vercel**
   - 打开浏览器，访问：https://vercel.com
   - 点击 "Sign up" 或 "Log in"

2. **使用GitHub登录**
   - 选择 "Continue with GitHub"
   - 授权Vercel访问您的GitHub账户

3. **导入项目**
   - 点击 "New Project"
   - 找到 `lzy-prog/ai-cosplay-fusion` 仓库
   - 点击 "Import"

4. **配置项目**
   - **Project Name**: `ai-cosplay-fusion`
   - **Framework Preset**: `Next.js` (自动检测)
   - **Root Directory**: `frontend` ⚠️ 重要：选择frontend文件夹
   - **Build Command**: `npm run build` (默认)
   - **Output Directory**: `.next` (默认)

5. **添加环境变量**
   - 点击 "Environment Variables"
   - 添加：
     - **Name**: `NEXT_PUBLIC_API_URL`
     - **Value**: `https://ai-cosplay-fusion-backend.onrender.com`

6. **开始部署**
   - 点击 "Deploy"
   - 等待2-3分钟

### 第二步：部署后端到Render

1. **访问 Render**
   - 打开新标签页，访问：https://render.com
   - 点击 "Get Started for Free"

2. **使用GitHub登录**
   - 选择 "Continue with GitHub"
   - 授权Render访问您的GitHub账户

3. **创建Web服务**
   - 点击 "New +" → "Web Service"
   - 找到 `lzy-prog/ai-cosplay-fusion` 仓库
   - 点击 "Connect"

4. **配置服务**
   - **Name**: `ai-cosplay-fusion-backend`
   - **Root Directory**: `backend` ⚠️ 重要：选择backend文件夹
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`

5. **添加环境变量**
   - 点击 "Advanced"
   - 添加：
     - **Key**: `FLASK_ENV`
     - **Value**: `production`
     - **Key**: `PORT`
     - **Value**: `10000`

6. **开始部署**
   - 点击 "Create Web Service"
   - 等待5-10分钟

## 🎉 部署完成

部署完成后，您将获得：

- **前端应用**: `https://ai-cosplay-fusion.vercel.app`
- **后端API**: `https://ai-cosplay-fusion-backend.onrender.com`

## 🧪 测试应用

1. 访问前端URL
2. 上传一张角色扮演照片
3. 等待AI处理完成
4. 下载融合结果

## 📞 需要帮助？

如果在部署过程中遇到问题，请告诉我：
1. 在哪一步遇到了问题
2. 看到了什么错误信息
3. 我会立即帮您解决！

## 🎯 功能特性

- ✅ 智能角色识别（支持10个热门角色）
- ✅ AI背景生成（基于Stable Diffusion）
- ✅ 精准人物抠图（使用rembg AI）
- ✅ 智能图像融合（自动光线匹配）
- ✅ 现代化界面（响应式设计）
- ✅ 移动端支持

## 🎭 支持的角色

- 皮卡丘、鸣人、孙悟空
- 蜘蛛侠、蝙蝠侠、超人
- 钢铁侠、美国队长
- 米老鼠、艾莎

---

**现在您可以开始部署了！整个过程大约需要10-15分钟。**
