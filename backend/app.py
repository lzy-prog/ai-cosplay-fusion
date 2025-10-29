from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import io
import base64
import time
from PIL import Image
import numpy as np
import cv2
from dotenv import load_dotenv
import logging

# 导入自定义模块
from services.image_processor import ImageProcessor
from services.character_recognizer import CharacterRecognizer
from services.background_generator import BackgroundGenerator
from services.image_blender import ImageBlender

# 加载环境变量
load_dotenv()

app = Flask(__name__)
CORS(app)

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 创建服务实例
image_processor = ImageProcessor()
character_recognizer = CharacterRecognizer()
background_generator = BackgroundGenerator()
image_blender = ImageBlender()

# 确保上传目录存在
UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route('/api/health', methods=['GET'])
def health_check():
    """健康检查端点"""
    return jsonify({
        'status': 'healthy',
        'message': 'AI Cosplay Fusion API is running'
    })

@app.route('/api/process-image', methods=['POST'])
def process_image():
    """处理图片的主要端点"""
    try:
        # 检查是否有文件上传
        if 'image' not in request.files:
            return jsonify({'error': '没有上传图片'}), 400
        
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': '没有选择文件'}), 400
        
        # 保存上传的图片
        filename = f"upload_{int(time.time())}.jpg"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        
        logger.info(f"图片已保存: {filepath}")
        
        # 步骤1: 角色识别
        logger.info("开始角色识别...")
        character = character_recognizer.recognize_character(filepath)
        logger.info(f"识别到角色: {character}")
        
        # 步骤2: 背景生成
        logger.info("开始生成背景...")
        background_image = background_generator.generate_background(character)
        logger.info("背景生成完成")
        
        # 步骤3: 人物抠图
        logger.info("开始人物抠图...")
        extracted_person = image_processor.extract_person(filepath)
        logger.info("人物抠图完成")
        
        # 步骤4: 图像融合
        logger.info("开始图像融合...")
        result_image = image_blender.blend_images(extracted_person, background_image)
        logger.info("图像融合完成")
        
        # 保存结果
        result_filename = f"result_{int(time.time())}.png"
        result_path = os.path.join(RESULT_FOLDER, result_filename)
        result_image.save(result_path)
        
        # 将结果转换为base64
        result_buffer = io.BytesIO()
        result_image.save(result_buffer, format='PNG')
        result_base64 = base64.b64encode(result_buffer.getvalue()).decode()
        
        # 清理临时文件
        os.remove(filepath)
        
        return jsonify({
            'success': True,
            'character': character,
            'resultImage': f'data:image/png;base64,{result_base64}',
            'message': '处理完成'
        })
        
    except Exception as e:
        logger.error(f"处理图片时出错: {str(e)}")
        return jsonify({
            'error': f'处理失败: {str(e)}'
        }), 500

@app.route('/api/characters', methods=['GET'])
def get_characters():
    """获取支持的角色列表"""
    characters = character_recognizer.get_supported_characters()
    return jsonify({
        'characters': characters
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
