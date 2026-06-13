from audio_capture import record_audio
from funasr_processor import FunASRProcessor
from utils import map_speakers, print_and_save_transcript
import argparse
import os
import torch

def main():
    parser = argparse.ArgumentParser(description="FunASR 说话人区分 Demo")
    parser.add_argument("--mode", choices=["record", "file"], default="record", help="record 或 file 模式")
    parser.add_argument("--file", type=str, help="已有音频文件路径")
    parser.add_argument("--duration", type=int, default=15, help="录制时长（秒）")
    args = parser.parse_args()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"使用设备: {device}")
    processor = FunASRProcessor(device=device)

    if args.mode == "record":
        audio_file = record_audio(duration=args.duration)
    else:
        audio_file = args.file
        if not os.path.exists(audio_file):
            print(f"❌ 文件不存在: {audio_file}")
            return

    print("🔍 开始说话人区分 + 语音转写...")
    results = processor.process_audio(audio_file)
    
    if not results:
        print("⚠️ 未检测到语音内容")
        return
    
    spk_map = map_speakers(results)
    print_and_save_transcript(results, spk_map)

if __name__ == "__main__":
    main()