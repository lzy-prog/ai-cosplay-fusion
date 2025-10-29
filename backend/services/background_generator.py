import logging
import os
import requests
from PIL import Image
import io
from typing import Optional

logger = logging.getLogger(__name__)

class BackgroundGenerator:
    """背景生成服务类"""
    
    def __init__(self):
        """初始化背景生成器"""
        # 使用Hugging Face的Stable Diffusion API
        self.api_url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
        self.api_token = os.getenv('HUGGINGFACE_API_TOKEN')
        
        # 如果没有API token，使用本地生成的示例背景
        self.use_local_fallback = not self.api_token
        
        logger.info(f"背景生成器初始化完成，使用{'本地回退' if self.use_local_fallback else 'Hugging Face API'}")
    
    def generate_background(self, character_name: str, width: int = 1024, height: int = 1024) -> Image.Image:
        """
        根据角色生成背景图片
        
        Args:
            character_name (str): 角色名称
            width (int): 图片宽度
            height (int): 图片高度
            
        Returns:
            PIL.Image: 生成的背景图片
        """
        try:
            if self.use_local_fallback:
                return self._generate_local_background(character_name, width, height)
            else:
                return self._generate_api_background(character_name, width, height)
                
        except Exception as e:
            logger.error(f"背景生成失败: {str(e)}")
            # 返回默认背景
            return self._generate_default_background(width, height)
    
    def _generate_api_background(self, character_name: str, width: int, height: int) -> Image.Image:
        """使用API生成背景"""
        try:
            # 构建提示词
            prompt = self._build_prompt(character_name)
            
            # API请求参数
            payload = {
                "inputs": prompt,
                "parameters": {
                    "width": width,
                    "height": height,
                    "num_inference_steps": 20,
                    "guidance_scale": 7.5
                }
            }
            
            headers = {
                "Authorization": f"Bearer {self.api_token}",
                "Content-Type": "application/json"
            }
            
            # 发送请求
            response = requests.post(self.api_url, json=payload, headers=headers)
            
            if response.status_code == 200:
                # 将响应转换为图片
                image_data = response.content
                image = Image.open(io.BytesIO(image_data))
                logger.info("API背景生成成功")
                return image
            else:
                logger.warning(f"API请求失败: {response.status_code}")
                return self._generate_local_background(character_name, width, height)
                
        except Exception as e:
            logger.error(f"API背景生成失败: {str(e)}")
            return self._generate_local_background(character_name, width, height)
    
    def _generate_local_background(self, character_name: str, width: int, height: int) -> Image.Image:
        """生成本地背景（回退方案）"""
        try:
            # 根据角色生成不同的背景
            if '皮卡丘' in character_name:
                return self._create_pokemon_background(width, height)
            elif '鸣人' in character_name:
                return self._create_naruto_background(width, height)
            elif '蜘蛛侠' in character_name:
                return self._create_spiderman_background(width, height)
            elif '蝙蝠侠' in character_name:
                return self._create_batman_background(width, height)
            else:
                return self._create_default_background(width, height)
                
        except Exception as e:
            logger.error(f"本地背景生成失败: {str(e)}")
            return self._create_default_background(width, height)
    
    def _build_prompt(self, character_name: str) -> str:
        """构建背景生成提示词"""
        prompts = {
            '皮卡丘': 'A magical Pokemon forest with electric sparks, cherry blossoms, mystical atmosphere, anime style, high quality, detailed',
            '鸣人': 'Hidden Leaf Village with traditional Japanese architecture, cherry blossoms, ninja scrolls, anime style, detailed',
            '孙悟空': 'Dragon Ball world with floating islands, energy orbs, mystical mountains, anime style, epic',
            '蜘蛛侠': 'New York City skyline at sunset, skyscrapers, web-swinging perspective, comic book style, dynamic',
            '蝙蝠侠': 'Gothic Gotham City at night, dark alleys, bat signal in sky, noir atmosphere, cinematic',
            '超人': 'Metropolis cityscape with flying perspective, clouds, heroic atmosphere, comic book style',
            '米老鼠': 'Disney magical kingdom with castle, fireworks, fairy tale atmosphere, cartoon style, colorful',
            '艾莎': 'Frozen ice palace with snowflakes, aurora borealis, magical ice crystals, Disney style, enchanting',
            '钢铁侠': 'Stark Tower with futuristic technology, holographic displays, city skyline, sci-fi atmosphere',
            '美国队长': 'Patriotic battlefield with American flag, heroic atmosphere, comic book style, dynamic action'
        }
        
        return prompts.get(character_name, 'Fantasy landscape with magical atmosphere, high quality, detailed')
    
    def _create_pokemon_background(self, width: int, height: int) -> Image.Image:
        """创建皮卡丘主题背景"""
        from PIL import ImageDraw
        
        # 创建渐变背景
        image = Image.new('RGB', (width, height), (135, 206, 235))  # 天蓝色
        draw = ImageDraw.Draw(image)
        
        # 添加渐变效果
        for y in range(height):
            color_value = int(135 + (y / height) * 100)  # 从浅蓝到深蓝
            draw.line([(0, y), (width, y)], fill=(color_value, 206, 235))
        
        return image
    
    def _create_naruto_background(self, width: int, height: int) -> Image.Image:
        """创建火影忍者主题背景"""
        from PIL import ImageDraw
        
        # 创建日式风格背景
        image = Image.new('RGB', (width, height), (255, 248, 220))  # 米色
        draw = ImageDraw.Draw(image)
        
        # 添加渐变效果
        for y in range(height):
            color_value = int(255 - (y / height) * 50)  # 从浅到深
            draw.line([(0, y), (width, y)], fill=(color_value, 248, 220))
        
        return image
    
    def _create_spiderman_background(self, width: int, height: int) -> Image.Image:
        """创建蜘蛛侠主题背景"""
        from PIL import ImageDraw
        
        # 创建城市夜景背景
        image = Image.new('RGB', (width, height), (25, 25, 112))  # 深蓝色
        draw = ImageDraw.Draw(image)
        
        # 添加渐变效果
        for y in range(height):
            color_value = int(25 + (y / height) * 100)  # 从深蓝到浅蓝
            draw.line([(0, y), (width, y)], fill=(color_value, color_value, 112))
        
        return image
    
    def _create_batman_background(self, width: int, height: int) -> Image.Image:
        """创建蝙蝠侠主题背景"""
        from PIL import ImageDraw
        
        # 创建哥特式背景
        image = Image.new('RGB', (width, height), (47, 79, 79))  # 深灰色
        draw = ImageDraw.Draw(image)
        
        # 添加渐变效果
        for y in range(height):
            color_value = int(47 + (y / height) * 80)  # 从深灰到浅灰
            draw.line([(0, y), (width, y)], fill=(color_value, color_value, color_value))
        
        return image
    
    def _create_default_background(self, width: int, height: int) -> Image.Image:
        """创建默认背景"""
        from PIL import ImageDraw
        
        # 创建简单的渐变背景
        image = Image.new('RGB', (width, height), (240, 248, 255))  # 浅蓝色
        draw = ImageDraw.Draw(image)
        
        # 添加渐变效果
        for y in range(height):
            color_value = int(240 - (y / height) * 50)  # 从浅到深
            draw.line([(0, y), (width, y)], fill=(color_value, 248, 255))
        
        return image
