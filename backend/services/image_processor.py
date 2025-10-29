import os
import cv2
import numpy as np
from PIL import Image
import logging
from rembg import remove, new_session
import io

logger = logging.getLogger(__name__)

class ImageProcessor:
    """图像处理服务类"""
    
    def __init__(self):
        """初始化图像处理器"""
        # 初始化rembg会话
        self.session = new_session('u2net')
        logger.info("图像处理器初始化完成")
    
    def extract_person(self, image_path):
        """
        从图片中提取人物主体
        
        Args:
            image_path (str): 输入图片路径
            
        Returns:
            PIL.Image: 提取的人物图像（带透明背景）
        """
        try:
            # 读取图片
            with open(image_path, 'rb') as f:
                input_image = f.read()
            
            # 使用rembg进行背景移除
            output_image = remove(input_image, session=self.session)
            
            # 转换为PIL Image
            result_image = Image.open(io.BytesIO(output_image))
            
            # 确保是RGBA模式（带透明通道）
            if result_image.mode != 'RGBA':
                result_image = result_image.convert('RGBA')
            
            logger.info("人物抠图完成")
            return result_image
            
        except Exception as e:
            logger.error(f"人物抠图失败: {str(e)}")
            raise
    
    def resize_image(self, image, max_size=1024):
        """
        调整图片大小，保持宽高比
        
        Args:
            image (PIL.Image): 输入图片
            max_size (int): 最大尺寸
            
        Returns:
            PIL.Image: 调整后的图片
        """
        width, height = image.size
        
        if width > height:
            if width > max_size:
                new_width = max_size
                new_height = int(height * max_size / width)
            else:
                return image
        else:
            if height > max_size:
                new_height = max_size
                new_width = int(width * max_size / height)
            else:
                return image
        
        return image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    def enhance_image(self, image):
        """
        增强图片质量
        
        Args:
            image (PIL.Image): 输入图片
            
        Returns:
            PIL.Image: 增强后的图片
        """
        # 转换为numpy数组
        img_array = np.array(image)
        
        # 应用锐化滤镜
        kernel = np.array([[-1,-1,-1],
                          [-1, 9,-1],
                          [-1,-1,-1]])
        
        # 分别处理每个通道
        if len(img_array.shape) == 3:
            enhanced = np.zeros_like(img_array)
            for i in range(img_array.shape[2]):
                enhanced[:,:,i] = cv2.filter2D(img_array[:,:,i], -1, kernel)
        else:
            enhanced = cv2.filter2D(img_array, -1, kernel)
        
        # 限制像素值范围
        enhanced = np.clip(enhanced, 0, 255).astype(np.uint8)
        
        return Image.fromarray(enhanced)
    
    def adjust_lighting(self, image, brightness=1.0, contrast=1.0):
        """
        调整图片亮度和对比度
        
        Args:
            image (PIL.Image): 输入图片
            brightness (float): 亮度调整因子
            contrast (float): 对比度调整因子
            
        Returns:
            PIL.Image: 调整后的图片
        """
        # 转换为numpy数组
        img_array = np.array(image, dtype=np.float32)
        
        # 调整亮度和对比度
        img_array = img_array * contrast + (brightness - 1) * 128
        
        # 限制像素值范围
        img_array = np.clip(img_array, 0, 255).astype(np.uint8)
        
        return Image.fromarray(img_array)
