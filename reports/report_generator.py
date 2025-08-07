# reports/report_generator.py

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os

def generate_report(content, output_path="news_report.pdf"):
    doc = SimpleDocTemplate(output_path, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    for line in content.split("\n"):
        story.append(Paragraph(line, styles["Normal"]))
        story.append(Spacer(1, 12))

    try:
        doc.build(story)
        print(f"[✓] PDF generated at: {os.path.abspath(output_path)}")
    except Exception as e:
        print(f"[x] Failed to generate PDF: {e}")
