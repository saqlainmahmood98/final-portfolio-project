import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code!= 200:
        return None
    return r.json()

# LOAD ASSETS
lottie_coding = load_lottieurl("https://lottie.host/48e588c5-daa8-413d-932a-a06a5170ad4d/0N4IavDhb6.json")
img_football = Image.open("images/origi.jpeg")
img_machu_picchu = Image.open("images/Machu_Picchu.jpg")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# Navigation bar
st.sidebar.title("Navigation")
pages = ["Home", "About Me", "Interests & Hobbies", "Gallery", "Contact Us"]
page = st.sidebar.selectbox("Select a page", pages)

# HEADER
st.markdown("""
<header style="text-align: center; padding: 20px;">
    <p>Designed and Maintained by Saqlain</p>
</header>
""", unsafe_allow_html=True)

if page == "Home":
    # HOME PAGE
    with st.container():
        st.write("---")
        st.subheader("My Webpage :wave:")
        st.title("Welcome to my webpage!")
        st.write("This is my homepage. You can navigate to other pages using the sidebar.")

elif page == "About Me":
    # ABOUT ME PAGE
    with st.container():
        st.write("---")
        st.header("Who am I?")
        st.write("My name is Saqlain, I am 26 years old and I am from Bradford, England. I attended the University of Huddersfield studying Accountancy and Finance but recently I have been interested in computing and studying coding languages such as Python and Javascript. Slowly I became obsessed with the idea of building something out of codes and now I am dedicated on building a career where I can do just that.")
        with st.container():
            st_lottie(lottie_coding, height=300, key="coding")

elif page == "Interests & Hobbies":
    # INTERESTS & HOBBIES PAGE
    with st.container():
        st.write("---")
        st.header("My Interests and Hobbies")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_football)
        with text_column:
            st.subheader("Sports :sports_medal:")
            st.write("I love all kinds of sports, I enjoy tennis, swimming, table tennis, badminton, golf but my favourite sport would be footbal and as you can probably tell from the picture, I support Liverpool Football Club. Growing up I was a very active and sporty person in school achieving multiple trophies in football and olympic themed sports mainly the 100 meter sprint. I am incredibly proud of my achievements as they were not easy as I was competing with many students including thos from surrounding schools in the area.")
        with st.container():
            image_column, text_column = st.columns((1, 2))
            with image_column:
                st.image(img_machu_picchu)
            with text_column:
                st.subheader("Exploring :world_map:")
                st.write("I love to travel and explore the world. I have been to many countries but my favourite place that I have visited is Croatia simply because of the views and the pure beauty of the country. One day I hope to travel to Peru and see Machu Picchu.")

elif page == "Gallery":
    # GALLERY PAGE
    with st.container():
        st.write("---")
        st.header("Gallery")
        st.write("##")
        st.image(img_football)
        st.write("##")
        st.image(img_machu_picchu)


elif page == "Contact Us":
    # CONTACT US PAGE
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")
        contact_form = """
        <form action="https://formsubmit.co/your@email.com" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <input type="text" name="name" placeholder="Your Name" required>
             <input type="email" name="email" placeholder="Your Email" required>
             <textarea name="message" placeholder="Your message here" required></textarea>
             <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()

# FOOTER
st.markdown("""
<footer style="text-align: center; padding: 20px; position: fixed; bottom: 0; width: 100%;">
    <p>&copy; 2024 Saqlain</p>
</footer>
""", unsafe_allow_html=True)