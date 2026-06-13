# FunASR 说话人区分 Demo（公安项目推荐）

## 功能
- 麦克风实时录音 + 说话人自动区分（A/B/C）
- 中文语音转写（FunASR SenseVoice + cam++）
- 生成带时间戳的结构化笔录
- 全离线部署，适合公安/政务场景

## 新增功能
- **Gradio 实时 Web UI**：`python gradio_app.py`
- **Word 专业笔录导出**：自动生成格式化 .docx
- **Docker 支持**：一键部署
- **声纹注册模块**：speaker_registration.py

## 快速开始

1. 安装依赖
```bash
pip install -r requirements.txt
```

2. 运行 Gradio UI（推荐）
```bash
python gradio_app.py
```

访问 http://localhost:7860 使用

## Docker 部署
```bash
docker build -t funasr-demo .
docker run -p 7860:7860 --gpus all funasr-demo
```

公安项目基础完善，可快速迭代。