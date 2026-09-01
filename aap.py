from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie




st.set_page_config(page_title="My webpage",page_icon=":tada:",layout="wide")


    
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

    
lottie_coding = load_lottieurl("https://lottie.host/8e9ce5db-cfd7-40dd-84db-3ba776b29f5c/SyCbfqoUiu.json")

image_contact_form=Image.open("code.png")
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")


with st.container():
    st.subheader("Hi I am rayen :wave: ")
    st.title("A student from LPA")
    st.write("I am verry passionate about becoming a freeelencer with makni")
    st.write("[More info>] (https://www.instagram.com/rayen___neji?igsi=MTJxOW4wNDIwMjdjcg%3D%3D)")
    st.write("[drop a folow to mkni>] (https://www.instagram.com/rayen_makni_/?utm_source=ig_web_button_share_sheet)")



        
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)

    with left_column:
        st.header("My Porftfolio:")
        st.write("##")
        st.write(
            """
            I am a 17 years old junior coder, if you need any service in:

            *creating a web site  
            *graphic post design  
            *cleaning your data  
            *web automations and scripts.

            Feel free to contact us :wave:
            """
        )
    with right_column:
            st_lottie(lottie_coding, height=300, key="coding")


with st.container():
        st.write("---")
        image_column,text_column=st.columns((1,2))

        with image_column:

            st.image(image_contact_form)

        with text_column:
            st.subheader("Lean how to code:")
            st.write(

                """
                learn how to create a web site with python and streamlit
                """
               )
            st.markdown("[Watch tuto>] (https://youtu.be/VqgUkExPvLY?si=aRfVM_Y9qJ5Tza7-)")


with st.container():
    st.write("---")
    st.header("Contact Me :email:")
    st.write("##")
    contact_form="""
    <form action="https://formsubmit.co/nejirayen710@gmail.com" method="POST" target="_blank">
       <input type="hidden" name="_captcha" value="false">
       <input type="text" name="name" placeholder="your name"  required>
       <input type="email" name="email" placeholder="your email" required>
       <textarea name="message" placeholder="your message here " required></textarea>
       <button type="submit">Send</button>
    </form>
    """
    left_column,right_column=st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()





        
