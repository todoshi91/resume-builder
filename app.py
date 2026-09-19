import streamlit as st
import streamlit.components.v1 as components
import re

st.set_page_config(page_title="1-Page A4 Resume Engine", layout="wide")

st.title("📄 1-Page A4 Resume Engine")

# -------------------------------------------------------------
# SIDEBAR CONTROLS & THEME PICKER
# -------------------------------------------------------------
st.sidebar.header("🎨 Layout & Input")
theme_choice = st.sidebar.selectbox(
    "Choose Resume Style:",
    [
        "Corporate ATS Standard",
        "Modern Operations",
        "Compact Tech",
        "Executive Serif",
        "Modern Two-Column (Sidebar)"
    ]
)

input_mode = st.sidebar.radio("Input Method:", ["⚡ Quick Paste (Auto-Arrange)", "✍️ Edit Single Fields"])

# Generic sanitized default template
default_paste = """FULL NAME: FIRSTNAME LASTNAME
CONTACT: City, State | +6012-000 0000 | user.name@email.com | linkedin.com/in/username

PROFESSIONAL SUMMARY:
Results-driven IT Support and Operations Specialist with a background in Information Technology. Combines Tier-1 remote technical troubleshooting expertise with commercial administration, CRM tracking, and client relations experience. Proven record of resolving technical inquiries, executing accurate documentation, and delivering high-touch customer support. Fully autonomous, self-directed, and equipped for remote operations.

CORE COMPETENCIES:
• Technical Support: Tier-1 Troubleshooting, Remote Helpdesk Operations, Hardware & Software Diagnostics, Network Connectivity
• Administration & Systems: MS Office Suite (Advanced Excel, Word, PowerPoint), Order Processing, Data Verification, Documentation
• Client Operations: Multi-channel Support (Email/Ticket/Phone), Account Maintenance, Conflict Escalation, SLA Compliance
• Languages: Professional Working Proficiency in English and Bahasa Melayu (Written & Verbal)

PROFESSIONAL EXPERIENCE:
Enterprise Operations Sdn. Bhd. | Commercial / Sales Executive | April 2024 – Present
- Administered commercial workflows by generating precise sales quotations, purchase orders, and technical logs.
- Provided specialized product consultation on technical devices, coordinating setups under strict operational standards.
- Maintained institutional key client accounts, consistently securing renewals and supporting departmental targets.

Regional Distribution Corp. | Accounts & Operations Representative | 2019 – 2020
- Handled general trade client accounts, resolving billing discrepancies, product returns, and logistics inquiries promptly.
- Executed daily payment collections, reconciled customer statements, and onboarded new retail accounts across regional territories.

Technical Services Ltd. | Quality / Operations Assistant | 2015 – 2019
- Executed quality-control evaluations and standardized testing procedures in strict compliance with safety regulations.
- Maintained comprehensive testing documentation and collaborated with teams during procedural trials.

Global Communications Support | Customer Support & IT Helpdesk | 2014
- Delivered remote Tier-1 technical assistance for network users, resolving hardware, router, and connection faults.
- Guided non-technical end-users step-by-step through network diagnostics, achieving rapid first-contact resolution metrics.
- Documented support cases, escalations, and troubleshooting outcomes accurately within ticketing databases.

EDUCATION:
• Bachelor of Information Technology | University Name | Current
• Diploma in Information Technology | College Name | Graduated
• Sijil Pelajaran Malaysia (SPM) | Secondary School Name | Completed
"""

# -------------------------------------------------------------
# PARSING LOGIC
# -------------------------------------------------------------
if input_mode == "⚡ Quick Paste (Auto-Arrange)":
    raw_text = st.sidebar.text_area("Paste / Edit All Info Here:", default_paste, height=360)

    name_m = re.search(r"FULL NAME:\s*(.*)", raw_text, re.IGNORECASE)
    name = name_m.group(1).strip() if name_m else "FIRSTNAME LASTNAME"

    contact_m = re.search(r"CONTACT:\s*(.*)", raw_text, re.IGNORECASE)
    contact_line = contact_m.group(1).strip() if contact_m else "City, State | +6012-000 0000 | user.name@email.com"

    summary_m = re.search(r"(?:PROFESSIONAL\s+)?SUMMARY:\s*\n(.*?)(?=\n[A-Z\s]{4,}:|\Z)", raw_text, re.DOTALL | re.IGNORECASE)
    summary_text = summary_m.group(1).strip() if summary_m else ""

    comp_m = re.search(r"(?:CORE\s+)?COMPETENCIES:\s*\n(.*?)(?=\n[A-Z\s]{4,}:|\Z)", raw_text, re.DOTALL | re.IGNORECASE)
    competencies = []
    if comp_m:
        for l in comp_m.group(1).strip().split("\n"):
            clean = l.strip().lstrip("•-* ")
            if clean:
                competencies.append(clean)

    exp_m = re.search(r"(?:PROFESSIONAL\s+)?EXPERIENCE:\s*\n(.*?)(?=\n[A-Z\s]{4,}:|\Z)", raw_text, re.DOTALL | re.IGNORECASE)
    jobs = []
    if exp_m:
        blocks = re.split(r"\n\s*\n", exp_m.group(1).strip())
        for b in blocks:
            lines = [l.strip() for l in b.split("\n") if l.strip()]
            if lines:
                header = lines[0].lstrip("•-* ")
                bullets = [l.lstrip("•-* ") for l in lines[1:] if l.strip()]
                jobs.append({"header": header, "bullets": bullets})

    edu_m = re.search(r"EDUCATION:\s*\n(.*?)(?=\n[A-Z\s]{4,}:|\Z)", raw_text, re.DOTALL | re.IGNORECASE)
    education = []
    if edu_m:
        for l in edu_m.group(1).strip().split("\n"):
            clean = l.strip().lstrip("•-* ")
            if clean:
                education.append(clean)

