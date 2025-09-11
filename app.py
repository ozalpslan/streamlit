import streamlit as st

# Use st.set_page_config() for a custom page title and layout
st.set_page_config(page_title="Alper Ozarslan's Portfolio", layout="wide")

# --- HEADER SECTION ---
with st.container():
    st.image("profile_photo.jpg", width=200) # You'll need to add your photo file
    st.title("Alper Ozarslan")
    st.write("Machine Learning Student with MLOps Knowledge")
    st.write("3rd-year Computer Science student with practical experience in machine learning, deep learning, and data engineering.")
    st.write("[LinkedIn Profile](https://www.linkedin.com/in/alper-ozarslan-821361201/)")
    
# --- SKILLS SECTION ---
st.write("---")
st.header("Skills")
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Programming Languages")
    st.write("Python, C#, Javascript, Node.js, Java, R, C")
with col2:
    st.subheader("Python Libraries")
    st.write("Scikit-Learn, Pytorch, Pandas, Keras, Tensorflow, YOLO, OpenCV, Pycaret, Transformers, MLflow")
with col3:
    st.subheader("Tools & Databases")
    st.write("Git, Github, Linux, Docker, AWS Tools, MySQL, PostgreSQL, SQLite, MSSQL")
    
# --- PROJECTS SECTION ---
st.write("---")
st.header("Projects & Experiences")
st.subheader("Yildiz Technical University Machine Learning Datathon 2025")
st.write("Built a machine learning model to predict maintenance needs and failures using real factory machine data.")
st.write("Skills: Data Preprocessing, Feature Engineering, Predictive Maintenance")
# You can add more projects in a similar way

# --- CERTIFICATES SECTION ---
st.write("---")
st.header("Certificates")
st.subheader("AWS Certified Cloud Practitioner")
st.write("Demonstrated solid understanding of AWS core services like EC2, S3, RDS, Lambda, and more.")
# Add other certificates here
