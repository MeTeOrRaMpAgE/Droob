import streamlit as st
from Dashboard import eventWidget

st.title("Academic Club Activities")

math, science, socials, mun, literary, cyber = st.tabs(["Math", "Science", "Social Science", "Model UN", "Literary", "Cyber"])

with math:
    eventWidget("Escape Room", "12/11/22", "Welcome to escape room. Time: 6th period in auditorium. Bring pencil pouch.", "https://docs.google.com/forms/u/0/")
    eventWidget("Quiz", "26/2/21", "Welcome to math quiz! Time: 4th 5th and 6th period in ER 2. Bring pencil pouch, diary and notebook.", "https://docs.google.com/forms/u/0/")
    eventWidget("Math puzzle", "1/2/23", "Welcome to math puzzle. Time: 7th and 8th period in Dance room.", "https://docs.google.com/forms/u/0/")


with science:
    eventWidget("Science Quiz", "12/11/22", "Welcome to science quiz. Time: 1st and 2nd period in auditorium. Bring pencil pouch.", "https://docs.google.com/forms/u/0/")

with socials:
    eventWidget("Eminence", "12/11/22", "Welcome to eminence. Time: 6th period in auditorium. Bring pencil pouch.", "https://docs.google.com/forms/u/0/")
with mun:
    eventWidget("Interhouse Mun", "12/11/22 and 13/11/22", "Welcome to interhouse Mun. Committees - UEFA, UNCCPCJ, CCC, HSC, UNHRC, Lok Sabha. Venue: auditorium. Electronics are allowed. However, internet usage is prohibited during committee.", "https://docs.google.com/forms/u/0/")
with literary:
    eventWidget("Pass it along", "18/11/22", "Welcome to pass it along. Time: 6th period in auditorium. Bring pencil pouch.", "https://docs.google.com/forms/u/0/")
    eventWidget("Riddle Room", "28/11/22", "Welcome to riddle room. Time: 6th period in auditorium. Bring pencil pouch.", "https://docs.google.com/forms/u/0/")
with cyber:
    eventWidget("Cyber gaming - Minecraft", "12/11/22", "Time: 6th period in computer lab.", "https://docs.google.com/forms/u/0/")
    eventWidget("Cyber gaming - Chrome Dino", "12/11/22", "Time: 6th period in computer lab.", "https://docs.google.com/forms/u/0/")
    eventWidget("Hackathon", "24/10/22", "Theme: Useless app", "https://docs.google.com/forms/u/0/")
    eventWidget("Competitive Coding", "23/6/22", "Time: 8th period.     Venue: Computer Lab", "https://docs.google.com/forms/u/0/")