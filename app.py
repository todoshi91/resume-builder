import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="1-Page ATS Resume Builder", layout="wide")

st.title("📄 1-Page ATS Resume Engine")
st.caption("Generates strictly 1-page, ATS-optimized resumes with recruiter-preferred formatting.")

# -------------------------------------------------------------
# SIDEBAR: FORMAT & PREFERENCES
# -------------------------------------------------------------
st.sidebar.header("Layout & Style")
theme_choice = st.sidebar.selectbox(
    "Choose Employer-Approved Format:",
    ["Corporate ATS Standard", "Modern Operations", "Compact Tech"]
)

# -------------------------------------------------------------
# INPUT CONTROLS (Sanitized Generic Defaults)
# -------------------------------------------------------------
with st.sidebar.expander("1. Contact Information", expanded=False):
    name = st.text_input("Full Name", "YOUR FULL NAME")
    contact_line = st.text_input("Contact Details", "City, State | +6012-345 6789 | youremail@example.com")
    linkedin = st.text_input("LinkedIn / Portfolio URL", "linkedin.com/in/your-profile")

with st.sidebar.expander("2. Professional Summary", expanded=False):
    summary_text = st.text_area(
        "Summary (Keep to 3–4 impactful lines)",
        "Results-driven IT Support and Operations Specialist with a background in Information Technology. Combines Tier-1 remote troubleshooting expertise with commercial administration, CRM tracking, and client relations experience. Fully autonomous and equipped for remote operations.",
        height=100
    )

with st.sidebar.expander("3. Core Competencies", expanded=False):
    comp_1 = st.text_input("Technical Support", "Tier-1 Troubleshooting, Remote Helpdesk Operations, Hardware & Software Diagnostics")
    comp_2 = st.text_input("Administration & Systems", "MS Office Suite (Excel, Word, PowerPoint), Order Processing, Data Verification")
    comp_3 = st.text_input("Client Operations", "Multi-channel Support (Email/Ticket/Phone), Account Maintenance, SLA Compliance")
    comp_4 = st.text_input("Languages", "Professional Working Proficiency in English and Bahasa Melayu (Written & Verbal)")

with st.sidebar.expander("4. Experience 1 (Most Recent)", expanded=False):
    exp1_company = st.text_input("Role & Company 1", "Company Name A | Sales Executive")
    exp1_dates = st.text_input("Dates 1", "April 2024 – March 2026")
    exp1_b1 = st.text_input("Bullet 1.1", "Administered commercial workflows by generating precise sales quotations, purchase orders, and technical logs.")
    exp1_b2 = st.text_input("Bullet 1.2", "Provided specialized product consultation on technical devices, coordinating setups under strict operational standards.")
    exp1_b3 = st.text_input("Bullet 1.3", "Maintained key client accounts, consistently securing renewals and supporting departmental revenue targets.")

with st.sidebar.expander("5. Experience 2", expanded=False):
    exp2_company = st.text_input("Role & Company 2", "Company Name B | Sales Representative")
    exp2_dates = st.text_input("Dates 2", "2019 – 2020")
    exp2_b1 = st.text_input("Bullet 2.1", "Handled client accounts, resolving billing discrepancies, product returns, and logistics inquiries promptly.")
    exp2_b2 = st.text_input("Bullet 2.2", "Executed daily payment collections, reconciled customer statements, and onboarded new retail accounts.")

with st.sidebar.expander("6. Experience 3 & 4", expanded=False):
    exp3_company = st.text_input("Role & Company 3", "Company Name C | Operations / Lab Assistant")
    exp3_dates = st.text_input("Dates 3", "2015 – 2019")
    exp3_b1 = st.text_input("Bullet 3.1", "Executed quality-control evaluations and standardized testing procedures in strict alignment with compliance standards.")
    exp3_b2 = st.text_input("Bullet 3.2", "Maintained comprehensive testing documentation and collaborated with teams during new procedural trials.")

    exp4_company = st.text_input("Role & Company 4", "Company Name D | Customer Service / IT Support Representative")
    exp4_dates = st.text_input("Dates 4", "2014")
    exp4_b1 = st.text_input("Bullet 4.1", "Delivered remote Tier-1 technical assistance for broadband users, resolving hardware, router, and connection faults.")
    exp4_b2 = st.text_input("Bullet 4.2", "Guided non-technical end-users through network diagnostics, achieving rapid first-contact resolution metrics.")

with st.sidebar.expander("7. Education", expanded=False):
    edu1 = st.text_input("Education 1", "Bachelor of Information Technology | University Name | 2025 – Present")
    edu2 = st.text_input("Education 2", "Diploma in Information Technology | College Name | 2010 – 2014")
    edu3 = st.text_input("Education 3", "Secondary School Certificate (SPM) | School Name | 2007 – 2008")

# -------------------------------------------------------------
# DYNAMIC CSS ENGINES (Strict 1-Page Calibrated)
# -------------------------------------------------------------
base_css = """
@page {
    size: A4 portrait;
    margin: 10mm;
}
@media print {
    html, body {
        width: 210mm;
        height: 297mm;
        margin: 0 !important;
        padding: 0 !important;
        background: #fff;
    }
    .page-container {
        border: none !important;
        box-shadow: none !important;
        padding: 0 !important;
        margin: 0 !important;
        height: 100vh;
    }
    .no-print {
        display: none !important;
    }
}
.page-container {
    width: 210mm;
    max-height: 297mm;
    margin: 0 auto;
    background: #ffffff;
    padding: 12mm 14mm;
    box-sizing: border-box;
    overflow: hidden;
    border: 1px solid #dcdcdc;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}
p, ul { margin: 0; padding: 0; }
li { margin-bottom: 2.5px; }
ul { padding-left: 18px; }
"""

