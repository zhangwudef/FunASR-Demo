import sounddevice as sd
import numpy as np
import wave
from datetime import datetime
import os

os.makedirs("recordings", exist_ok=True)

def record_audio(filename=None, duration=20, fs=16000):
    if filename is None:
        filename = f"recordings/rec_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
    
    print(f"🎤 开始录制 {duration} 秒... 说话吧（支持多人）")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()
    
    recording = np.squeeze(recording)
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(fs)
        wf.writeframes((recording * 32767).astype(np.int16).tobytes())
    
    print(f"✅ 录制完成: {filename}")
    return filename