import spacy 
import re
import PyPDF2

nlp = spacy.load("en_core_web_sm")

SKILLS_DB = ["python", "machine learning", "data science", "sql", "excel", "java", "tensorflow",
             "nlp", "deep learning", "c++", "html", "css", "javascript", "power bi", "tableau", "scikit-learn"]

def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_info(text):
    doc = nlp(text)

    # Name extraction
    name = " ".join([ent.text for ent in doc.ents if ent.label_ == "PERSON"][:1])

    # Email extraction
    email = re.findall(r"[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+", text)
    email_matches = email[0] if email else "Not found"

    # Phone extraction
    phone = re.findall(r"\+?\d[\d\s\-\(\)]{8,}\d", text)
    phone_matches = phone[0] if phone else "Not found"

    # Skills matching
    found_skills = []
    for token in doc:
        token_lower = token.text.lower()
        if token_lower in [s.lower() for s in SKILLS_DB] and token_lower not in found_skills:
            found_skills.append(token_lower)

    # Final dictionary return
    return {
        "Name": name if name else "Not found",
        "Email": email_matches,
        "Phone": phone_matches,
        "Skills": found_skills
    }
