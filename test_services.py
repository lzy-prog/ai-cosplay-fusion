#!/usr/bin/env python3
"""
AI角色扮演场景融合器测试脚本
"""

import os
import sys
import logging
from PIL import Image, ImageDraw
import numpy as np

# 添加backend目录到Python路径
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from services.character_recognizer import CharacterRecognizer
from services.background_generator import BackgroundGenerator
from services.image_blender import ImageBlender

def create_test_image():
    """创建一个测试用的角色扮演图片"""
    # 创建一个简单的测试图片
    width, height = 400, 600
    
    # 创建白色背景
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)
    
    # 绘制一个简单的人物轮廓（皮卡丘风格）
    # 头部（黄色圆形）
    draw.ellipse([150, 50, 250, 150], fill='yellow', outline='black', width=2)
    
    # 身体（黄色椭圆）
    draw.ellipse([140, 150, 260, 300], fill='yellow', outline='black', width=2)
    
    # 耳朵（黄色三角形）
    draw.polygon([(160, 50), (180, 20), (200, 50)], fill='yellow', outline='black', width=2)
    draw.polygon([(200, 50), (220, 20), (240, 50)], fill='yellow', outline='black', width=2)
    
    # 眼睛
    draw.ellipse([170, 80, 185, 95], fill='black')
    draw.ellipse([215, 80, 230, 95], fill='black')
    
    # 嘴巴
    draw.arc([180, 100, 220, 120], 0, 180, fill='black', width=2)
    
    # 手臂
    draw.ellipse([100, 180, 140, 220], fill='yellow', outline='black', width=2)
    draw.ellipse([260, 180, 300, 220], fill='yellow', outline='black', width=2)
    
    # 腿部
    draw.ellipse([160, 300, 200, 380], fill='yellow', outline='black', width=2)
    draw.ellipse([200, 300, 240, 380], fill='yellow', outline='black', width=2)
    
    return image

def test_services():
    """测试各个服务"""
    print("🧪 开始测试AI角色扮演场景融合器服务...")
    
    try:
        # 测试角色识别器
        print("\n1️⃣ 测试角色识别器...")
        recognizer = CharacterRecognizer()
        characters = recognizer.get_supported_characters()
        print(f"✅ 支持的角色: {', '.join(characters[:5])}...")
        
        # 测试背景生成器
        print("\n2️⃣ 测试背景生成器...")
        generator = BackgroundGenerator()
        test_bg = generator.generate_background('皮卡丘', 400, 400)
        print(f"✅ 背景生成成功，尺寸: {test_bg.size}")
        
        # 测试图像融合器
        print("\n3️⃣ 测试图像融合器...")
        blender = ImageBlender()
        
        # 创建测试图片
        test_image = create_test_image()
        print(f"✅ 测试图片创建成功，尺寸: {test_image.size}")
        
        # 测试融合
        result = blender.blend_images(test_image, test_bg)
        print(f"✅ 图像融合成功，结果尺寸: {result.size}")
        
        # 保存测试结果
        test_image.save('test_character.png')
        test_bg.save('test_background.png')
        result.save('test_result.png')
        
        print("\n🎉 所有测试通过！")
        print("📁 测试文件已保存:")
        print("   - test_character.png (测试角色图片)")
        print("   - test_background.png (生成的背景)")
        print("   - test_result.png (融合结果)")
        
        return True
        
    except Exception as e:
        print(f"\n❌ 测试失败: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_services()
    sys.exit(0 if success else 1)
