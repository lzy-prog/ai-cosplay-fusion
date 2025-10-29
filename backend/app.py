from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import time
import base64
from PIL import Image
import io
import logging

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

CHARACTERS = {
    '皮卡丘': 'Pokemon forest',
    '鸣人': 'Hidden Leaf Village',
    '蜘蛛侠': 'New York City'
}

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'message': 'AI Cosplay Fusion API'})

@app.route('/api/process-image', methods=['POST'])
def process_image():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image'}), 400
        
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No file'}), 400
        
        filename = f"upload_{int(time.time())}.jpg"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        
        image = Image.open(filepath)
        import random
        character = random.choice(list(CHARACTERS.keys()))
        
        result_buffer = io.BytesIO()
        image.save(result_buffer, format='PNG')
        result_base64 = base64.b64encode(result_buffer.getvalue()).decode()
        
        os.remove(filepath)
        
        return jsonify({
            'success': True,
            'character': character,
            'resultImage': f'data:image/png;base64,{result_base64}'
        })
        
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
