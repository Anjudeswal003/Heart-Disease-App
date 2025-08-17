import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Login | Heart Health",
    page_icon="❤",
    layout="wide"
)

# Hide sidebar
st.markdown("""
<style>
[data-testid="stSidebar"] {display: none;}
[data-testid="collapsedControl"] {display: none;}
</style>
""", unsafe_allow_html=True)

# ----------------- SESSION STATE -----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ----------------- LOGIN FORM -----------------
left_col, right_col = st.columns([1, 1], gap="large")

with left_col:
    st.markdown("""
    <div style='margin-top: 80px; text-align: center; font-size: 45px; font-weight: bold; color: red;'>
        ❤️ Heart Health <br> Prediction ❤️
    </div>
    """, unsafe_allow_html=True)

with right_col:
    st.markdown("<h2 style='text-align: center; margin-top: 50px;'>Login</h2>", unsafe_allow_html=True)
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if email == "admin@gmail.com" and password == "admin123":
            st.session_state.logged_in = True
            st.success("Login successful! 🎉")
            switch_page("Dashboard")  # ✅ Directly open Dashboard file
        else:
            st.error("Invalid email or password ❌")
