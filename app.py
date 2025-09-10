
import streamlit as st
import base64

st.set_page_config(
    page_title="Alper Ozarslan - Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    .sub-header {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .navbar {
        display: flex;
        justify-content: center;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 30px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .navbar a {
        color: white;
        text-decoration: none;
        padding: 10px 20px;
        margin: 0 10px;
        border-radius: 8px;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    .navbar a:hover {
        background-color: rgba(255, 255, 255, 0.2);
        transform: translateY(-2px);
    }
    .project-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        border-left: 4px solid #1f77b4;
    }
    .skill-tag {
        display: inline-block;
        background: #e8f4fd;
        color: #1f77b4;
        padding: 5px 10px;
        border-radius: 15px;
        margin: 2px;
        font-size: 0.9rem;
    }
    .contact-info {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">Alper Ozarslan</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Machine Learning Student with MLOps Knowledge</p>', unsafe_allow_html=True)

# Navigation
st.markdown("""
<div class="navbar">
    <a href="#about-me">About Me</a>
    <a href="#projects">Projects</a>
    <a href="#experience-education">Experience</a>
    <a href="#certifications">Certifications</a>
    <a href="#contact">Contact</a>
</div>
""", unsafe_allow_html=True)

# About Me Section
st.markdown('<div id="about-me"></div>', unsafe_allow_html=True)
st.header("🎯 About Me")

col1, col2 = st.columns([2, 1])

with col1:
    st.write("""
    3rd-year Computer Science student with practical experience in machine learning, deep learning, and data engineering.
    Skilled in Python, SQL, AWS, and .NET, with hands-on work from datathons, internships, and certification programs.
    Interested in projects involving AI, automation, and cloud-based solutions.
    """)

with col2:
    st.markdown("### 📍 Location")
    st.write("Istanbul/Fatih, Çorlu/Tekirdağ")
    st.markdown("### 🎓 Education")
    st.write("Computer Science (CGPA: 3.38)")
    st.write("Istanbul University")

# Skills Section
st.subheader("💻 Technical Skills")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Programming Languages**")
    languages = ["Python", "C#", "JavaScript", "Node.js", "Java", "R", "C"]
    for lang in languages:
        st.markdown(f'<span class="skill-tag">{lang}</span>', unsafe_allow_html=True)

with col2:
    st.markdown("**Python Libraries**")
    libraries = ["Scikit-Learn", "PyTorch", "Pandas", "Keras", "TensorFlow", "YOLO", "OpenCV", "MLflow"]
    for lib in libraries:
        st.markdown(f'<span class="skill-tag">{lib}</span>', unsafe_allow_html=True)

with col3:
    st.markdown("**Tools & Technologies**")
    tools = ["Git", "Docker", "AWS", "MySQL", "PostgreSQL", "Linux"]
    for tool in tools:
        st.markdown(f'<span class="skill-tag">{tool}</span>', unsafe_allow_html=True)

st.markdown("**Speaking Languages:** Turkish (Native), English B2, German (A1)")

# Projects Section
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.header("🚀 Featured Projects")

project_data = [
    {
        "name": "🏭 Yildiz Technical University ML Datathon 2025",
        "description": "Built a machine learning model using real factory machine data to predict maintenance needs and failures. Applied data preprocessing, feature engineering, and model evaluation techniques to improve prediction accuracy.",
        "technologies": ["Machine Learning", "Data Preprocessing", "Feature Engineering", "Predictive Maintenance"],
        "github_link": "#"
    },
    {
        "name": "🖼️ Istanbul Technical University Deep Learning Datathon 2025",
        "description": "Developed a deep learning model using images from three different cities for image-based predictions and classification. Applied CNNs for feature extraction and model training.",
        "technologies": ["Deep Learning", "Computer Vision", "CNNs", "Image Classification"],
        "github_link": "#"
    },
    {
        "name": "🏆 Kaggle OBSS AI Intern Deep Learning Datathon 2025",
        "description": "Built an image classification model using Kaggle datasets. Utilized pre-trained models and transfer learning to improve classification accuracy.",
        "technologies": ["Deep Learning", "Transfer Learning", "Kaggle", "Image Classification"],
        "github_link": "#"
    },
    {
        "name": "💰 Derin-ogrenme-ile-kredi-riski-analizi",
        "description": "Deep learning based credit risk analysis project implementing advanced neural networks for financial risk assessment.",
        "technologies": ["Deep Learning", "Financial Analysis", "Risk Assessment"],
        "github_link": "https://github.com/ozalpslan/Derin-ogrenme-ile-kredi-riski-analizi"
    },
    {
        "name": "🐍 Akbank Python Bootcamp Project",
        "description": "Comprehensive project developed during Akbank Python Bootcamp, demonstrating object-oriented programming principles.",
        "technologies": ["Python", "OOP", "Software Development"],
        "github_link": "https://github.com/ozalpslan/Akbank-python-bootcamp-projesi"
    },
    {
        "name": "🌐 Streamlit Portfolio Website",
        "description": "This interactive portfolio website built with Streamlit to showcase projects and professional experience.",
        "technologies": ["Streamlit", "Python", "Web Development"],
        "github_link": "https://github.com/ozalpslan/streamlit"
    }
]

for project in project_data:
    st.markdown(f"""
    <div class="project-card">
        <h3>{project["name"]}</h3>
        <p>{project["description"]}</p>
        <p><strong>Technologies:</strong> {", ".join(project["technologies"])}</p>
        <a href="{project["github_link"]}" target="_blank">🔗 View on GitHub</a>
    </div>
    """, unsafe_allow_html=True)

# Experience & Education Section
st.markdown('<div id="experience-education"></div>', unsafe_allow_html=True)
st.header("💼 Experience & Education")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🏢 Internships")
    
    st.markdown("**QNB Finansbank Intern** (07/2024 - 08/2024)")
    st.write("• C# programming and web development focus")
    st.write("• Application design and software solutions")
    st.write("• Financial technology insights")
    
    st.markdown("**Denizbank Denizasiri Intern** (02/2024 - 03/2024)")
    st.write("• Data Science and AI fundamentals")
    st.write("• Financial sector technology applications")
    st.write("• Analytical thinking development")

with col2:
    st.subheader("🎓 Education")
    st.markdown("**Computer Science 3rd Grade**")
    st.write("• CGPA: 3.38")
    st.write("• Istanbul University, Istanbul/Turkey")
    st.write("• Focus on Machine Learning and Data Engineering")

# Certifications Section
st.markdown('<div id="certifications"></div>', unsafe_allow_html=True)
st.header("🏆 Certifications")

certifications = [
    ("AWS Certified Cloud Practitioner", "2025", "☁️"),
    ("DataCamp – AI Engineer for Data Scientists Associate", "2025", "🤖"),
    ("Dr. Angela Yu – Full-Stack Web Development Bootcamp", "2025", "🌐"),
    ("QNB Finansbank – C# & Web Development", "2024", "💻"),
    ("BilgeAdam – Advanced Excel Certificate", "2025", "📊"),
    ("Akbank – Python Bootcamp", "2024", "🐍"),
    ("Turkcell Geleceği Yazanlar – Python 101-401", "2024", "📚")
]

col1, col2 = st.columns(2)
for i, (cert, year, icon) in enumerate(certifications):
    if i % 2 == 0:
        col1.markdown(f"{icon} **{cert}** ({year})")
    else:
        col2.markdown(f"{icon} **{cert}** ({year})")

# Contact Section
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.header("📞 Contact")

st.markdown("""
<div class="contact-info">
    <h3>Let's Connect!</h3>
    <p>📧 <strong>Email:</strong> ozalpslan@gmail.com</p>
    <p>📱 <strong>Phone:</strong> +90 538 061 97 10</p>
    <p>💼 <strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/alper-ozarslan-821361201/" target="_blank" style="color: white;">linkedin.com/in/alper-ozarslan-821361201</a></p>
    <p>🐙 <strong>GitHub:</strong> <a href="https://github.com/ozalpslan" target="_blank" style="color: white;">github.com/ozalpslan</a></p>
</div>
""", unsafe_allow_html=True)


