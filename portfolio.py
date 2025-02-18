import streamlit as st
from PIL import Image
import base64

# Page configuration
st.set_page_config(page_title="Atik Zafar - Portfolio", page_icon=":guardsman:", layout="wide")

# Side Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "About Me", "Resume", "Achievements", "Contact"])

# Home Page
if menu == "Home":
    st.title("Welcome to My Portfolio!")
    st.write("Hello, I am **Atik Zafar**, an aspiring UPSC student with a passion for data science, marketing, and leadership.")
    st.write("This portfolio showcases my journey, achievements, and projects.")
    st.image("https://drive.google.com/file/d/1VCXlHAbjIlZmXwwZRIulMBY18QOC9jFZ/view?usp=sharing", caption="", use_column_width=True)

# About Me
elif menu == "About Me":
    st.title("About Me")
    st.write("""
        Hello! I'm **Atik Zafar**, an aspiring **UPSC candidate** and a data science enthusiast.
        
        - **Current Roles**: Co-Secretary of the Career Development Cell at DIT University
        - **Education**: B.Tech CSE at DIT University (2022-2026)
        - **Scholarship**: Reliance Foundation Scholarship (UG) - ₹2 Lakh Awarded
        - **Technical Skills**: Java, C, C++, R, SQL, Tableau, MS Excel, Google Workspace, Adobe Illustrator, Canva, VN
        - **Languages**: English, Hindi, German (beginner)
        
        I have experience in designing marketing strategies, organizing career development programs, and working on sustainability projects. I'm also working on an innovative project to create ink from soot collected from silencers.
    """)
    st.image("https://i.postimg.cc/T33hwxNn/Screenshot-2025-02-14-at-3-24-13-PM.png", caption="Atik Zafar", width=200)

# Resume
elif menu == "Resume":
    st.title("My Resume")
    st.write("Download my latest resume below:")
    resume_link = "https://www.linkedin.com/in/atikzafar/"  # Replace with actual link
    st.markdown(f"[Download Resume]({resume_link})", unsafe_allow_html=True)

# Achievements
elif menu == "Achievements":
    st.title("My Achievements")
    st.write("Here are some of my key achievements:")
    
    achievements = [
        "First place in G20 Quiz organized by School of Physical Sciences, DIT",
        "First place in Engineer’s Shark Tank Startup Idea Competition, SOET, DIT University",
        "Reliance Foundation Scholarship (UG) - ₹2 Lakh Awarded",
        "Finalist at Zonal Debate Competition, ASISC Debate Competition Zonal",
        "Recipient of Prabhat Pratibha Samman for extraordinary academic prowess in ICSE X",
        "Finalist in 26th National Children's Science Congress",
        "Achieved Rank 1 at the district level in the Digital India quiz",
        "Third prize in PowerPoint presentation competition (National Workshop on World Ozone Day)",
        "Second prize in relay race",
    ]
    
    for achievement in achievements:
        st.write(f"- {achievement}")
    
    uploaded_image = st.file_uploader("Upload an Achievement Image", type=["jpg", "jpeg", "png"])
    if uploaded_image is not None:
        st.image(uploaded_image, caption="Achievement Image", use_column_width=True)

# Contact
elif menu == "Contact":
    st.title("Contact Me")
    st.write("""
        You can reach me through the following channels:
        - **Email**: atikzafar28@gmail.com
        - **LinkedIn**: [linkedin.com/in/atikzafar](https://linkedin.com/in/atikzafar)
        - **GitHub**: [github.com/atikzafar](https://github.com/atikzafar)
    """)
    
    # Contact Form
    contact_form = """
    <form action="https://formsubmit.co/atikzafar28@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your Name" required><br>
        <input type="email" name="email" placeholder="Your Email" required><br>
        <textarea name="message" placeholder="Your Message" required></textarea><br>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
