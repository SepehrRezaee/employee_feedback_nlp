from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Employee Feedback NLP Analysis - Project Report', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

def create_report():
    pdf = PDF()
    pdf.add_page()
    
    # Title
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Executive Summary', 0, 1, 'L')
    
    # Body
    pdf.set_font('Arial', '', 11)
    intro = (
        "I built this project to automate the analysis of employee feedback. "
        "Understanding employee sentiment and stress levels is crucial for maintaining a healthy workplace culture. "
        "This tool processes raw text feedback to extract actionable insights for HR and management."
    )
    pdf.multi_cell(0, 7, intro)
    pdf.ln(5)
    
    # Methodology
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Methodology & Pipeline', 0, 1, 'L')
    pdf.set_font('Arial', '', 11)
    methodology = (
        "My NLP pipeline is designed to be lightweight and effective, running locally without external API dependencies. "
        "It consists of the following components:\n"
        "- Sentiment Analysis: Using VADER to quantify positive and negative sentiment.\n"
        "- Stress Estimation: A custom heuristic combining sentiment scores with burnout-related keywords.\n"
        "- Topic Extraction: Utilizing NMF (Non-negative Matrix Factorization) to identify emerging themes.\n"
        "- Summarization: Extractive summarization via LSA (Latent Semantic Analysis).\n"
        "- Recommendations: An automated tagging system that suggests HR actions (e.g., 'Wellness Check')."
    )
    pdf.multi_cell(0, 7, methodology)
    pdf.ln(5)
    
    # Results
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Key Results', 0, 1, 'L')
    pdf.set_font('Arial', '', 11)
    results = (
        "I tested the pipeline on a dataset of 10 sample employee messages. The system successfully flagged "
        "critical issues such as 'unmanageable workload' and 'impossible deadlines' with high stress scores (0.90). "
        "It also correctly identified positive feedback regarding the 'remote work policy' and 'mentorship program'."
    )
    pdf.multi_cell(0, 7, results)
    pdf.ln(5)
    
    # Conclusion
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Conclusion', 0, 1, 'L')
    pdf.set_font('Arial', '', 11)
    conclusion = (
        "This project demonstrates how standard NLP techniques can be applied to solve real-world HR challenges. "
        "The automated tagging system provides immediate visibility into team morale and potential burnout risks."
    )
    pdf.multi_cell(0, 7, conclusion)
    pdf.ln(10)
    
    # Link
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Project Repository', 0, 1, 'L')
    pdf.set_font('Arial', 'U', 11)
    pdf.set_text_color(0, 0, 255)
    link = "https://github.com/SepehrRezaee/employee_feedback_nlp/tree/main"
    pdf.cell(0, 10, link, 0, 1, 'L', link=link)
    
    pdf.output('project_report.pdf', 'F')
    print("Report generated successfully: project_report.pdf")

if __name__ == '__main__':
    create_report()
