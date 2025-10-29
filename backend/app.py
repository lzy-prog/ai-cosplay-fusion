from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import base64

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# 一个1x1像素的透明PNG图片（base64编码）
TINY_IMAGE = 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg=='

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
        
        # 读取文件（只是验证文件存在，不处理）
        file_data = file.read()
        
        if len(file_data) == 0:
            return jsonify({'error': '文件为空'}), 400
        
        # 模拟角色识别
        characters = ['皮卡丘', '鸣人', '蜘蛛侠', '蝙蝠侠', '超人', '钢铁侠', '美国队长']
        import random
        character = random.choice(characters)
        
        # 返回一个简单的演示图片
        # 在实际应用中，这里会进行AI处理
        return jsonify({
            'success': True,
            'character': character,
            'resultImage': f'data:image/png;base64,{TINY_IMAGE}',
            'message': f'已识别角色：{character}（演示模式）'
        })
        
    except Exception as e:
        return jsonify({'error': f'处理失败: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=False)
