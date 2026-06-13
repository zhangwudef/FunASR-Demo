import gradio as gr
import os
from datetime import datetime
from audio_capture import record_audio
from funasr_processor import FunASRProcessor
from utils import map_speakers, print_and_save_transcript, export_to_word

processor = None

def init_processor():
    global processor
    if processor is None:
        processor = FunASRProcessor()
    return processor

def process_recording(duration=15):
    init_processor()
    audio_file = record_audio(duration=duration)
    results = processor.process_audio(audio_file)
    spk_map = map_speakers(results)
    txt_file = f"outputs/penlu_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    print_and_save_transcript(results, spk_map, txt_file)
    
    # Export to Word
    word_file = export_to_word(results, spk_map)
    
    return txt_file, word_file, "处理完成！笔录已生成。"

def process_file(audio_file):
    init_processor()
    if audio_file is None:
        return None, None, "请上传音频文件"
    results = processor.process_audio(audio_file.name)
    spk_map = map_speakers(results)
    txt_file = f"outputs/penlu_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    print_and_save_transcript(results, spk_map, txt_file)
    word_file = export_to_word(results, spk_map)
    return txt_file, word_file, "处理完成！"

with gr.Blocks(title="FunASR 说话人区分 Demo - 公安项目") as demo:
    gr.Markdown("# 🎤 FunASR 说话人自动区分系统\n公安智能语音笔录工具")
    
    with gr.Tab("实时录音"):
        duration = gr.Slider(5, 60, value=15, step=5, label="录音时长 (秒)")
        record_btn = gr.Button("开始录音并处理", variant="primary")
        output_txt = gr.File(label="TXT 笔录")
        output_docx = gr.File(label="Word 专业笔录")
        status = gr.Textbox(label="状态")
        
        record_btn.click(process_recording, inputs=[duration], outputs=[output_txt, output_docx, status])
    
    with gr.Tab("上传音频"):
        audio_upload = gr.Audio(source="upload", type="filepath", label="上传音频文件 (wav/mp3)")
        upload_btn = gr.Button("处理音频", variant="primary")
        output_txt2 = gr.File(label="TXT 笔录")
        output_docx2 = gr.File(label="Word 专业笔录")
        status2 = gr.Textbox(label="状态")
        
        upload_btn.click(process_file, inputs=[audio_upload], outputs=[output_txt2, output_docx2, status2])

    gr.Markdown("### 注意\n- 首次加载模型需要时间\n- 支持多人对话自动区分 A/B/C\n- 输出包含时间戳和说话人标签")

if __name__ == "__main__":
    os.makedirs("outputs", exist_ok=True)
    demo.launch(server_name="0.0.0.0", server_port=7860, share=False)