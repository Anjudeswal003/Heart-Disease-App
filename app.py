import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Page config
st.set_page_config(layout="wide", page_title="Login | Heart Health", page_icon="❤", initial_sidebar_state="collapsed")

# Hide sidebar toggle
st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
        [data-testid="collapsedControl"] {display: none;}
    </style>
""", unsafe_allow_html=True)

# Initialize login state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Layout
left_col, right_col = st.columns([1, 1], gap="large")

with left_col:
    st.markdown("""
        <div style='margin-top: 80px; text-align: center; font-size: 45px; font-weight: bold; color: red;'>
            ❤️ Heart Health <br> Prediction ❤️
        </div>
    """, unsafe_allow_html=True)

with right_col:
    st.markdown("<h2 style='text-align: center; margin-top: 50px;'>Login</h2>", unsafe_allow_html=True)
    email = st.text_input("Email", key="email")
    password = st.text_input("Password", type="password", key="password")
    login = st.button("Login")

    if login:
        if email == "admin@gmail.com" and password == "admin123":
            st.session_state.logged_in = True
            st.success("Login successful! 🎉")
            switch_page("Dashboard")  # Automatically open Dashboard page
        else:
            st.error("Invalid email or password ❌")
