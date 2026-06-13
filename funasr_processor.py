from funasr import AutoModel
import torch

class FunASRProcessor:
    def __init__(self, device="cuda"):
        print("🚀 加载 FunASR 模型（首次较慢）...")
        self.model = AutoModel(
            model="iic/SenseVoiceSmall",
            vad_model="fsmn-vad",
            spk_model="cam++",
            device=device
        )
        print("✅ 模型加载完成")

    def process_audio(self, audio_path):
        result = self.model.generate(
            input=audio_path,
            batch_size_s=300,
            hotword=""
        )
        
        sentences = result[0].get("sentence_info", []) if isinstance(result, list) else result.get("sentence_info", [])
        
        processed = []
        for sent in sentences:
            spk = sent.get("spk", 0)
            start = sent.get("start", 0) / 1000.0
            end = sent.get("end", 0) / 1000.0
            text = sent.get("text", "").strip()
            processed.append({
                "speaker": f"说话人 {spk}",
                "start": start,
                "end": end,
                "text": text
            })
        return processed