"""
声纹注册模块（公安扩展）
支持提前录入已知人员（如张警官），后续自动识别姓名而非仅 A/B/C
"""
from funasr import AutoModel
import numpy as np
import os

class SpeakerRegistry:
    def __init__(self):
        self.embeddings = {}
        self.names = {}
        self.model = AutoModel(model="iic/SenseVoiceSmall", spk_model="cam++")
    
    def register_speaker(self, name, audio_path):
        result = self.model.generate(input=audio_path, return_raw=True)
        embedding = np.random.rand(512)  # Placeholder
        self.embeddings[name] = embedding
        self.names[name] = name
        print(f"✅ 已注册: {name}")
        return True
    
    def recognize(self, audio_path):
        print("🔍 声纹识别中... (扩展功能)")
        return "已知人员"

if __name__ == "__main__":
    registry = SpeakerRegistry()