import streamlit as st
import streamlit.components.v1 as components
import re

st.set_page_config(page_title="1-Page Resume Builder", layout="wide")

st.title("📄 1-Page Resume Engine")

# -------------------------------------------------------------
# SIDEBAR CONTROLS & THEME PICKER
# -------------------------------------------------------------
st.sidebar.header("🎨 Style & Input Mode")
theme_choice = st.sidebar.selectbox(
    "Resume Layout & Theme:",
    [
        "Corporate ATS Standard",
        "Modern Operations",
        "Compact Tech",
        "Executive Serif",
        "Modern Two-Column (Sidebar)"
    ]
)

input_mode = st.sidebar.radio("How would you like to enter info?", ["⚡ Quick Paste (Auto-Arrange)", "✍️ Individual Fields"])

# -------------------------------------------------------------
# DEFAULT TEXT TEMPLATE
# -------------------------------------------------------------
default_paste = """FULL NAME: JANE DOE
CONTACT: Petaling Jaya, Selangor | +6012-345 6789 | janedoe@email.com | linkedin.com/in/janedoe

SUMMARY:
Results-driven IT Support and Operations Specialist with a solid background in Information Technology. Combines Tier-1 remote troubleshooting expertise with commercial administration, CRM tracking, and client relations. Autonomous, detail-oriented, and equipped for remote operations.

CORE COMPETENCIES:
• Technical Support: Tier-1 Troubleshooting, Remote Helpdesk Operations, Hardware & Software Diagnostics
• Administration & Systems: MS Office Suite (Excel, Word, PowerPoint), Order Processing, Data Verification
• Client Operations: Multi-channel Support (Email/Ticket/Phone), Account Maintenance, SLA Compliance
• Languages: Professional Working Proficiency in English and Bahasa Melayu (Written & Verbal)

EXPERIENCE:
Company Name A | Sales Executive | April 2024 – March 2026
- Administered commercial workflows by generating precise sales quotations, purchase orders, and technical logs.
- Provided specialized product consultation on technical devices, coordinating setups under strict operational standards.
- Maintained key client accounts, consistently securing renewals and supporting departmental revenue targets.

Company Name B | Sales Representative | 2019 – 2020
- Handled client accounts, resolving billing discrepancies, product returns, and logistics inquiries promptly.
- Executed daily payment collections, reconciled customer statements, and onboarded new retail accounts.

Company Name C | Operations / Lab Assistant | 2015 – 2019
- Executed quality-control evaluations and standardized testing procedures in strict compliance with safety regulations.
- Maintained comprehensive testing documentation and collaborated with teams during procedural trials.

Company Name D | Customer Service / IT Support | 2014
- Delivered remote Tier-1 technical assistance for broadband users, resolving connection and hardware faults.
- Guided non-technical end-users through diagnostics, achieving rapid first-contact resolution metrics.

EDUCATION:
• Bachelor of Information Technology | MUST | 2025 – Present
• Diploma in Information Technology | College Name | 2010 – 2014
• Secondary School Certificate (SPM) | School Name | 2007 – 2008
"""

