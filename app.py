import streamlit as st

# Page config (sirf ek baar yahi pe rakhna hai)
st.set_page_config(
    layout="wide",
    page_title="Login | Heart Health",
    page_icon="❤",
    initial_sidebar_state="collapsed"  # sidebar auto collapsed
)

# CSS to completely hide sidebar toggle (optional)
hide_sidebar_style = """
    <style>
        [data-testid="stSidebar"] {display: none;}
        [data-testid="collapsedControl"] {display: none;}
    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)

# Layout: 2 Columns (top align)
left_col, right_col = st.columns([1, 1], gap="large")

# Left Column — Heading (parallel to login form, top aligned)
with left_col:
    st.markdown("""
        <div style='margin-top: 80px; text-align: center; font-size: 45px; font-weight: bold; color: red;'>
            ❤️ Heart Health <br> Prediction ❤️
        </div>
    """, unsafe_allow_html=True)

# Right Column — Login Form
with right_col:
    st.markdown("<h2 style='text-align: center; margin-top: 50px;'>Login</h2>", unsafe_allow_html=True)

    # Input fields
    email = st.text_input("Email", key="email")
    password = st.text_input("Password", type="password", key="password")

    # Login button
    login = st.button("Login")

    # Validation
    if login:
        if email == "admin@gmail.com" and password == "admin123":
            st.success("Login successful! 🎉")

            # Directly open Dashboard page (no button, no link)
            st.switch_page("pages/Dashboard.py")
        else:
            st.error("Invalid email or password ❌")



