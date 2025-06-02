import streamlit as st
from PIL import Image

# Set up the page
st.set_page_config(page_title="Navaneetha Krishnan R", layout="wide")

# Load resume and image
with open("Navaneeth_resume 20dec.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open("profile_pic.jpg")  # Make sure this file is in the same folder

# --- HEADER ---
st.write("")

col1, col2 = st.columns([1, 4], gap="large")

with col1:
    st.image(profile_pic, width=180)

with col2:
    st.markdown("<h1 style='margin-bottom: 0;'>Navaneetha Krishnan R</h1>", unsafe_allow_html=True)
    st.markdown("🎓 <b>B.Tech in Artificial Intelligence and Data Science</b>", unsafe_allow_html=True)
    st.markdown("💻 Python | 🤖 AI/ML | 🧠 Deep Learning | 📸 OpenCV | 🛠️ OCR", unsafe_allow_html=True)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name="Navaneeth_Krishnan_Resume.pdf",
        mime="application/pdf"
    )

# --- ABOUT ME ---
st.write("---")
st.header("🧑‍💼 About Me")
st.write("""
I'm a recent B.Tech graduate in Artificial Intelligence and Data Science from Sri Sairam Engineering College.
I specialize in Python programming, AI/ML model development, and real-time analytics. 
I'm passionate about applying AI to solve real-world challenges and I'm actively seeking opportunities in Machine Learning, AI, and Software Development.
""")

# --- SKILLS ---
st.write("---")
st.header("🛠️ Skills")
st.write("""
- **Programming:** Python (Expert), C/C++ (Intermediate), Java (Basics), SQL  
- **Libraries/Frameworks:** TensorFlow, Keras, OpenCV, Transformers (Hugging Face), Matplotlib, ChromaDB  
- **Tools:** Power BI, MySQL, MS Office, Figma, UiPath, Unity  
- **Soft Skills:** Leadership, Teamwork, Critical Thinking, Adaptability  
""")

# --- EDUCATION ---
st.write("---")
st.header("🎓 Education")
st.write("""
- **B.Tech in Artificial Intelligence and Data Science**  
  Sri Sairam Engineering College, Chennai (2021–2025) | CGPA: 7.45

- **HSC - 12th Std (2021):** M.P. Aanandh MHSS, Chennai – 72.5%  
- **SSLC - 10th Std (2019):** M.P. Aanandh MHSS, Chennai – 67%  
""")

# --- PROJECTS ---
st.write("---")
st.header("📂 Projects")
projects = [
    "Flight Simulator Trainer using VR",
    "Facial Recognition using Python for emotion detection",
    "Posture Recognition for astronauts using OpenCV",
    "Sentiment Analysis using Voice",
    "Text Extraction using OCR in Python",
    "Image Classification using CNN on CIFAR dataset"
]
for p in projects:
    st.write(f"🔹 {p}")

# --- EXPERIENCE ---
st.write("---")
st.header("💼 Experience")
st.write("""
**Intern – Jorim Technology Pvt Ltd**  
- Oct 2023 – Dec 2023: Worked on emotion recognition from speech, chat, and face for mentally ill patients  
- Apr 2024 – May 2024: Worked on OCR and image-captioning model research
         
**Intern- Workcohol Solutions**
- Apr 2025 – currently working: Working on Creating AI modules 
""")

# --- CERTIFICATIONS ---
st.write("---")
st.header("🎖️ Certifications")
certs = [
    "AI for Everyone – IBM edX",
    "AI Chatbots Without Programming – IBM edX",
    "Introduction to Data Science – IBM edX",
    "Introduction to Cloud Computing – IBM edX",
    "Fundamentals of Deep Learning – NVIDIA",
    "Python Essentials – IBM edX"
]
for c in certs:
    st.write(f"📘 {c}")

# --- PUBLICATIONS ---
st.write("---")
st.header("📚 Publications & Patents")
st.write("""
- 🧠 **Patent:** Virtual Reality powered flight training (Issue 45/2024)  
- 📝 **Paper:** Flight Procedure Trainer Using VR — [TIJER Link](https://tijer.org/TIJER/papers/TIJER2405024)
""")

# --- LANGUAGES ---
st.write("---")
st.header("🌐 Languages Known")
st.write("Tamil (Native), English (Professional), Hindi (Intermediate), Malayalam (Intermediate), French (Beginner)")

# --- CONTACT ---
st.write("---")
st.header("📬 Contact Me")
st.write("📧 Email: rnk12092002@gmail.com")
st.write("📞 Phone: +91-99529-62137")
st.write("🔗 LinkedIn: [linkedin.com/in/navaneetha-krishnan-r](https://linkedin.com/in/navaneetha-krishnan-r)")
