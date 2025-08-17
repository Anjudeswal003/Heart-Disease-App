import streamlit as st

# ----------------- PAGE CONFIG -----------------
st.set_page_config(
    page_title="Login | Heart Health",
    page_icon="❤",
    layout="wide"
)

# ----------------- HIDE SIDEBAR -----------------
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
        else:
            st.error("Invalid email or password ❌")

# ----------------- STOP UNTIL LOGIN -----------------
if not st.session_state.logged_in:
    st.stop()

# ----------------- MAIN APP -----------------
tabs = st.tabs(["🏠 Dashboard", "🔍 Predict", "💡 Health Tips"])

with tabs[0]:
    st.header("🏠 Dashboard")
    st.write("Welcome to your Heart Health Dashboard!")
    # Dashboard content yahan add karein

with tabs[1]:
    st.header("🔍 Predict")
    st.write("Heart disease prediction form goes here.")
    # Predict tab content yahan add karein

with tabs[2]:
    st.header("💡 Health Tips")
    st.write("All heart health tips go here.")
    # Health Tips tab content yahan add karein
