import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Set up the page
st.set_page_config(page_title="Navaneetha Krishnan R", layout="wide")

# Load resume
with open("Navaneeth_resume 20dec.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# Load and encode profile picture
def get_base64_image(image: Image.Image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_bytes = buffered.getvalue()
    return base64.b64encode(img_bytes).decode()

profile_pic = Image.open("profile_pic.jpg")
profile_pic_base64 = get_base64_image(profile_pic)

# --- CUSTOM CSS STYLING ---
st.markdown(f"""
    <style>
        /* Page background and text */
        body {{
            font-family: 'Segoe UI', sans-serif;
            color: white;
        }}
        /* Profile image styling */
        .profile-pic {{
            border-radius: 50%;
            width: 180px;
            height: 180px;
            object-fit: cover;
            box-shadow: 0 4px 12px rgba(255, 255, 255, 0.2);
            animation: fadeIn 1.5s ease-in-out;
        }}
        /* Text animation */
        .fade-text {{
            animation: fadeIn 2s ease-in-out;
        }}
        /* Button styling */
        .stDownloadButton > button {{
            background-color: #1f77b4;
            color: white;
            border-radius: 8px;
            padding: 0.6em 1.2em;
            font-size: 16px;
            transition: 0.3s ease-in-out;
        }}
        .stDownloadButton > button:hover {{
            background-color: #45aaf2;
            transform: scale(1.05);
        }}
        /* Fade animation */
        @keyframes fadeIn {{
            0% {{ opacity: 0; transform: translateY(20px); }}
            100% {{ opacity: 1; transform: translateY(0); }}
        }}
    </style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
col1, col2 = st.columns([1, 4], gap="large")

with col1:
    st.markdown(f"""
        <img class="profile-pic" src="data:image/png;base64,{profile_pic_base64}" alt="Profile Pic">
    """, unsafe_allow_html=True)

with col2:
    st.markdown("<h1 class='fade-text'>Navaneetha Krishnan R</h1>", unsafe_allow_html=True)
    st.markdown("<p class='fade-text'>🎓 <b>B.Tech in Artificial Intelligence and Data Science</b></p>", unsafe_allow_html=True)
    st.markdown("<p class='fade-text'>💻 Python | 🤖 AI/ML | 🧠 Deep Learning | 📸 OpenCV | 🛠️ OCR</p>", unsafe_allow_html=True)
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
    "Image Classification using CNN on CIFAR dataset",
    "AI Story Generator using Cohere API"
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
         
**Intern – Workcohol solutions**
- Apr 2025 – currently working: Working on Creating AI models
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