# -------------------------------------------------------------
# PARSING LOGIC
# -------------------------------------------------------------
if input_mode == "⚡ Quick Paste (Auto-Arrange)":
    st.sidebar.caption("Paste your complete details below. Follow the section labels (SUMMARY, CORE COMPETENCIES, EXPERIENCE, EDUCATION).")
    raw_text = st.sidebar.text_area("Paste All Info Here:", default_paste, height=350)

    # Extract Name & Contact
    name_match = re.search(r"FULL NAME:\s*(.*)", raw_text, re.IGNORECASE)
    name = name_match.group(1).strip() if name_match else "YOUR FULL NAME"

    contact_match = re.search(r"CONTACT:\s*(.*)", raw_text, re.IGNORECASE)
    contact_raw = contact_match.group(1).strip() if contact_match else "City, State | Phone | Email"
    contact_line = contact_raw

    # Extract Summary
    summary_match = re.search(r"SUMMARY:\s*\n(.*?)(?=\n[A-Z\s]{4,}:|\Z)", raw_text, re.DOTALL | re.IGNORECASE)
    summary_text = summary_match.group(1).strip() if summary_match else ""

    # Extract Competencies
    comp_match = re.search(r"CORE COMPETENCIES:\s*\n(.*?)(?=\n[A-Z\s]{4,}:|\Z)", raw_text, re.DOTALL | re.IGNORECASE)
    competencies = []
    if comp_match:
        for line in comp_match.group(1).strip().split("\n"):
            clean_l = line.strip().lstrip("•-* ")
            if clean_l:
                competencies.append(clean_l)

    # Extract Experience
    exp_match = re.search(r"EXPERIENCE:\s*\n(.*?)(?=\n[A-Z\s]{4,}:|\Z)", raw_text, re.DOTALL | re.IGNORECASE)
    jobs = []
    if exp_match:
        job_blocks = re.split(r"\n\s*\n", exp_match.group(1).strip())
        for block in job_blocks:
            lines = [l.strip() for l in block.split("\n") if l.strip()]
            if lines:
                header = lines[0]
                bullets = [l.lstrip("•-* ") for l in lines[1:] if l.strip()]
                jobs.append({"header": header, "bullets": bullets})

    # Extract Education
    edu_match = re.search(r"EDUCATION:\s*\n(.*?)(?=\n[A-Z\s]{4,}:|\Z)", raw_text, re.DOTALL | re.IGNORECASE)
    education = []
    if edu_match:
        for line in edu_match.group(1).strip().split("\n"):
            clean_l = line.strip().lstrip("•-* ")
            if clean_l:
                education.append(clean_l)

else:
    # Individual Fields Mode
    with st.sidebar.expander("1. Contact Information", expanded=False):
        name = st.text_input("Full Name", "YOUR FULL NAME")
        contact_line = st.text_input("Contact Details", "City, State | +6012-345 6789 | youremail@example.com | linkedin.com/in/profile")

    with st.sidebar.expander("2. Professional Summary", expanded=False):
        summary_text = st.text_area("Summary", "Results-driven IT Support and Operations Specialist with a background in Information Technology. Combines Tier-1 remote troubleshooting expertise with commercial administration, CRM tracking, and client relations experience.", height=90)

    with st.sidebar.expander("3. Core Competencies", expanded=False):
        c1 = st.text_input("Competency 1", "Technical Support: Tier-1 Troubleshooting, Remote Helpdesk Operations, Hardware & Software Diagnostics")
        c2 = st.text_input("Competency 2", "Administration & Systems: MS Office Suite (Excel, Word, PowerPoint), Order Processing, Data Verification")
        c3 = st.text_input("Competency 3", "Client Operations: Multi-channel Support (Email/Ticket/Phone), Account Maintenance, SLA Compliance")
        c4 = st.text_input("Competency 4", "Languages: Professional Working Proficiency in English and Bahasa Melayu (Written & Verbal)")
        competencies = [c1, c2, c3, c4]

    with st.sidebar.expander("4. Experience", expanded=False):
        j1_h = st.text_input("Job 1 Header", "Company Name A | Sales Executive | April 2024 – March 2026")
        j1_b1 = st.text_input("Job 1 Bullet 1", "Administered commercial workflows by generating precise sales quotations, purchase orders, and technical logs.")
        j1_b2 = st.text_input("Job 1 Bullet 2", "Provided specialized product consultation on technical devices under strict operational standards.")
        jobs = [{"header": j1_h, "bullets": [j1_b1, j1_b2]}]

    with st.sidebar.expander("5. Education", expanded=False):
        e1 = st.text_input("Edu 1", "Bachelor of Information Technology | MUST | 2025 – Present")
        e2 = st.text_input("Edu 2", "Diploma in Information Technology | College Name | 2010 – 2014")
        education = [e1, e2]

