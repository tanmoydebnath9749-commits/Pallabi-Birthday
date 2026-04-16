import streamlit as st
import base64
from streamlit_lottie import st_lottie
import requests

# Page configuration
st.set_page_config(page_title="Happy Birthday Pallabi!", page_icon="🎂")

# --- Guaranteed Music Logic ---
def play_background_music(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            # Eita ekta invisible player jeta session_state diye maintain hobe
            # Loop attribute deoa ache jate gaan na thame
            st.markdown(
                f"""
                <audio id="bday_audio" loop autoplay>
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                <script>
                    // Streamlit er parent window te audio play korar force logic
                    var audio = window.parent.document.getElementById("bday_audio");
                    if (audio) {{
                        audio.play().catch(function(error) {{
                            console.log("Autoplay blocked, waiting for click...");
                        }});
                    }}
                </script>
                """,
                unsafe_allow_html=True
            )
    except Exception as e:
        st.error("Music file ('music.mp3') load hote problem hochhe!")

# Animations load function
def load_lottieurl(url):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Load animations
lottie_love = load_lottieurl("https://lottie.host/86369062-8e12-4040-9759-9941a310c81d/T6x5X6mYj3.json")
lottie_cake = load_lottieurl("https://lottie.host/842245b7-7e61-460b-8012-663832c326d9/A7HwF8rG5p.json")
lottie_gift = load_lottieurl("https://lottie.host/868779a5-738a-449e-8761-0f7962489814/Vf5K9j0X9A.json")
lottie_panda = load_lottieurl("https://lottie.host/5f583e74-0f31-412d-a2f0-94d306b3e839/T1kK0Hh9eB.json")

if 'page' not in st.session_state:
    st.session_state.page = 1

# --- Display Logic ---

# Page 1: Passcode
if st.session_state.page == 1:
    st.markdown("<h1 style='text-align: center;'>A Surprise for...</h1>", unsafe_allow_html=True)
    if lottie_love:
        st_lottie(lottie_love, height=300)
    st.markdown("<h1 style='color: #FF1493; text-align: center;'>PALLABI 💖</h1>", unsafe_allow_html=True)
    
    passcode = st.text_input("Enter Passcode (2204):", type="password")
    if st.button("Unlock 🗝️"):
        if passcode == "2204":
            st.session_state.page = 2
            st.rerun()
        else:
            st.error("Bhul password! Thik kore enter koro.")

# Page 2: One More Step (Music Starts Globally Here)
elif st.session_state.page == 2:
    play_background_music("music.mp3") # Music starts eikhan theke
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 60px; color: #FF69B4;'>One More Step...</h1>", unsafe_allow_html=True)
    if lottie_panda:
        st_lottie(lottie_panda, height=300)
    
    if st.button("Click to see the surprise! ✨", use_container_width=True):
        st.session_state.page = 3
        st.rerun()

# Page 3: Birthday Wish & Photo
elif st.session_state.page == 3:
    play_background_music("music.mp3")
    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>Happy Birthday, Pallabi! 🎂 Scroll Down</h1>", unsafe_allow_html=True)
    
    try:
        st.image("pallavi.jpeg", caption="The Birthday Queen 👑", use_container_width=True)
    except:
        st.info("Eikhane 'pallavi.jpeg' chobi ta thakbe.")

    if lottie_cake:
        st_lottie(lottie_cake, height=300)
    
    st.balloons()
    if st.button("Open Your Special Gift 🎁"):
        st.session_state.page = 4
        st.rerun()

# Page 4: Message
elif st.session_state.page == 4:
    play_background_music("music.mp3")
    st.title("A Message from My Heart ❤️")
    if lottie_gift:
        st_lottie(lottie_gift, height=250)
    st.markdown("### My Dearest Pallabi, \n Tui amar jibone ashar por theke sob kichu bodle gachhe...tui amar jibone sobtheke boro gift...ajker dinta tor kache special...❤️enjoy kor...ar sobsomoy hasi khusi thak...etai chai...tor hasi ta amar boro priyo....😊ar onno kotha bole tor mood kharap korbo nha sudhu etai boli valo thakis...tor tanmoy...😊")
    
    if st.button("See Your Memories 📸"):
        st.session_state.page = 5
        st.rerun()

# Page 5: Memories
elif st.session_state.page == 5:
    play_background_music("music.mp3")
    st.title("Your Beautiful Memories 📸")
    col1, col2 = st.columns(2)
    try:
        with col1:
            st.image("pallavi2.jpeg")
            st.image("pallavi3.jpeg")
        with col2:
            st.image("pallavi4.jpeg")
            st.image("pallavi5.jpeg")
    except:
        st.info("Photos eikhane thakbe.")

    if st.button("Start Again ❤️"):
        st.session_state.page = 1
        st.rerun()