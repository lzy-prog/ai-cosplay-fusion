# 🚀 AI角色扮演场景融合器 - 部署指南

## 📋 部署概述

本项目将使用以下平台进行部署：
- **前端**: Vercel (免费)
- **后端**: Render (免费)

## 🌐 部署后的访问地址

- **前端应用**: `https://ai-cosplay-fusion.vercel.app`
- **后端API**: `https://ai-cosplay-fusion-backend.onrender.com`

## 🔧 部署步骤

### 1. 前端部署 (Vercel)

#### 方法一: 通过Vercel CLI
```bash
# 安装Vercel CLI
npm i -g vercel

# 登录Vercel
vercel login

# 部署前端
cd frontend
vercel --prod
```

#### 方法二: 通过GitHub集成
1. 将代码推送到GitHub仓库
2. 访问 [vercel.com](https://vercel.com)
3. 点击 "New Project"
4. 导入GitHub仓库
5. 设置根目录为 `frontend`
6. 添加环境变量:
   - `NEXT_PUBLIC_API_URL`: `https://ai-cosplay-fusion-backend.onrender.com`
7. 点击 "Deploy"

### 2. 后端部署 (Render)

#### 方法一: 通过Render Dashboard
1. 访问 [render.com](https://render.com)
2. 点击 "New +" → "Web Service"
3. 连接GitHub仓库
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

#### 方法二: 通过render.yaml
项目已包含 `render.yaml` 配置文件，可以直接使用。

### 3. 环境变量配置

#### 前端环境变量 (Vercel)
```
NEXT_PUBLIC_API_URL=https://ai-cosplay-fusion-backend.onrender.com
```

#### 后端环境变量 (Render)
```
FLASK_ENV=production
PORT=10000
HUGGINGFACE_API_TOKEN=your_token_here (可选)
```

## 🔄 自动部署

### GitHub Actions (可选)
创建 `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Production

on:
  push:
    branches: [ main ]

jobs:
  deploy-frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Vercel
        uses: amondnet/vercel-action@v20
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.ORG_ID }}
          vercel-project-id: ${{ secrets.PROJECT_ID }}
          working-directory: ./frontend

  deploy-backend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Render
        run: |
          curl -X POST "https://api.render.com/v1/services/${{ secrets.RENDER_SERVICE_ID }}/deploys" \
            -H "Authorization: Bearer ${{ secrets.RENDER_API_KEY }}"
```

## 🧪 测试部署

### 1. 健康检查
```bash
# 测试后端API
curl https://ai-cosplay-fusion-backend.onrender.com/api/health

# 测试前端
curl https://ai-cosplay-fusion.vercel.app
```

### 2. 功能测试
1. 访问前端URL
2. 上传测试图片
3. 检查处理流程
4. 验证结果下载

## 🔧 故障排除

### 常见问题

#### 1. CORS错误
- 确保后端设置了正确的CORS配置
- 检查前端API URL配置

#### 2. 图片上传失败
- 检查文件大小限制
- 验证MIME类型支持

#### 3. AI处理失败
- 检查Hugging Face API token
- 验证rembg库安装

### 日志查看
- **Vercel**: Dashboard → Functions → Logs
- **Render**: Dashboard → Logs

## 📊 性能优化

### 前端优化
- 启用Vercel的CDN
- 配置图片优化
- 使用Next.js的静态生成

### 后端优化
- 启用Render的自动扩展
- 配置缓存策略
- 优化AI模型加载

## 🔐 安全配置

### 环境变量
- 不要在代码中硬编码API密钥
- 使用环境变量管理敏感信息

### CORS配置
- 限制允许的域名
- 配置适当的请求头

## 📈 监控和维护

### 性能监控
- Vercel Analytics
- Render Metrics

### 错误追踪
- Sentry集成 (可选)
- 日志聚合服务

## 🎯 下一步

1. 配置自定义域名
2. 设置SSL证书
3. 配置CDN加速
4. 添加监控告警
5. 实现CI/CD流水线

---

## 📞 支持

如有部署问题，请检查：
1. 环境变量配置
2. 服务状态
3. 日志信息
4. 网络连接
