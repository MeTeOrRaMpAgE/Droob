import streamlit as st
from Dashboard import eventWidget



music, art, dance, drama, fashion, = st.tabs(["Music", "Art", "Dance", "Drama", "Fashion"])

with music:
    st.subheader("Here are all music events taking place!")
    eventWidget("School of Rock", "14/11/22,","Time limit: 12 minutes including setup and sound check.      Venue: Auditorium", "https://images.google.com/?gws_rd=ssl")
    eventWidget("Sonata", "18/11/22,","Time limit: 6 minutes including setup and sound check.      Venue: Auditorium", "https://images.google.com/?gws_rd=ssl")
    eventWidget("Raghasudha", "14/11/22,","Time limit: 12 minutes including setup and sound check.      Venue: Auditorium", "https://images.google.com/?gws_rd=ssl")
    eventWidget("Light Vocals", "14/11/22,","Time limit: 12 minutes including setup and sound check.      Venue: Auditorium", "https://images.google.com/?gws_rd=ssl")

with art:
    st.subheader("Here are all art events taking place!")
    eventWidget("Art competition", "14/11/22,","Theme: Pollution and things we can do to reduce it.      Venue: KG ground", "https://images.google.com/?gws_rd=ssl")
    eventWidget("Nazariya", "14/11/22,","Theme: Superheroes      Venue: Auditorium", "https://images.google.com/?gws_rd=ssl")

with dance:
    st.subheader("Here are all dance events taking place!")
    eventWidget("Filmy Dance", "14/11/22,","Time limit: 3 mins.      Venue: Auditorium", "https://images.google.com/?gws_rd=ssl")
    eventWidget("Fusion Dance", "14/11/22,","Time limit: 3 mins.      Venue: Auditorium", "https://images.google.com/?gws_rd=ssl")
    eventWidget("Classical Dance", "14/11/22,","Time limit: 3 mins.      Venue: Auditorium", "https://images.google.com/?gws_rd=ssl")

with drama:
    st.subheader("Here are all drama events taking place!")
    eventWidget("Play Along", "14/11/22,","Time limit: 15 mins.      Venue: Auditorium", "https://images.google.com/?gws_rd=ssl")
    eventWidget("Stand up comedy", "14/11/22,","Time limit: 7mins.      Venue: Auditorium", "https://images.google.com/?gws_rd=ssl")

with fashion:
    st.subheader("Here are all fashion events taking place!")
    eventWidget("Fashion Show", "14/11/22,","Time limit: 10 mins.      Venue: Auditorium", "https://images.google.com/?gws_rd=ssl")