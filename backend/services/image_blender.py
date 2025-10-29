import logging
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
import cv2
from typing import Tuple

logger = logging.getLogger(__name__)

class ImageBlender:
    """图像融合服务类"""
    
    def __init__(self):
        """初始化图像融合器"""
        logger.info("图像融合器初始化完成")
    
    def blend_images(self, foreground: Image.Image, background: Image.Image) -> Image.Image:
        """
        将前景人物与背景进行融合
        
        Args:
            foreground (PIL.Image): 前景人物图片（带透明通道）
            background (PIL.Image): 背景图片
            
        Returns:
            PIL.Image: 融合后的图片
        """
        try:
            # 确保背景图片大小合适
            background = self._resize_background(background, foreground.size)
            
            # 调整前景图片的光线和色彩
            enhanced_foreground = self._enhance_foreground(foreground, background)
            
            # 进行图像融合
            blended_image = self._blend_with_lighting(enhanced_foreground, background)
            
            # 后处理优化
            final_image = self._post_process(blended_image)
            
            logger.info("图像融合完成")
            return final_image
            
        except Exception as e:
            logger.error(f"图像融合失败: {str(e)}")
            raise
    
    def _resize_background(self, background: Image.Image, target_size: Tuple[int, int]) -> Image.Image:
        """调整背景图片大小以匹配前景"""
        # 计算缩放比例，保持宽高比
        bg_width, bg_height = background.size
        fg_width, fg_height = target_size
        
        # 计算缩放比例
        scale_w = fg_width / bg_width
        scale_h = fg_height / bg_height
        scale = max(scale_w, scale_h)  # 使用较大的缩放比例确保完全覆盖
        
        new_width = int(bg_width * scale)
        new_height = int(bg_height * scale)
        
        # 调整大小
        resized_bg = background.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # 居中裁剪
        left = (new_width - fg_width) // 2
        top = (new_height - fg_height) // 2
        right = left + fg_width
        bottom = top + fg_height
        
        return resized_bg.crop((left, top, right, bottom))
    
    def _enhance_foreground(self, foreground: Image.Image, background: Image.Image) -> Image.Image:
        """增强前景图片以匹配背景环境"""
        try:
            # 分析背景的主要颜色和亮度
            bg_colors = self._analyze_background_colors(background)
            bg_brightness = self._calculate_brightness(background)
            
            # 调整前景的亮度
            brightness_factor = self._calculate_brightness_adjustment(foreground, bg_brightness)
            enhanced = ImageEnhance.Brightness(foreground).enhance(brightness_factor)
            
            # 调整对比度
            contrast_factor = 1.1  # 稍微增加对比度
            enhanced = ImageEnhance.Contrast(enhanced).enhance(contrast_factor)
            
            # 调整饱和度
            saturation_factor = 1.05  # 稍微增加饱和度
            enhanced = ImageEnhance.Color(enhanced).enhance(saturation_factor)
            
            # 添加轻微的锐化
            enhanced = enhanced.filter(ImageFilter.UnsharpMask(radius=1, percent=150, threshold=3))
            
            return enhanced
            
        except Exception as e:
            logger.error(f"前景增强失败: {str(e)}")
            return foreground
    
    def _blend_with_lighting(self, foreground: Image.Image, background: Image.Image) -> Image.Image:
        """考虑光照效果的图像融合"""
        try:
            # 转换为RGBA模式
            if foreground.mode != 'RGBA':
                foreground = foreground.convert('RGBA')
            if background.mode != 'RGB':
                background = background.convert('RGB')
            
            # 创建新的图片
            result = Image.new('RGB', background.size)
            
            # 获取像素数据
            fg_pixels = np.array(foreground)
            bg_pixels = np.array(background)
            
            # 创建结果像素数组
            result_pixels = np.zeros_like(bg_pixels, dtype=np.float32)
            
            # 逐像素融合
            for y in range(fg_pixels.shape[0]):
                for x in range(fg_pixels.shape[1]):
                    fg_pixel = fg_pixels[y, x]
                    bg_pixel = bg_pixels[y, x]
                    
                    # 获取alpha通道值
                    alpha = fg_pixel[3] / 255.0
                    
                    if alpha > 0:  # 如果前景像素不透明
                        # 计算融合后的颜色
                        for c in range(3):  # RGB三个通道
                            # 使用alpha混合
                            result_pixels[y, x, c] = (
                                fg_pixel[c] * alpha + 
                                bg_pixel[c] * (1 - alpha)
                            )
                    else:  # 如果前景像素透明
                        result_pixels[y, x] = bg_pixel
            
            # 转换回PIL Image
            result_pixels = np.clip(result_pixels, 0, 255).astype(np.uint8)
            result = Image.fromarray(result_pixels)
            
            return result
            
        except Exception as e:
            logger.error(f"光照融合失败: {str(e)}")
            # 回退到简单融合
            return self._simple_blend(foreground, background)
    
    def _simple_blend(self, foreground: Image.Image, background: Image.Image) -> Image.Image:
        """简单的图像融合（回退方案）"""
        if foreground.mode != 'RGBA':
            foreground = foreground.convert('RGBA')
        if background.mode != 'RGB':
            background = background.convert('RGB')
        
        # 使用PIL的paste方法进行融合
        result = background.copy()
        result.paste(foreground, (0, 0), foreground)
        
        return result
    
    def _analyze_background_colors(self, background: Image.Image) -> dict:
        """分析背景的主要颜色"""
        try:
            # 转换为numpy数组
            img_array = np.array(background)
            
            # 计算平均颜色
            mean_colors = np.mean(img_array, axis=(0, 1))
            
            return {
                'mean_r': mean_colors[0],
                'mean_g': mean_colors[1],
                'mean_b': mean_colors[2],
                'dominant_color': tuple(mean_colors.astype(int))
            }
        except Exception as e:
            logger.error(f"背景颜色分析失败: {str(e)}")
            return {'mean_r': 128, 'mean_g': 128, 'mean_b': 128}
    
    def _calculate_brightness(self, image: Image.Image) -> float:
        """计算图片的平均亮度"""
        try:
            # 转换为灰度图
            gray = image.convert('L')
            gray_array = np.array(gray)
            
            # 计算平均亮度
            brightness = np.mean(gray_array)
            return brightness / 255.0  # 归一化到0-1
            
        except Exception as e:
            logger.error(f"亮度计算失败: {str(e)}")
            return 0.5
    
    def _calculate_brightness_adjustment(self, foreground: Image.Image, target_brightness: float) -> float:
        """计算前景亮度调整因子"""
        try:
            current_brightness = self._calculate_brightness(foreground)
            
            # 计算调整因子
            if current_brightness > 0:
                adjustment = target_brightness / current_brightness
                # 限制调整范围
                adjustment = max(0.7, min(1.3, adjustment))
            else:
                adjustment = 1.0
            
            return adjustment
            
        except Exception as e:
            logger.error(f"亮度调整计算失败: {str(e)}")
            return 1.0
    
    def _post_process(self, image: Image.Image) -> Image.Image:
        """后处理优化"""
        try:
            # 轻微的色彩增强
            enhanced = ImageEnhance.Color(image).enhance(1.05)
            
            # 轻微的锐化
            sharpened = enhanced.filter(ImageFilter.UnsharpMask(radius=1, percent=120, threshold=3))
            
            return sharpened
            
        except Exception as e:
            logger.error(f"后处理失败: {str(e)}")
            return image
