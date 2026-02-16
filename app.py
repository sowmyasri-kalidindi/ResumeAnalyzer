import streamlit as st
import PyPDF2

# -----------------------
# Load skills from file
# -----------------------
with open("skills.txt", "r") as file:
    skills = file.read().split("\n")

# Remove empty lines and normalize case
skills = [skill.strip().lower() for skill in skills if skill.strip()]

# -----------------------
# Function to extract text from PDF
# -----------------------
def extract_text(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.lower()

# -----------------------
# Streamlit App
# -----------------------
st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄")

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume (PDF) to check which skills you have!")

uploaded_file = st.file_uploader("Upload Resume", type="pdf")

if uploaded_file:
    # Extract resume text
    text = extract_text(uploaded_file)

    # -----------------------
    # Check skills
    # -----------------------
    found = [skill for skill in skills if skill in text]
    missing = [skill for skill in skills if skill not in text]

    # Display results
    st.subheader("✅ Skills Found")
    if found:
        st.write(found)
    else:
        st.write("No matching skills found.")

    st.subheader("❌ Missing Skills")
    if missing:
        st.write(missing)
    else:
        st.write("All target skills found!")

    # -----------------------
    # Proportional Score
    # -----------------------
    score = (len(found) / len(skills)) * 100
    score = round(score, 2)

    st.subheader("🎯 Score")
    st.write(f"{score} / 100")
