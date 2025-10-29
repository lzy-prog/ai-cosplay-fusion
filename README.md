# 🎭 AI角色扮演场景融合器

一个基于AI技术的角色扮演照片处理工具，能够自动识别角色并生成专属背景进行图像融合。

## ✨ 功能特性

- 🎯 **智能角色识别**: 自动识别照片中的角色扮演角色
- 🎨 **AI背景生成**: 根据角色生成专属的经典场景背景
- ✂️ **精准人物抠图**: 使用AI技术精确提取人物主体
- 🌟 **智能图像融合**: 自动调整光线和色彩，实现自然融合效果
- 📱 **现代化界面**: 响应式设计，支持拖拽上传
- ⚡ **实时处理**: 显示处理进度和状态

## 🚀 技术栈

### 前端
- **Next.js 14** - React框架
- **TypeScript** - 类型安全
- **Tailwind CSS** - 样式框架
- **React Dropzone** - 文件上传
- **Lucide React** - 图标库

### 后端
- **Python Flask** - Web框架
- **PIL/Pillow** - 图像处理
- **OpenCV** - 计算机视觉
- **rembg** - AI背景移除
- **Stable Diffusion** - AI图像生成
- **NumPy** - 数值计算

## 📦 安装和运行

### 环境要求
- Node.js 18+
- Python 3.8+
- pip

### 前端安装
```bash
cd frontend
npm install
npm run dev
```

### 后端安装
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### 环境配置
1. 复制 `.env.example` 为 `.env`
2. 配置 Hugging Face API Token（可选，用于背景生成）

## 🎮 使用方法

1. **上传照片**: 拖拽或点击上传角色扮演照片
2. **AI识别**: 系统自动识别角色
3. **背景生成**: 根据角色生成专属背景
4. **图像融合**: 自动进行人物抠图和融合处理
5. **下载结果**: 保存最终的融合图片

## 🎯 支持的角色

- 皮卡丘 (Pokemon)
- 鸣人 (火影忍者)
- 孙悟空 (龙珠)
- 蜘蛛侠 (Marvel)
- 蝙蝠侠 (DC)
- 超人 (DC)
- 米老鼠 (Disney)
- 艾莎 (冰雪奇缘)
- 钢铁侠 (Marvel)
- 美国队长 (Marvel)

## 🔧 开发说明

### 项目结构
```
ai-cosplay-fusion/
├── frontend/                 # Next.js前端
│   ├── app/                 # App Router
│   ├── components/          # React组件
│   └── package.json
├── backend/                 # Flask后端
│   ├── services/            # 业务服务
│   ├── app.py              # 主应用
│   └── requirements.txt
└── README.md
```

### 核心服务
- `ImageProcessor`: 图像处理和人物抠图
- `CharacterRecognizer`: 角色识别（MVP版本）
- `BackgroundGenerator`: 背景生成
- `ImageBlender`: 图像融合

## 🚧 开发计划

### MVP版本 ✅
- [x] 基础文件上传和前端界面
- [x] 人物抠图功能
- [x] 预设角色识别
- [x] 背景生成和图像融合

### 下一版本 🚀
- [ ] 集成真正的AI角色识别模型
- [ ] 优化光线和色彩融合算法
- [ ] 增加更多角色支持
- [ ] 添加批量处理功能
- [ ] 实现用户账户系统

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📞 联系方式

如有问题或建议，请通过Issue联系我们。
