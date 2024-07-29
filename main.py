import os
import gradio as gr
from huggingface_hub import snapshot_download

# 设置为hf的国内镜像网站
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

def download_model(model_name, token, allow_patterns, ignore_patterns, download_all):
    while True:
        try:
            if download_all:
                allow_patterns = None
                ignore_patterns = None
            else:
                allow_patterns = allow_patterns.split(",") if allow_patterns else None
                ignore_patterns = ignore_patterns.split(",") if ignore_patterns else None
            
            snapshot_download(
                repo_id=model_name,
                local_dir_use_symlinks=True,  # 在local-dir指定的目录中都是一些“链接文件”
                local_dir=model_name,
                token=token,  # huggingface的token
                resume_download=True,
                allow_patterns=allow_patterns,
                ignore_patterns=ignore_patterns
            )
            return f"Model {model_name} downloaded successfully!"
        except Exception as e:
            pass

def gradio_interface(model_name, token, allow_patterns, ignore_patterns, download_all):
    result = download_model(model_name, token, allow_patterns, ignore_patterns, download_all)
    return result

def update_visibility(download_all):
    if download_all:
        return gr.update(visible=False), gr.update(visible=False)
    else:
        return gr.update(visible=True, value="*.md,*.json"), gr.update(visible=True, value="*vocab.json")

# 创建Gradio界面
with gr.Blocks() as iface:
    gr.Markdown("# HuggingFace Model Downloader")
    gr.Markdown("1.Enter the model name and your HuggingFace token to download the model. You can customize the download patterns or download all files.")  
    with gr.Row():
        model_name = gr.Textbox(lines=1, placeholder="Enter Model Name", label="Model Name")
        token = gr.Textbox(lines=1, placeholder="Enter Token", label="Token", type="password")
    with gr.Column():
        gr.Markdown("2.When checked, all files will be downloaded. When unchecked, filtering options will be applied.")
        download_all = gr.Checkbox(label="Download All Files", value=True)  
        allow_patterns = gr.Textbox(lines=1, placeholder="Enter Allow Patterns (comma separated)", label="Allow Patterns", value="*.md,*.json", visible=False)
        ignore_patterns = gr.Textbox(lines=1, placeholder="Enter Ignore Patterns (comma separated)", label="Ignore Patterns", value="*vocab.json", visible=False)

    gr.Markdown("3.Output Result Print")  
    output = gr.Textbox(label="Output")

    download_all.change(fn=update_visibility, inputs=download_all, outputs=[allow_patterns, ignore_patterns])

    download_button = gr.Button("Download")
    download_button.click(gradio_interface, inputs=[model_name, token, allow_patterns, ignore_patterns, download_all], outputs=output)

if __name__ == "__main__":
    iface.launch()
