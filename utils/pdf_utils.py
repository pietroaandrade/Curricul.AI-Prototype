from markdown import markdown
from weasyprint import HTML

def export_resume(new_resume: str, output_path="resumes/optimized_resume.pdf") -> str:
    try:
        html_content = markdown(new_resume)
        HTML(string=html_content).write_pdf(output_path)
        return f"Successfully exported resume to {output_path} 🎉"
    except Exception as e:
        return f"Failed to export resume: {str(e)} 💔"
