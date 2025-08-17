import streamlit as st

# ---------------- CSS Styling ----------------
st.markdown("""
    <style>
    /* Space between tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
    }
             /* Top padding remove karega */
    .block-container {
        padding-top: 0rem !important;
    }
    div[data-testid="stVerticalBlock"] {
        padding-top: 0rem !important;
    }
    /* Tab text styling */
    .stTabs [data-baseweb="tab"] {
        font-size: 18px;
        padding: 14px 24px;
        font-weight: 600;
        color: #1B263B;
        border-radius: 8px 8px 0 0;
        background-color: #F4F6F8;
    }
    /* Active tab */
    .stTabs [aria-selected="true"] {
        background-color: #FF6F61;
        color: white !important;
        border-bottom: 3px solid +9
    }
    /* Margin between header and tabs */
    div[data-testid="stTabs"] {
        margin-top: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- Rest of your code ----------------

# Page config

st.markdown("""
    <style>
    .block-container {
        padding-top: 0px !important;
        margin-top: -40px !important;
    }
    header[data-testid="stHeader"] {
        height: 0px;
        visibility: hidden;
    }
    </style>
""", unsafe_allow_html=True)

# Hide sidebar & menu
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        #MainMenu, header, footer {
            visibility: hidden;
        }
        .block-container {
            padding-top: 0rem;
            max-width: 95%;
            margin: auto;
        }
        body {
            background-color: #FFFFFF;
        }
    </style>
""", unsafe_allow_html=True)

# Tab styles
st.markdown("""
    <style>
    .stTabs [data-baseweb="tab"] {
        font-size: 24px;
        padding: 14px 24px;
        font-weight: 600;
        color: #1B263B;
        border-radius: 15px 15px 0 0;
    }
    .stTabs [aria-selected="true"] {
        background-color: #FF6F61;
        color: white !important;
        border-bottom: 3px solid #E64A19;
    }
    </style>
""", unsafe_allow_html=True)

