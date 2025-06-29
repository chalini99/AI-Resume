import streamlit as st
from resume_parser import extract_text_from_pdf, extract_info

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("🤖 AI Resume Analyzer")
st.write("Upload your resume (PDF) and get an instant analysis!")

uploaded_file = st.file_uploader("📄 Choose your resume (PDF format only)", type="pdf")

if uploaded_file is not None:
    with st.spinner('Analyzing your resume...'):
        text = extract_text_from_pdf(uploaded_file)
        result = extract_info(text) if text else None

    if not result:
        st.error("❌ Failed to extract info from the resume.")
    else:
        st.success("✅ Resume analysis complete!")
        st.subheader("🧾 Extracted Information:")

        # Show Name
        name = result.get("Name", "Not found")
        st.write(f"**Name:** {name}")

        # Show Email
        email = result.get("Email", "Not found")
        st.write(f"**Email:** {email}")

        # Show Phone
        phone = result.get("Phone", "Not found")
        st.write(f"**Phone:** {phone}")

        # Show Skills
        st.subheader("💼 Detected Skills:")
        skills = result.get("Skills", [])
        if skills:
            st.write(", ".join(skills))
        else:
            st.warning("No matching skills found.")

        st.info("Try uploading different resumes to see how it works!")

else:
    st.warning("📂 Please upload a resume file to begin.")

    