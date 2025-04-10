import gradio as gr
print(gr.__version__)

from main import process_resume
from utils import export_resume

with gr.Blocks() as app:
    gr.Markdown(
    """
    ## Resume Optimizer
    Upload your resume, paste job description and get actionable insights!
    """)

    with gr.Row():
        resume = gr.File(label="Upload Your Resume (.md)")
        job_desc = gr.Textbox(label="Paste your job description here", lines = 9, interactive = True, placeholder="Paste job description...")
    run_button = gr.Button("Optmize Resume 🚀")

    output_resume_md = gr.Markdown(label="New Resume")
    output_suggestions = gr.Markdown(label="suggestions")   
    
    output_resume = gr.Textbox(label="Edit resume and import", interactive= True)
    export_button = gr.Button("Export resume as PDF 📲")
    export_result = gr.Markdown(label="Export Result")

    run_button.click(process_resume, inputs=[resume, job_desc], outputs=[output_resume_md, output_resume, output_suggestions])
    export_button.click(export_resume, inputs=[output_resume], outputs=[export_result])



app.launch()