else:
    name = st.sidebar.text_input("Full Name", "FIRSTNAME LASTNAME")
    contact_line = st.sidebar.text_input("Contact", "City, State | +6012-000 0000 | user.name@email.com | linkedin.com/in/username")
    summary_text = st.sidebar.text_area("Summary", "Results-driven IT Support and Operations Specialist with a background in Information Technology. Combines Tier-1 remote troubleshooting expertise with commercial administration, CRM tracking, and client relations experience.", height=90)
    competencies = [
        "Technical Support: Tier-1 Troubleshooting, Remote Helpdesk Operations, Hardware/Software Diagnostics",
        "Administration & Systems: MS Office Suite (Excel, Word, PowerPoint), Order Processing, Data Verification",
        "Client Operations: Multi-channel Support, Account Maintenance, SLA Compliance",
        "Languages: Professional Working Proficiency in English and Bahasa Melayu"
    ]
    jobs = [
        {"header": "Enterprise Operations Sdn. Bhd. | Commercial / Sales Executive | April 2024 – Present", "bullets": ["Administered commercial workflows and quotations.", "Provided product consultation on technical devices."]},
        {"header": "Global Communications Support | Customer Support & IT Helpdesk | 2014", "bullets": ["Delivered remote Tier-1 technical assistance.", "Achieved first-contact resolution."]}
    ]
    education = [
        "Bachelor of Information Technology | University Name | Current",
        "Diploma in Information Technology | College Name | Graduated"
    ]

# -------------------------------------------------------------
# BALANCED A4 CSS (Calibrated for Proportional Vertical Fill)
# -------------------------------------------------------------
base_css = """
@page {
    size: 210mm 297mm;
    margin: 0mm;
}
@media print {
    html, body {
        width: 210mm !important;
        height: 297mm !important;
        margin: 0 !important;
        padding: 0 !important;
        background: #ffffff !important;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }
    .page-container {
        width: 210mm !important;
        height: 297mm !important;
        max-height: 297mm !important;
        border: none !important;
        box-shadow: none !important;
        margin: 0 !important;
        padding: 12mm 14mm !important;
        page-break-after: avoid !important;
        page-break-inside: avoid !important;
    }
    .no-print {
        display: none !important;
    }
}
body {
    margin: 0;
    padding: 0;
    background-color: #f1f5f9;
}
.page-container {
    width: 210mm;
    min-height: 297mm;
    max-height: 297mm;
    margin: 10px auto;
    background: #ffffff;
    padding: 12mm 14mm;
    box-sizing: border-box;
    overflow: hidden;
    border: 1px solid #cbd5e1;
    box-shadow: 0 4px 14px rgba(0,0,0,0.12);
}
p, ul { margin: 0; padding: 0; }
li { margin-bottom: 3.5px; }
ul { padding-left: 18px; }
.job-header {
    font-weight: bold;
    margin-top: 8px;
    margin-bottom: 2px;
    font-size: 9.6pt;
    display: flex;
    justify-content: space-between;
}
.print-bar {
    text-align: center;
    padding: 10px 0 15px 0;
}
.btn-print {
    background-color: #0f172a;
    color: #ffffff;
    border: none;
    padding: 9px 24px;
    font-size: 14px;
    font-weight: 600;
    border-radius: 6px;
    cursor: pointer;
}
"""

if theme_choice == "Corporate ATS Standard":
    theme_css = base_css + """
    body { font-family: 'Times New Roman', Times, serif; color: #111; line-height: 1.34; font-size: 9.8pt; }
    h1 { font-size: 18pt; font-weight: bold; text-align: center; margin: 0 0 3px 0; letter-spacing: 0.5px; text-transform: uppercase; }
    .contact { text-align: center; font-size: 9pt; margin-bottom: 10px; color: #333; }
    h2 { font-size: 10.5pt; font-weight: bold; text-transform: uppercase; border-bottom: 1px solid #111; padding-bottom: 2px; margin: 10px 0 4px 0; letter-spacing: 0.4px; }
    """
