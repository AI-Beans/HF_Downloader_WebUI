
# 🌟 HF_Downloader_WebUI🌟

## 📝 简介
这个工具帮助您从中国大陆 HuggingFace 下载模型、数据集，可以选择下载所有文件或者自定义下载过滤选项。

## ⚙️ 功能
- 下载 HuggingFace 模型
- 支持使用过滤选项自定义下载内容
- 断点续传功能，防止下载中断

## 🚀 快速开始

1. 克隆这个仓库到你的本地机器：
   ```bash
   git clone https://github.com/yourusername/huggingface-model-downloader.git
   ```

2. 进入项目目录并安装依赖：
   ```bash
   cd huggingface-model-downloader
   pip install -r requirements.txt
   ```

3. 运行应用：
   ```bash
   python main.py
   ```

## 🛠️ 使用说明

1. 输入模型名称和 HuggingFace 的 token。
2. 选择“下载所有文件”或自定义下载选项：
   - 当勾选“下载所有文件”时，所有文件将被下载。
   - 当取消勾选时，可以设置 `Allow Patterns` 和 `Ignore Patterns` 来过滤下载内容。
3. 点击“下载”按钮开始下载。

### 🎨 示例界面
![示例界面](https://path-to-your-screenshot.png)

## 📜 许可证
这个项目遵循 [MIT 许可证](LICENSE)。

## 🤝 贡献
欢迎提出问题和贡献代码！请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 获取更多信息。

## 💬 联系我们
如果有任何问题，请通过 [email@example.com](mailto:email@example.com) 联系我们。
