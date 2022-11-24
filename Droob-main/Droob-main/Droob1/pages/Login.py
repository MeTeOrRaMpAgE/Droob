import streamlit as st
import sqlite3

st.set_page_config(page_title="Droobツ - Login", page_icon="person-fill-lock", layout="centered", initial_sidebar_state="auto")

#Login widget

st.subheader("Login")
loginname = st.text_input("Username", key="loginname")
loginpwd = st.text_input("Password", key="loginpwd", type="password")
login = st.button("Login")


#Sign up widget

st.subheader("Don't have an account? Sign up")
registername = st.text_input("Username", key="signupname")
registerpwd = st.text_input("Password", key="signuppwd", type="password")
signup = st.button("Sign Up")

if signup:
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (regusername text, regpwd text);')
    cursor.execute("INSERT INTO users VALUES (?, ?)", (registername, registerpwd))
    
    conn.commit()
    st.success("Account created!")

    
        

if login:
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute("SELECT regusername, regpwd FROM users WHERE regusername='"+loginname+"' AND regpwd='"+loginpwd+"'")
    logresults = cursor.fetchall()


    conn.commit()

    if len(logresults) >= 1 :
        st.success("Logged in")
        loggedInFlag = True
    else:
        st.error("Login failed. Are you sure you've created an account?")
    
    
#APP

