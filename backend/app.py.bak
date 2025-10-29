from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import time
import base64
from PIL import Image
import io
import logging

# 创建Flask应用
app = Flask(__name__)
CORS(app)

# 日志配置
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 创建上传和结果目录
UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# 预设角色列表
CHARACTERS = {
    '皮卡丘': {
        'prompt': 'A magical Pokemon forest with electric sparks, cherry blossoms, mystical atmosphere, anime style, high quality'
    },
    '鸣人': {
        'prompt': 'Hidden Leaf Village with traditional Japanese architecture, cherry blossoms, ninja scrolls, anime style'
    },
    '蜘蛛侠': {
        'prompt': 'New York City skyline at sunset, skyscrapers, web-swinging perspective, comic book style, dynamic'
    }
}

@app.route('/api/health', methods=['GET'])
def health_check():
    """健康检查"""
    return jsonify({
        'status': 'healthy',
        'message': 'AI Cosplay Fusion API is running (Lite Mode)'
    })

@app.route('/api/process-image', methods=['POST'])
def process_image():
    """处理图片（简化版本）"""
    try:
        # 检查是否有文件
        if 'image' not in request.files:
            return jsonify({'error': '没有上传图片'}), 400
        
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': '没有选择文件'}), 400
        
        # 保存图片
        filename = f"upload_{int(time.time())}.jpg"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        logger.info(f"图片已保存: {filepath}")
        
        # 读取图片
        image = Image.open(filepath)
        
        # 模拟角色识别（随机选择一个）
        import random
        character = random.choice(list(CHARACTERS.keys()))
        logger.info(f"识别到角色: {character}")
        
        # 创建一个简单的渐变背景
        bg_width, bg_height = image.size
        background = Image.new('RGB', (bg_width, bg_height), (135, 206, 235))  # 天蓝色
        
        # 简单融合：使用原始图片（模拟AI处理效果）
        result_image = image
        
        # 保存结果
        result_filename = f"result_{int(time.time())}.png"
        result_path = os.path.join(RESULT_FOLDER, result_filename)
        result_image.save(result_path)
        
        # 转换为base64
        result_buffer = io.BytesIO()
        result_image.save(result_buffer, format='PNG')
        result_base64 = base64.b64encode(result_buffer.getvalue()).decode()
        
        # 清理临时文件
        os.remove(filepath)
        
        return jsonify({
            'success': True,
            'character': character,
            'resultImage': f'data:image/png;base64,{result_base64}',
            'message': '处理完成（Lite模式）'
        })
        
    except Exception as e:
        logger.error(f"处理图片时出错: {str(e)}")
        return jsonify({
            'error': f'处理失败: {str(e)}'
        }), 500

@app.route('/api/characters', methods=['GET'])
def get_characters():
    """获取支持的角色列表"""
    return jsonify({
        'characters': list(CHARACTERS.keys())
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
