import streamlit as st
import sqlite3
import pandas as pd
import time

DB_NAME = "logs.db"

st.set_page_config(layout="wide")

st.title("🔐 API Threat Detection Dashboard")


import requests

def load_data():
    try:
        response = requests.get("http://127.0.0.1:5000/logs")
        data = response.json()
        df = pd.DataFrame(data)

        # Rename columns to match your dashboard
        df.rename(columns={
            "time": "timestamp",
            "agent": "user_agent",
            "score": "threat_score"
        }, inplace=True)

        return df

    except:
        return pd.DataFrame()


placeholder = st.empty()

while True:
    df = load_data()

    with placeholder.container():
        if df.empty:
            st.warning("No data yet...")
        else:
            st.subheader("📊 Attack Timeline")

            st.dataframe(
                df[[
                    "timestamp",
                    "ip",
                    "endpoint",
                    "geo",
                    "user_agent",
                    "threat_score",
                    "status",
                    "attack_type",
                    "recommended_action",
                    "future_risk"
                ]],
                use_container_width=True
            )

            # 🔥 NEW AI INSIGHTS PANEL
            st.subheader("🧠 AI Insights")

            latest = df.iloc[0]

            st.write(f"Attack Type: {latest.get('attack_type', 'N/A')}")
            st.write(f"Recommended Action: {latest.get('recommended_action', 'N/A')}")
            st.write(f"Future Risk: {latest.get('future_risk', 'N/A')}")

    time.sleep(2)