import pandas as pd
import streamlit as st
from datetime import datetime, timedelta

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="MIT Candidate Training Dashboard", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---- CUSTOM STYLING ----
st.markdown("""
    <style>
        :root { color-scheme: dark; }
        html, body, [data-testid="stApp"], [data-testid="stAppViewContainer"] {
            background-color: #0E1117 !important;
            color: #FAFAFA !important;
        }
        .dashboard-title {
            font-size: 2rem;
            font-weight: 700;
            color: white;
            background: linear-gradient(90deg, #6C63FF, #00B4DB);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 20px;
        }
        div[data-testid="stMetric"] {
            background: #1E1E1E;
            border-radius: 15px;
            padding: 20px 25px;
            box-shadow: 0 0 12px rgba(108, 99, 255, 0.25);
            border-left: 6px solid #6C63FF;
        }
        div[data-testid="stMetricValue"] {
            color: white !important;
            font-size: 28px !important;
            font-weight: bold !important;
        }
        div[data-testid="stMetricLabel"] {
            color: #E5E7EB !important;
            font-size: 14px !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---- MAIN DASHBOARD ----
st.markdown('<div class="dashboard-title">🎓 MIT Candidate Training Dashboard</div>', unsafe_allow_html=True)

# Sample data for testing
st.info("🔄 Testing with sample data - Replace URLs below with your Google Sheets URLs")

# Sample metrics
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Candidates", 25)
col2.metric("Ready for Placement", 8)
col3.metric("Open Positions", 12)
col4.metric("In Training", 15)
col5.metric("Starting MIT Program", 2)

st.markdown("---")
st.markdown("### 📍 Google Sheets URLs to Test")

st.code("""
Main Data URL:
https://docs.google.com/spreadsheets/d/e/2PACX-1vTAdbdhuieyA-axzb4aLe8c7zdAYXBLPNrIxKRder6j1ZAlj2g4U1k0YzkZbm_dEcSwBik4CJ57FROJ/pub?gid=813046237&single=true&output=csv

Jobs Data URL:
https://docs.google.com/spreadsheets/d/e/2PACX-1vTAdbdhuieyA-axzb4aLe8c7zdAYXBLPNrIxKRder6j1ZAlj2g4U1k0YzkZbm_dEcSwBik4CJ57FROJ/pub?gid=1073524035&single=true&output=csv
""")

st.markdown("### 🔧 Next Steps:")
st.markdown("""
1. **Test URLs**: Open both URLs in your browser
2. **Check Sharing**: Make sure Google Sheets are "Anyone with link can view"
3. **Get Correct URLs**: Use the exact CSV export URLs from your sheets
4. **Replace URLs**: Update the URLs in the code with your working ones
""")

# Test URL loading
st.markdown("### 🧪 URL Test")
if st.button("Test Main Data URL"):
    try:
        url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTAdbdhuieyA-axzb4aLe8c7zdAYXBLPNrIxKRder6j1ZAlj2g4U1k0YzkZbm_dEcSwBik4CJ57FROJ/pub?gid=813046237&single=true&output=csv"
        df = pd.read_csv(url, skiprows=4)
        st.success(f"✅ Successfully loaded {len(df)} rows!")
        st.write("Columns:", list(df.columns))
        st.dataframe(df.head())
    except Exception as e:
        st.error(f"❌ Error loading data: {e}")

if st.button("Test Jobs Data URL"):
    try:
        url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTAdbdhuieyA-axzb4aLe8c7zdAYXBLPNrIxKRder6j1ZAlj2g4U1k0YzkZbm_dEcSwBik4CJ57FROJ/pub?gid=1073524035&single=true&output=csv"
        df = pd.read_csv(url, skiprows=5)
        st.success(f"✅ Successfully loaded {len(df)} rows!")
        st.write("Columns:", list(df.columns))
        st.dataframe(df.head())
    except Exception as e:
        st.error(f"❌ Error loading data: {e}")