if theme_choice == "Corporate ATS Standard":
    theme_css = base_css + """
    body { font-family: 'Times New Roman', Times, serif; color: #111; line-height: 1.25; font-size: 10pt; }
    h1 { font-size: 17pt; font-weight: bold; text-align: center; margin: 0 0 3px 0; letter-spacing: 0.5px; text-transform: uppercase; }
    .contact { text-align: center; font-size: 9pt; margin-bottom: 10px; color: #333; }
    h2 { font-size: 10.5pt; font-weight: bold; text-transform: uppercase; border-bottom: 1px solid #111; padding-bottom: 1px; margin: 8px 0 4px 0; letter-spacing: 0.5px; }
    .job-header { display: flex; justify-content: space-between; font-weight: bold; margin-top: 5px; font-size: 9.5pt; }
    """
elif theme_choice == "Modern Operations":
    theme_css = base_css + """
    body { font-family: Arial, Helvetica, sans-serif; color: #1a202c; line-height: 1.28; font-size: 9.5pt; }
    h1 { font-size: 18pt; font-weight: bold; color: #0f172a; margin: 0 0 2px 0; }
    .contact { font-size: 8.5pt; margin-bottom: 10px; color: #475569; }
    h2 { font-size: 10pt; font-weight: bold; text-transform: uppercase; color: #1e3a8a; border-bottom: 1.5px solid #cbd5e1; padding-bottom: 2px; margin: 8px 0 4px 0; }
    .job-header { display: flex; justify-content: space-between; font-weight: bold; margin-top: 5px; font-size: 9pt; }
    """
else:  # Compact Tech
    theme_css = base_css + """
    body { font-family: 'Calibri', 'Segoe UI', sans-serif; color: #000; line-height: 1.2; font-size: 9.5pt; }
    h1 { font-size: 17pt; font-weight: bold; margin: 0 0 1px 0; }
    .contact { font-size: 8.5pt; margin-bottom: 8px; color: #333; }
    h2 { font-size: 10pt; font-weight: bold; text-transform: uppercase; background-color: #f1f5f9; padding: 2px 4px; margin: 7px 0 3px 0; }
    .job-header { display: flex; justify-content: space-between; font-weight: bold; margin-top: 4px; font-size: 9pt; }
    """

# -------------------------------------------------------------
# HTML TEMPLATE INJECTION
# -------------------------------------------------------------
resume_html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
{theme_css}
.print-btn-bar {{
    text-align: center;
    margin-bottom: 15px;
}}
.btn-print {{
    background-color: #0f172a;
    color: #ffffff;
    border: none;
    padding: 8px 20px;
    font-size: 14px;
    font-weight: 600;
    border-radius: 4px;
    cursor: pointer;
}}
.btn-print:hover {{
    background-color: #1e293b;
}}
</style>
</head>
<body>

<div class="no-print print-btn-bar">
    <button class="btn-print" onclick="window.print()">🖨️ Print to 1-Page PDF</button>
</div>

<div class="page-container">
    <h1>{name}</h1>
    <div class="contact">{contact_line} | {linkedin}</div>

    <h2>Professional Summary</h2>
    <p>{summary_text}</p>

    <h2>Core Competencies</h2>
    <ul style="list-style-type: square; margin-top: 2px;">
        <li><strong>Technical Support:</strong> {comp_1}</li>
        <li><strong>Administration & Systems:</strong> {comp_2}</li>
        <li><strong>Client Operations:</strong> {comp_3}</li>
        <li><strong>Languages:</strong> {comp_4}</li>
    </ul>

    <h2>Professional Experience</h2>
    
    <div class="job-header">
        <span>{exp1_company}</span>
        <span>{exp1_dates}</span>
    </div>
    <ul>
        <li>{exp1_b1}</li>
        <li>{exp1_b2}</li>
        <li>{exp1_b3}</li>
    </ul>

    <div class="job-header">
        <span>{exp2_company}</span>
        <span>{exp2_dates}</span>
    </div>
    <ul>
        <li>{exp2_b1}</li>
        <li>{exp2_b2}</li>
    </ul>

    <div class="job-header">
        <span>{exp3_company}</span>
        <span>{exp3_dates}</span>
    </div>
    <ul>
        <li>{exp3_b1}</li>
        <li>{exp3_b2}</li>
    </ul>

    <div class="job-header">
        <span>{exp4_company}</span>
        <span>{exp4_dates}</span>
    </div>
    <ul>
        <li>{exp4_b1}</li>
        <li>{exp4_b2}</li>
    </ul>

    <h2>Education</h2>
    <p style="margin-top: 3px; font-size: 9pt;">• {edu1}</p>
    <p style="margin-top: 2px; font-size: 9pt;">• {edu2}</p>
    <p style="margin-top: 2px; font-size: 9pt;">• {edu3}</p>
</div>

</body>
</html>
"""

components.html(resume_html, height=1150, scrolling=True)