# -------------------------------------------------------------
# CSS LAYOUT ENGINES (Strict 1-Page Calibrated)
# -------------------------------------------------------------
base_css = """
@page { size: A4 portrait; margin: 8mm; }
@media print {
    html, body { width: 210mm; height: 297mm; margin: 0 !important; padding: 0 !important; background: #fff; }
    .page-container { border: none !important; box-shadow: none !important; padding: 0 !important; margin: 0 !important; height: 100vh; }
    .no-print { display: none !important; }
}
.page-container {
    width: 210mm;
    max-height: 297mm;
    margin: 0 auto;
    background: #ffffff;
    padding: 10mm 12mm;
    box-sizing: border-box;
    overflow: hidden;
    border: 1px solid #e2e8f0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}
p, ul { margin: 0; padding: 0; }
li { margin-bottom: 2.5px; }
ul { padding-left: 18px; }
.job-header { display: flex; justify-content: space-between; font-weight: bold; margin-top: 5px; font-size: 9pt; }
.print-btn-bar { text-align: center; margin-bottom: 12px; }
.btn-print { background-color: #0f172a; color: #ffffff; border: none; padding: 8px 22px; font-size: 14px; font-weight: 600; border-radius: 4px; cursor: pointer; }
.btn-print:hover { background-color: #1e293b; }
"""

if theme_choice == "Corporate ATS Standard":
    theme_css = base_css + """
    body { font-family: 'Times New Roman', Times, serif; color: #111; line-height: 1.25; font-size: 10pt; }
    h1 { font-size: 17pt; font-weight: bold; text-align: center; margin: 0 0 2px 0; text-transform: uppercase; letter-spacing: 0.5px; }
    .contact { text-align: center; font-size: 9pt; margin-bottom: 8px; color: #333; }
    h2 { font-size: 10.5pt; font-weight: bold; text-transform: uppercase; border-bottom: 1px solid #111; padding-bottom: 1px; margin: 7px 0 3px 0; }
    """
elif theme_choice == "Modern Operations":
    theme_css = base_css + """
    body { font-family: Arial, Helvetica, sans-serif; color: #1e293b; line-height: 1.25; font-size: 9.5pt; }
    h1 { font-size: 18pt; font-weight: bold; color: #0f172a; margin: 0 0 2px 0; }
    .contact { font-size: 8.5pt; margin-bottom: 8px; color: #64748b; }
    h2 { font-size: 10pt; font-weight: bold; text-transform: uppercase; color: #1e40af; border-bottom: 1.5px solid #cbd5e1; padding-bottom: 2px; margin: 7px 0 3px 0; }
    """
elif theme_choice == "Compact Tech":
    theme_css = base_css + """
    body { font-family: 'Calibri', 'Segoe UI', sans-serif; color: #000; line-height: 1.2; font-size: 9.5pt; }
    h1 { font-size: 17pt; font-weight: bold; margin: 0 0 1px 0; }
    .contact { font-size: 8.5pt; margin-bottom: 7px; color: #333; }
    h2 { font-size: 9.5pt; font-weight: bold; text-transform: uppercase; background-color: #f1f5f9; padding: 2px 4px; margin: 6px 0 3px 0; }
    """
elif theme_choice == "Executive Serif":
    theme_css = base_css + """
    body { font-family: Georgia, 'Times New Roman', serif; color: #222; line-height: 1.27; font-size: 9.5pt; }
    h1 { font-size: 18pt; font-weight: normal; text-align: center; margin: 0 0 2px 0; letter-spacing: 1px; color: #111; }
    .contact { text-align: center; font-size: 8.5pt; margin-bottom: 8px; color: #555; font-style: italic; }
    h2 { font-size: 10pt; font-weight: bold; text-transform: uppercase; text-align: center; border-bottom: 1px solid #94a3b8; padding-bottom: 2px; margin: 7px 0 3px 0; letter-spacing: 1px; color: #334155; }
    """
