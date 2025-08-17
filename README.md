#  Heart Health Prediction

A simple **Streamlit web application** to learn about heart health, predict conditions, and provide helpful tips for a healthy heart

## Features
- **Login Page:** Secure login with email & password.
- **Dashboard Tabs:**
  - **Home:** Learn about heart anatomy, functions, symptoms, and treatments.
  - **Predict:** Predict your heart health (model integration pending).
  - **Health Tips:** Tips to maintain a healthy heart.
    
##  Tech Stack  
  **Python** 
  **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn  
  **Streamlit** (for UI)
  
## create and activate virtual environment
    python -m venv .venv
    # for Windows
          .venv\Scripts\activate
    # macOS/Linux
          source .venv/bin/activate
  
## install dependencies
    pip install -r requirements.txt
 
## run the app
streamlit run app.py
## folder structure
heart_health_prediction/
│
├─ app.py                  # Login page (root folder)
├─ train_model.py          # ML model training script (root folder)
├─ pages/
│   └─ Dashboard.py        # Dashboard tabs page
├─ static/
│   └─ images/
│       └─ heart_anatomy.png # and all the remaining images , all are placed here
├─ heart.csv               # Dataset (root folder)
├─ model.pkl               # Trained model file (root folder)
├─ requirements.txt        # Python dependencies
└─ README.md               # Project documentation

