from fpdf import FPDF
from .base_dispatch import NewsDispatcher

class PDFDispatcher(NewsDispatcher):
    def __init__(self, filename="report.pdf"):
        self.filename = filename

    def dispatch(self, report):
        try:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.set_font("Arial", size=12)

            for line in report.split("\n"):
                pdf.multi_cell(0, 10, txt=line)

            pdf.output(self.filename)
            print(f"PDF report saved to {self.filename}")
        except Exception as e:
            print(f"Failed to create PDF: {e}")