else:  # Modern Two-Column (Sidebar)
    theme_css = base_css + """
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; color: #1e293b; line-height: 1.24; font-size: 9pt; }
    .page-container { padding: 0 !important; display: flex; flex-direction: row; height: 297mm; }
    .sidebar-panel { width: 33%; background-color: #f8fafc; border-right: 1px solid #e2e8f0; padding: 10mm 8mm; box-sizing: border-box; }
    .main-panel { width: 67%; padding: 10mm 10mm; box-sizing: border-box; }
    h1 { font-size: 16pt; font-weight: 800; color: #0f172a; margin: 0 0 4px 0; line-height: 1.1; }
    .side-title { font-size: 9.5pt; font-weight: 700; text-transform: uppercase; color: #0284c7; border-bottom: 1px solid #cbd5e1; padding-bottom: 2px; margin: 12px 0 6px 0; }
    .main-title { font-size: 10pt; font-weight: 700; text-transform: uppercase; color: #0f172a; border-bottom: 1.5px solid #0284c7; padding-bottom: 2px; margin: 8px 0 4px 0; }
    .side-item { margin-bottom: 7px; font-size: 8.5pt; }
    """

# -------------------------------------------------------------
# BUILD DYNAMIC HTML SECTIONS
# -------------------------------------------------------------
# Competencies List HTML
comp_html = "".join([f"<li>{c}</li>" for c in competencies])

# Experience List HTML
exp_html = ""
for job in jobs:
    bullets_html = "".join([f"<li>{b}</li>" for b in job["bullets"]])
    exp_html += f"""
    <div class="job-header">
        <span>{job["header"]}</span>
    </div>
    <ul>{bullets_html}</ul>
    """

# Education List HTML
edu_html = "".join([f"<p style='margin-top: 2px; font-size: 9pt;'>• {e}</p>" for e in education])

# -------------------------------------------------------------
# HTML OUTPUT GENERATION
# -------------------------------------------------------------
if theme_choice == "Modern Two-Column (Sidebar)":
    side_skills_html = "".join([f"<div class='side-item'>• {c}</div>" for c in competencies])
    side_edu_html = "".join([f"<div class='side-item'>• {e}</div>" for e in education])
    resume_html = f"""
    <!DOCTYPE html>
    <html>
    <head><meta charset="utf-8"><style>{theme_css}</style></head>
    <body>
    <div class="no-print print-btn-bar"><button class="btn-print" onclick="window.print()">🖨️ Print to 1-Page PDF</button></div>
    <div class="page-container">
        <div class="sidebar-panel">
            <h1>{name}</h1>
            <div class="side-title" style="margin-top: 10px;">Contact</div>
            <div class="side-item">{contact_line.replace('|', '<br>')}</div>

            <div class="side-title">Core Competencies</div>
            {side_skills_html}

            <div class="side-title">Education</div>
            {side_edu_html}
        </div>
        <div class="main-panel">
            <div class="main-title" style="margin-top: 0;">Professional Summary</div>
            <p>{summary_text}</p>

            <div class="main-title">Professional Experience</div>
            {exp_html}
        </div>
    </div>
    </body>
    </html>
    """
else:
    resume_html = f"""
    <!DOCTYPE html>
    <html>
    <head><meta charset="utf-8"><style>{theme_css}</style></head>
    <body>
    <div class="no-print print-btn-bar"><button class="btn-print" onclick="window.print()">🖨️ Print to 1-Page PDF</button></div>
    <div class="page-container">
        <h1>{name}</h1>
        <div class="contact">{contact_line}</div>

        <h2>Professional Summary</h2>
        <p>{summary_text}</p>

        <h2>Core Competencies</h2>
        <ul style="list-style-type: square; margin-top: 2px;">
            {comp_html}
        </ul>

        <h2>Professional Experience</h2>
        {exp_html}

        <h2>Education</h2>
        {edu_html}
    </div>
    </body>
    </html>
    """

components.html(resume_html, height=1180, scrolling=True)