elif theme_choice == "Modern Operations":
    theme_css = base_css + """
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif; color: #1e293b; line-height: 1.34; font-size: 9.5pt; }
    h1 { font-size: 18pt; font-weight: 700; color: #0f172a; margin: 0 0 3px 0; }
    .contact { font-size: 8.8pt; margin-bottom: 10px; color: #475569; }
    h2 { font-size: 10pt; font-weight: 700; text-transform: uppercase; color: #1e40af; border-bottom: 1.5px solid #cbd5e1; padding-bottom: 2px; margin: 9px 0 4px 0; }
    """
elif theme_choice == "Compact Tech":
    theme_css = base_css + """
    body { font-family: 'Calibri', 'Segoe UI', Arial, sans-serif; color: #000; line-height: 1.3; font-size: 9.6pt; }
    h1 { font-size: 17pt; font-weight: bold; margin: 0 0 2px 0; }
    .contact { font-size: 8.8pt; margin-bottom: 8px; color: #333; }
    h2 { font-size: 9.8pt; font-weight: bold; text-transform: uppercase; background-color: #f1f5f9; padding: 3px 5px; margin: 8px 0 4px 0; }
    """
elif theme_choice == "Executive Serif":
    theme_css = base_css + """
    body { font-family: Georgia, 'Times New Roman', serif; color: #1e293b; line-height: 1.34; font-size: 9.6pt; }
    h1 { font-size: 18pt; font-weight: normal; text-align: center; margin: 0 0 3px 0; letter-spacing: 1px; color: #0f172a; }
    .contact { text-align: center; font-size: 8.8pt; margin-bottom: 10px; color: #64748b; font-style: italic; }
    h2 { font-size: 10.2pt; font-weight: bold; text-transform: uppercase; text-align: center; border-bottom: 1px solid #94a3b8; padding-bottom: 2px; margin: 9px 0 4px 0; letter-spacing: 0.8px; color: #334155; }
    """
else:  # Modern Two-Column (Sidebar)
    theme_css = base_css + """
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif; color: #1e293b; line-height: 1.32; font-size: 9.2pt; }
    .page-container { padding: 0 !important; display: flex; flex-direction: row; height: 297mm; }
    .sidebar-panel { width: 34%; background-color: #f8fafc; border-right: 1px solid #e2e8f0; padding: 12mm 9mm; box-sizing: border-box; }
    .main-panel { width: 66%; padding: 12mm 11mm; box-sizing: border-box; }
    h1 { font-size: 16pt; font-weight: 800; color: #0f172a; margin: 0 0 4px 0; line-height: 1.1; }
    .side-title { font-size: 9.4pt; font-weight: 700; text-transform: uppercase; color: #0284c7; border-bottom: 1px solid #cbd5e1; padding-bottom: 2px; margin: 14px 0 6px 0; }
    .main-title { font-size: 10pt; font-weight: 700; text-transform: uppercase; color: #0f172a; border-bottom: 1.5px solid #0284c7; padding-bottom: 2px; margin: 9px 0 4px 0; }
    .side-item { margin-bottom: 6px; font-size: 8.8pt; }
    """

# -------------------------------------------------------------
# DYNAMIC HTML ENGINE
# -------------------------------------------------------------
comp_html = "".join([f"<li>{c}</li>" for c in competencies])

exp_html = ""
for j in jobs:
    bullets_html = "".join([f"<li>{b}</li>" for b in j["bullets"]])
    exp_html += f"""
    <div class="job-header">{j["header"]}</div>
    <ul>{bullets_html}</ul>
    """

edu_html = "".join([f"<p style='margin-top: 3px; font-size: 9.2pt;'>• {e}</p>" for e in education])

if theme_choice == "Modern Two-Column (Sidebar)":
    side_skills = "".join([f"<div class='side-item'>• {c}</div>" for c in competencies])
    side_edu = "".join([f"<div class='side-item'>• {e}</div>" for e in education])
    resume_html = f"""
    <!DOCTYPE html>
    <html>
    <head><meta charset="utf-8"><style>{theme_css}</style></head>
    <body>
    <div class="no-print print-bar"><button class="btn-print" onclick="window.print()">🖨️ Print / Save 1-Page A4 PDF</button></div>
    <div class="page-container">
        <div class="sidebar-panel">
            <h1>{name}</h1>
            <div class="side-title" style="margin-top: 8px;">Contact</div>
            <div class="side-item">{contact_line.replace('|', '<br>')}</div>
            <div class="side-title">Core Competencies</div>
            {side_skills}
            <div class="side-title">Education</div>
            {side_edu}
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
    <div class="no-print print-bar"><button class="btn-print" onclick="window.print()">🖨️ Print / Save 1-Page A4 PDF</button></div>
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

components.html(resume_html, height=1240, scrolling=True)
