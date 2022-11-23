import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="Droobツ - Dashbaord", page_icon=None)
st.title("Welcome to Droobツ!")
st.subheader("Your all in one application for club event updates!")

import time
import requests


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url_hello = "https://assets5.lottiefiles.com/packages/lf20_V9t630.json"
lottie_hello = load_lottieurl(lottie_url_hello)



st_lottie(lottie_hello, key="hello")




def eventWidget(eventName, eventDate, eventDetails, eventLink):
    st.write(eventName)
    st.write(eventDate)
    st.write(eventDetails)
    st.write(eventLink)