# Header strip
st.markdown("""
    <div style='background-color: #00796B; padding: 15px; border-radius: 10px; display: flex; justify-content: space-between; align-items: center;'>
        <div style='display: flex; align-items: center;'>
            <div style='width: 80px; height: 80px; border-radius: 50%; background-color: white; display: flex; align-items: center; justify-content: center; margin-right: 20px;'>
                <span style='font-size: 36px;'>💓</span>
            </div>
            <h1 style='color: white; margin: 0; font-weight: 700;'>Heart Health Prediction</h1>
        </div>
    </div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3 = st.tabs(["🏠 Home", "🔍 Predict", "💡 Health Tips"])
st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)

# HOME TAB
from pathlib import Path

with tab1:
    st.markdown("## 🫀 <span style='color:#1B263B; font-weight:700;'>What is the Heart Disease?</span>", unsafe_allow_html=True)
    st.markdown(
        "<p style='font-size:16px;'>The heart is a fist-sized organ that pumps blood throughout your body. Its your circulatory systems main organ. Muscle and tissue make up this powerhouse organ. Your heart contains four muscular sections (chambers) that briefly hold blood before moving it. Electrical impulses make your heart beat, moving blood through these chambers. Your brain and nervous system direct your heart’s function.</p>",
        unsafe_allow_html=True
    )

    st.markdown("### Function", unsafe_allow_html=True)
    st.markdown("### 🫀 What is the function of the Heart ?", unsafe_allow_html=True)
    st.markdown("""
    Your heart's main function is to move blood throughout your body. Blood brings oxygen and nutrients to your cells. It also takes away carbon dioxide and other waste so other organs can dispose of them.

    Your heart also:
    - Controls the rhythm and speed of your heart rate.
    - Maintains your blood pressure.

    Your heart works with these body systems to control your heart rate and other body functions:

    **Nervous system:** Helps control your heart rate. It sends signals that tell your heart to beat slower during rest and faster during stress.  
    **Endocrine system:** Sends out hormones that tell your blood vessels to constrict or relax, which affects your blood pressure. Hormones from your thyroid gland can also tell your heart to beat faster or slower.
    """, unsafe_allow_html=True)

    # Anatomy with image on right side
    st.markdown("## 🧠 Anatomy", unsafe_allow_html=True)

    col_left, col_right = st.columns([2, 1])

    with col_left:
        st.markdown("### The chambers and valves of the heart", unsafe_allow_html=True)
        st.write("Blood moves through chambers inside your heart.")

        st.markdown("### What are the parts of the heart?", unsafe_allow_html=True)
        st.write("Walls, Chambers, Valves, Blood vessels, and an Electrical conduction system.")

        st.markdown("### Heart walls", unsafe_allow_html=True)
        st.write("- Endocardium: Inner layer.")
        st.write("- Myocardium: Muscular middle layer.")
        st.write("- Epicardium: Protective outer layer.")

        st.markdown("### Heart chambers", unsafe_allow_html=True)
        st.write("Right Atrium, Right Ventricle, Left Atrium, Left Ventricle.")

        st.markdown("### Heart valves", unsafe_allow_html=True)
        st.write("They open and close to allow blood flow and prevent backward flow.")

        st.markdown("### Blood vessels", unsafe_allow_html=True)
        st.write("- Arteries carry oxygen-rich blood.")
        st.write("- Veins carry oxygen-poor blood.")
        st.write("- Capillaries exchange oxygen and nutrients.")

        st.markdown("### Coronary arteries", unsafe_allow_html=True)
        st.write("They supply blood to the heart muscle itself.")

        st.markdown("### Electrical conduction system", unsafe_allow_html=True)
        st.write("Controls the rhythm and pace of your heartbeat.")

        st.markdown("### Where is your heart located?", unsafe_allow_html=True)
        st.write("In the front of your chest, slightly to the left, between your lungs.")

        st.markdown("### What does your heart look like?", unsafe_allow_html=True)
        st.write("A bit like an upside-down pyramid with rounded edges.")

        st.markdown("### How big is your heart?", unsafe_allow_html=True)
        st.write("About the size of your fist, weighing ~10 ounces.")

    with col_right:
        img_path = Path(__file__).parent / ".." / "static" / "images" / "heart_anatomy.png"
        img_path = img_path.resolve()
        if img_path.exists():
            st.image(str(img_path), caption="Major parts of the heart", use_container_width=True)
        else:
            st.warning(f"Image not found at: {img_path}")

    st.markdown("## ❤️ Conditions and Disorders", unsafe_allow_html=True)

    st.markdown("### Common Conditions", unsafe_allow_html=True)
    st.write("Arrhythmia, Cardiomyopathy, Heart failure, Coronary artery disease, Heart attack, Valve disease, High BP, High cholesterol, Pericarditis.")

    st.markdown("### Symptoms", unsafe_allow_html=True)
    st.write("Chest pain, palpitations, dizziness, shortness of breath, fatigue, swelling.")

    st.markdown("### Tests", unsafe_allow_html=True)
    st.write("BP, ECG, Echo, X-ray, Blood tests, CT, MRI, Stress test.")

    st.markdown("### Treatments", unsafe_allow_html=True)
    st.write("Medicines, lifestyle changes, pacemakers, surgeries.")

    st.markdown("---")
    st.subheader("📊 Heart Health Stats (Sample)")
    col1, col2, col3 = st.columns(3)
    col1.metric("Avg Heartbeat", "72 BPM", "Normal")
    col2.metric("Blood Pressure", "120/80 mmHg", "Ideal")
    col3.metric("Cholesterol Risk", "200+", "- Risky if LDL is High")


# PREDICT TAB
with tab2:
    st.subheader("🔍 Heart Disease Prediction Form")
    st.markdown("<p style='font-size:16px;'>Fill the form below to check your heart health status.</p>", unsafe_allow_html=True)

    # Input fields
    age = st.slider("Age", 18, 100, 30)
    sex = st.radio("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=80, max_value=200, value=120)
    chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=400, value=200)
    fbs = st.radio("Fasting Blood Sugar > 120 mg/dl?", ["Yes", "No"])
    restecg = st.selectbox("Resting ECG Results", ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"])
    thalach = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, value=150)
    exang = st.radio("Exercise Induced Angina?", ["Yes", "No"])

    # Prediction
    if st.button("Predict"):
        risk_score = 0
        if age > 50: risk_score += 1
        if cp == "Asymptomatic": risk_score += 1
        if trestbps > 140: risk_score += 1
        if chol > 240: risk_score += 1
        if fbs == "Yes": risk_score += 1
        if exang == "Yes": risk_score += 1

        if risk_score >= 3:
            result = "⚠️ High risk of heart disease. Please consult a doctor."
            color = "#ffcccc"  # light red
            text_color = "#b30000"
        else:
            result = "✅ You seem to be at low risk. Stay healthy!"
            color = "#e0f7e9"  # light green
            text_color = "#1b5e20"

        # Result box
        st.markdown(
            f"""
            <div style='padding:20px; background-color:{color}; border-radius:12px; text-align:center; margin-top:20px;'>
                <h2 style='color:{text_color}; font-weight:bold;'>{result}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

    # --- Analytics Section (Now inside tab2) ---
    st.markdown("---")
    st.subheader("📊 Prediction Analytics")

    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    # Example DataFrame (dummy dataset)
    df = pd.DataFrame({
        "age": np.random.randint(30, 80, 100),
        "chol": np.random.randint(150, 350, 100),
        "trestbps": np.random.randint(100, 180, 100),
        "thalach": np.random.randint(100, 200, 100),
        "target": np.random.randint(0, 2, 100)  # 0 = Low risk, 1 = High risk
    })

    # --- Risk Distribution + Scatter plot side by side ---
    col1, col2 = st.columns(2)

    with col1:
        st.write("### Risk Distribution")
        fig1, ax1 = plt.subplots(figsize=(3,2))
        df["target"].value_counts().plot(kind="bar", ax=ax1, color=["green", "red"])
        ax1.set_xticklabels(["Low Risk", "High Risk"], rotation=0)
        ax1.set_ylabel("Count")
        st.pyplot(fig1, use_container_width=True)

    with col2:
        st.write("### Cholesterol vs Age")
        fig2, ax2 = plt.subplots(figsize=(3,2))
        scatter = ax2.scatter(df["age"], df["chol"], c=df["target"], cmap="bwr", alpha=0.7)
        ax2.set_xlabel("Age")
        ax2.set_ylabel("Cholesterol")
        plt.colorbar(scatter, ax=ax2, label="Risk (0=Low, 1=High)", shrink=0.6)
        st.pyplot(fig2, use_container_width=True)

# ------------------- 💡 HEALTH TIPS TAB (REPLACE YOUR OLD BLOCK) -------------------
# --- IMAGE HELPER FUNCTION ---
def show_image(img_name, caption=""):
    st.image(
        f"static/images/{img_name}",
        caption=caption,
        use_container_width=True
    )

# =============================
# HEALTH TIPS TAB
# =============================
with tab3:
    # Main title
    st.markdown("<h2 style='margin-top:0'>💡 How to Keep Your Heart Healthy</h2>", unsafe_allow_html=True)
    st.markdown(
        "<p style='font-size:16px'>Practical, science-backed tips to protect your heart—food, fitness, sleep, stress, habits, and more. Save the suggested images in <code>static/images/</code> with the same names to show them here.</p>",
        unsafe_allow_html=True
    )

    # --- 1) DIET ---
    c1, c2 = st.columns([2,1])
    with c1:
        st.markdown("### 🥗 Heart-Healthy Diet (DASH/Mediterranean) — What to Eat & Why")
        st.markdown("""
**Core Principles**
- 🥦 **Half plate** veggies + fruits (fiber, antioxidants)
- 🍞 **Whole grains**: oats, brown rice, whole-wheat roti/pasta
- 🫘 **Lean protein**: dals/beans, fish, skinless chicken, tofu, paneer (low-fat)
- 🥑 **Healthy fats**: olive/mustard oil (limit), nuts, seeds
- 🧂 **Low sodium**: taste with herbs, lemon, garlic; avoid processed foods
- 🧁 **Low sugar**: skip sodas, pastries; choose fruits/yogurt

**Best Daily Targets**
- Vegetables/Fruits: 5–9 servings  
- Whole grains: 3–4 servings  
- Protein: 2–3 servings  
- Low-fat dairy: 1–2 servings  
- Nuts/Seeds: small handful 5x/week

**Avoid/Limit:** red/processed meat, deep-fried snacks, bakery items, packaged chips, excess salt & sugar.
        """)
    with c2:
        show_image("diet_plate.png", "Balanced DASH/Mediterranean plate")

    # --- 2) EXERCISE PLAN ---
    c1, c2 = st.columns([2,1])
    with c1:
        st.markdown("### 🏃‍♀️ Exercise Plan — Cardio + Strength + Flexibility")
        st.markdown("""
**Weekly Goals**
- **Cardio:** 150–300 mins/week (brisk walk, cycling, swimming)
- **Strength:** 2–3 days/week (full body)
- **Flexibility & Balance:** 2–3 days/week (stretch/yoga)

**Simple Weekly Template**
- Mon: 30–40 min brisk walk + 10 min stretch  
- Tue: Full-body strength (squats, pushups, rows, core) ~30 min  
- Wed: 30–40 min cycling / jog  
- Thu: Yoga / mobility 20–30 min  
- Fri: 30–40 min brisk walk  
- Sat: Strength (legs/core/upper) 30 min  
- Sun: Leisure walk / rest
        """)
    with c2:
        show_image("exercise_plan.png", "Weekly heart-friendly workout split")

    # --- 3) STRESS MANAGEMENT ---
    c1, c2 = st.columns([2,1])
    with c1:
        st.markdown("### 🧘 Stress Management — Daily Calm Routine")
        st.markdown("""
**Mini-Routine (10–15 min)**
- 4–7–8 **breathing** × 5 rounds
- 5 min **mindfulness scan** (head→toe relax)
- 5 min **journaling** (3 gratitudes)

**Lifestyle Tips**
- Regular sleep/wake timing  
- Short breaks at work (Pomodoro)  
- Limit doom-scrolling & late caffeine
        """)
    with c2:
        show_image("stress_relief.png", "Breathe, stretch, reset")

    # --- 4) SLEEP HYGIENE ---
    c1, c2 = st.columns([2,1])
    with c1:
        st.markdown("### 🛌 Sleep Hygiene — 7–9 Hours Quality Sleep")
        st.markdown("""
**Do**
- Fixed sleep/wake time, dark & cool room  
- No screens 60 min before bed  
- Light dinner; finish 2–3 hrs before sleep  
- If awake >20 min, get up, read, go back relaxed  

**Avoid**
- Late caffeine, heavy meals, alcohol close to bedtime
        """)
    with c2:
        show_image("sleep_habits.png", "Simple sleep-friendly setup")

    # --- 5) QUIT SMOKING ---
    c1, c2 = st.columns([2,1])
    with c1:
        st.markdown("### 🚭 Quit Smoking/Tobacco — Immediate Heart Benefits")
        st.markdown("""
- 20 min: HR/BP begin to drop  
- 12 hrs: CO levels normalize  
- Weeks: circulation & lung function improve  
- 1 year: CHD risk halves vs smoker  

**Get Help**
- Set a Quit Date, remove triggers  
- Nicotine replacement (gum/patch) under guidance  
- Support groups / counseling
        """)
    with c2:
        show_image("quit_smoking.png", "Small steps → big wins")

    # --- 6) HYDRATION ---
    c1, c2 = st.columns([2,1])
    with c1:
        st.markdown("### 🥤 Hydration — Simple Rules")
        st.markdown("""
- Target **6–8 glasses/day** (more in hot weather/activity)  
- Prefer **water**, infused water, unsweetened tea  
- Limit sugary drinks & energy drinks
        """)
    with c2:
        show_image("hydration.png", "Hydration basics")

    # --- 7) MONITORING ---
    c1, c2 = st.columns([2,1])
    with c1:
        st.markdown("### 🩺 Regular Monitoring — What to Track & When")
        st.markdown("""
**At Home**
- **BP:** weekly if borderline/high  
- **Weight & Waist:** monthly  
- **Blood Sugar (if diabetic/pre):** as advised  

**Lab/Clinic (typical)**
- Lipid profile: 6–12 months  
- HbA1c (if diabetic): 3–6 months  
- ECG/Echo: as doctor advises
        """)
    with c2:
        show_image("monitoring.png", "Know your numbers")

    # --- 8) WARNING SIGNS ---
    c1, c2 = st.columns([2,1])
    with c1:
        st.markdown("### ⚠️ Warning Signs — Don’t Ignore")
        st.markdown("""
- Chest pressure/pain (heavy, squeezing)  
- Pain radiating to left arm/jaw/back  
- Shortness of breath, cold sweat, nausea  
- Sudden dizziness, fainting, irregular heartbeat  

👉 **Emergency? Call immediately. Do not self-drive.**
        """)
    with c2:
        show_image("warning_signs.png", "When to act fast")

    # --- 9) MEAL PLAN ---
    c1, c2 = st.columns([2,1])
    with c1:
        st.markdown("### 🍱 7-Day Heart-Healthy Meal Plan (Sample)")
        st.markdown("""
**Mon** – Oats + fruit | Dal-roti + salad | Veg khichdi + curd  
**Tue** – Poha + peanuts | Brown rice + rajma | Grilled paneer + veggies  
**Wed** – Upma + sambhar | Quinoa + chole | Fish (or tofu) + stir fry  
**Thu** – Eggs/Paneer bhurji + toast | Millet roti + dal + sabzi | Veg soup + multigrain toast  
**Fri** – Smoothie (curd+fruit+seeds) | Brown rice + sambar + veggies | Chicken breast / soy tikka + salad  
**Sat** – Idli + chutney | Roti + mix dal + bhindi | Veg pulao + raita  
**Sun** – Dalia + nuts | Grilled veg wrap | Light dinner + fruit bowl
        """)
    with c2:
        show_image("meal_plan.png", "Colorful weekly plate")

    # --- 10) WEEKLY WORKOUT ---
    c1, c2 = st.columns([2,1])
    with c1:
        st.markdown("### 🏋️‍♂️ Weekly Workout Split — Beginner Friendly")
        st.markdown("""
**Strength Day (30–35 min)**
- Squats/Chair squats 3×10  
- Pushups (inclined/knee) 3×8–10  
- Rows (band/dumbbell) 3×10  
- Glute bridge 3×12  
- Plank 3×20–30s  

**Cardio Day (30–40 min)**
- Brisk walk/jog/cycle at talkable pace  
- Cool down + light stretching
        """)
    with c2:
        show_image("workout_week.png", "Mix cardio + strength")

    # --- 11) BREATHING ---
    c1, c2 = st.columns([2,1])
    with c1:
        st.markdown("### 🫁 Breathing & Mindfulness — 5 to 10 Minutes")
        st.markdown("""
**4–7–8 Breathing**: Inhale 4s → Hold 7s → Exhale 8s × 5  
**Box Breathing**: 4-4-4-4 × 5  
**Body Scan**: Relax toes→head with slow breath
        """)
    with c2:
        show_image("breathing.png", "Calm breath patterns")

    # --- 12) GROCERY LIST ---
    c1, c2 = st.columns([2,1])
    with c1:
        st.markdown("### 🛒 Smart Grocery List — Heart-Friendly Staples")
        st.markdown("""
- **Grains:** oats, brown rice, quinoa, millets, whole wheat  
- **Proteins:** dals, beans, chickpeas, tofu, paneer (low-fat), eggs, fish  
- **Fats:** olive/mustard oil (mod), nuts (almond/walnut), seeds (flax/chia)  
- **Dairy:** low-fat milk/curd  
- **Extras:** herbs, spices, lemon, garlic
        """)
    with c2:
        show_image("grocery_list.png", "Stock the good stuff")

    # --- 13) DOs & DON'Ts ---
    c1, c2 = st.columns([2,1])
    with c1:
        st.markdown("### ✅ Do’s & Don’ts — Quick Checklist")
        st.markdown("""
**Do**
- Walk after meals (10–15 min)  
- Cook more at home  
- Read labels for **salt/sugar**  
- Take stairs, stand breaks  

**Don’t**
- Skip breakfast or overeat at night  
- Sit >60–90 min without moving  
- Smoke/vape/chew tobacco  
- Oversalt or oversugar food
        """)
    with c2:
        show_image("dos_donts.png", "Small habits → big results")

    # --- 14) MYTHS vs FACTS ---
    c1, c2 = st.columns([2,1])
    with c1:
        st.markdown("### 🧠 Myths vs Facts")
        st.markdown("""
**Myth:** Only older people get heart disease  
**Fact:** Risk factors can build from young age  

**Myth:** If BP feels OK, I can skip meds  
**Fact:** Always follow doctor’s plan  

**Myth:** Healthy food is bland  
**Fact:** Herbs & spices add flavor without salt  

**Myth:** Gym is mandatory  
**Fact:** Brisk walking works wonders
        """)
    with c2:
        show_image("myths_facts.png", "Know the truth")

    # --- 15) FAQs ---
    st.markdown("### ❓ FAQs")
    st.markdown("""
**Q1: Ghee/Butter allowed?**  
*A:* Very small amounts occasionally; prefer unsaturated oils.  

**Q2: Tea/Coffee?**  
*A:* In moderation; avoid late evening.  

**Q3: Cheat meal?**  
*A:* Occasionally, but portion-controlled and balanced day overall.  

**Q4: Supplements?**  
*A:* Only if prescribed (e.g., vitamin D/B12, omega-3 for some).
    """)

    st.success("🌟 A healthy heart means a healthier, happier you. Start today!")
