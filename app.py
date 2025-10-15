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

# ---- DATA LOADING FUNCTIONS ----
@st.cache_data(ttl=300)
def load_active_roster():
    """Load MIT tracking data from Google Sheets"""
    # CORRECTED URL - Changed from pubhtml to pub with output=csv
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTAdbdhuieyA-axzb4aLe8c7zdAYXBLPNrIxKRder6j1ZAlj2g4U1k0YzkZbm_dEcSwBik4CJ57FROJ/pub?gid=813046237&single=true&output=csv"
    
    try:
        st.markdown('<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; margin: 10px 0; border-left: 4px solid #6C63FF;">🔄 Loading MIT candidate data from Google Sheets...</div>', unsafe_allow_html=True)
        
        # Try different skiprows to find the right structure
        for skiprows in [0, 1, 2, 3, 4, 5]:
            try:
                df = pd.read_csv(url, skiprows=skiprows)
                if not df.empty and len(df.columns) > 3:
                    st.markdown(f'<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; margin: 10px 0; border-left: 4px solid #4CAF50;">✅ Successfully loaded MIT candidate data! (skiprows={skiprows})</div>', unsafe_allow_html=True)
                    break
            except:
                continue
        else:
            st.error("Could not load data with any skiprows configuration")
            return pd.DataFrame()
        
        # Show available columns for debugging
        st.markdown(f'<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; margin: 10px 0; border-left: 4px solid #00B4DB;">📋 Available columns: {list(df.columns)}</div>', unsafe_allow_html=True)
        
        return df
        
    except Exception as e:
        st.error(f"Error loading MIT candidate data: {e}")
        return pd.DataFrame()

@st.cache_data(ttl=300)
def load_placement_options():
    """Load job positions from Google Sheets"""
    # CORRECTED URL - Changed from pubhtml to pub with output=csv
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTAdbdhuieyA-axzb4aLe8c7zdAYXBLPNrIxKRder6j1ZAlj2g4U1k0YzkZbm_dEcSwBik4CJ57FROJ/pub?gid=1073524035&single=true&output=csv"
    
    try:
        st.markdown('<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; margin: 10px 0; border-left: 4px solid #6C63FF;">🔄 Loading job positions from Google Sheets...</div>', unsafe_allow_html=True)
        
        # Try different skiprows to find the right structure
        for skiprows in [0, 1, 2, 3, 4, 5, 6]:
            try:
                df = pd.read_csv(url, skiprows=skiprows)
                if not df.empty and len(df.columns) > 3:
                    st.markdown(f'<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; margin: 10px 0; border-left: 4px solid #4CAF50;">✅ Successfully loaded job positions! (skiprows={skiprows})</div>', unsafe_allow_html=True)
                    break
            except:
                continue
        else:
            st.error("Could not load job data with any skiprows configuration")
            return pd.DataFrame()
        
        # Show available columns for debugging
        st.markdown(f'<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; margin: 10px 0; border-left: 4px solid #00B4DB;">📋 Available columns: {list(df.columns)}</div>', unsafe_allow_html=True)
        
        return df
        
    except Exception as e:
        st.error(f"Error loading job positions: {e}")
        return pd.DataFrame()

# ---- MAIN DASHBOARD ----
st.markdown('<div class="dashboard-title">🎓 MIT Candidate Training Dashboard</div>', unsafe_allow_html=True)

# Load data
main_df = load_active_roster()
jobs_df = load_placement_options()

# Display metrics
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Candidates", len(main_df) if not main_df.empty else 0)
col2.metric("Ready for Placement", "TBD")
col3.metric("Open Positions", len(jobs_df) if not jobs_df.empty else 0)
col4.metric("In Training", "TBD")
col5.metric("Starting MIT Program", "TBD")

# Show raw data for debugging
if not main_df.empty:
    st.markdown("---")
    st.markdown("### 📊 Main Data Preview")
    st.dataframe(main_df.head())

if not jobs_df.empty:
    st.markdown("---")
    st.markdown("### 📊 Jobs Data Preview")
    st.dataframe(jobs_df.head())

st.markdown("---")
st.caption("🔄 LIVE DATA: Loading from Google Sheets | Auto-refreshes every 5 minutes")
