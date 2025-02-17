import streamlit as st
from PIL import Image
import base64

# Page configuration
st.set_page_config(page_title="My Portfolio", page_icon=":guardsman:", layout="wide")

# Side Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "About Me", "Resume", "Achievements", "Contact"])

# Home Page
if menu == "Home":
    st.title("Welcome to My Portfolio!")
    st.write("Hello, I am [Your Name], a passionate [Your Profession].")
    st.write("This is my personal portfolio website built with Streamlit.")
    st.image("https://i.postimg.cc/T33hwxNn/Screenshot-2025-02-14-at-3-24-13-PM.png", caption="A picture of me or my work", use_column_width=True)

# About Me
elif menu == "About Me":
    st.title("About Me")
    st.write("""
        Hello! I'm [Your Name]. I am a passionate software developer with experience in [languages, technologies].
        I love solving problems and learning new technologies.
        You can contact me through the form in the Contact section.
    """)
    st.image("https://i.postimg.cc/T33hwxNn/Screenshot-2025-02-14-at-3-24-13-PM.png", caption="A photo of me", width=200)

# Resume
elif menu == "Resume":
    st.title("My Resume")
    
    # Upload Resume PDF
    uploaded_file = st.file_uploader("Upload your Resume", type=["pdf"])
    if uploaded_file is not None:
        st.write("Here's my Resume:")
        st.download_button(
            label="Download Resume",
            data=uploaded_file,
            file_name="resume.pdf",
            mime="application/pdf",
        )

# Achievements
elif menu == "Achievements":
    st.title("My Achievements")
    
    # Upload Achievement Image(s)
    st.write("Here are some of my achievements:")
    uploaded_image = st.file_uploader("Upload an Achievement Image", type=["jpg", "jpeg", "png"])
    if uploaded_image is not None:
        st.image(uploaded_image, caption="Achievement Image", use_column_width=True)
        st.write("Achievement Description: [Description of the achievement]")

# Contact
elif menu == "Contact":
    st.title("Contact Me")
    st.write("""
        You can reach me through the following channels:
        - Email: [your.email@example.com]
        - LinkedIn: [your-linkedin]
        - GitHub: [your-github]
    """)
    
    # Contact Form (Basic)
    contact_form = """
    <form action="https://formsubmit.co/your-email@example.com" method="POST">
        <input type="text" name="name" placeholder="Your Name" required><br>
        <input type="email" name="email" placeholder="Your Email" required><br>
        <textarea name="message" placeholder="Your Message" required></textarea><br>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

