import streamlit as st
import pandas as pd
import glob
import os

# Page Config
st.set_page_config(page_title="Information Systems Dashboard", layout="wide")

st.title("📊 Data Extraction & Analysis Dashboard")
st.markdown("### Technical Consultant: [Your Name]")

# 1. Sidebar - File Selection
st.sidebar.header("Data Management")
data_files = glob.glob("data/*.csv")

if not data_files:
    st.warning("No data files found in /data. Please run main.py first.")
else:
    selected_file = st.sidebar.selectbox("Select a Dataset to Visualize", data_files)
    
    # Load Data
    df = pd.read_csv(selected_file)

    # 2. Key Metrics (KPIs)
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Records", len(df))
    col2.metric("Data Source", "Hacker News")
    col3.metric("Status", "Validated")

    # 3. Data Table View
    st.subheader("📋 Raw Extracted Data")
    st.dataframe(df, use_container_width=True)

    # 4. Simple Analysis (Example: Title Length Distribution)
    st.subheader("📈 Information Analytics")
    df['title_length'] = df['title'].apply(len)
    
    chart_data = df[['title', 'title_length']]
    st.bar_chart(chart_data.set_index('title'))

    # 5. System Logs Integration
    if st.sidebar.checkbox("Show System Audit Logs"):
        st.subheader("📂 Recent System Logs")
        log_files = glob.glob("logs/*.log")
        if log_files:
            latest_log = max(log_files, key=os.path.getctime)
            with open(latest_log, "r") as f:
                st.text(f.read())