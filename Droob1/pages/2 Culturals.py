import streamlit as st
import Dashboard



music, art, dance, drama, fashion, = st.tabs(["Music", "Art", "Dance", "Drama", "Fashion"])

with music:
    st.subheader("Here are all music events taking place!")
    Dashboard.eventWidget("School of Rock", "14/11/22,","Blah Blah Blah", "https://images.google.com/?gws_rd=ssl")

