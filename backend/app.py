from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import time
import base64
import io
from PIL import Image

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'message': 'Backend is running'})

@app.route('/api/process-image', methods=['POST'])
def process():
    try:
        if 'image' not in request.files:
            return jsonify({'error': '没有上传图片'}), 400
        
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': '没有选择文件'}), 400
        
        # 读取图片
        image = Image.open(file.stream)
        
        # 创建结果（这里简单返回原图，实际应该有AI处理）
        result_buffer = io.BytesIO()
        image.save(result_buffer, format='PNG')
        result_base64 = base64.b64encode(result_buffer.getvalue()).decode()
        
        # 模拟角色识别
        characters = ['皮卡丘', '鸣人', '蜘蛛侠', '蝙蝠侠', '超人']
        import random
        character = random.choice(characters)
        
        return jsonify({
            'success': True,
            'character': character,
            'resultImage': f'data:image/png;base64,{result_base64}',
            'message': '处理完成'
        })
        
    except Exception as e:
        return jsonify({'error': f'处理失败: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=False)
