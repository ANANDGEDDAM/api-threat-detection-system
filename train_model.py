import sqlite3
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

DB_NAME = "logs.db"
MODEL_FILE = "model.pkl"

print("Loading logs from database...")

conn = sqlite3.connect(DB_NAME)
df = pd.read_sql_query("SELECT * FROM api_logs", conn)
conn.close()

if df.empty:
    print("No data available for training.")
    exit()

print(f"Total logs loaded: {len(df)}")

df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values(["ip_address", "timestamp"])

df["time_diff"] = df.groupby("ip_address")["timestamp"].diff().dt.total_seconds()
df["time_diff"] = df["time_diff"].fillna(df["time_diff"].mean())

features = df.groupby("ip_address").agg({
    "ip_address": "count",
    "time_diff": "mean"
}).rename(columns={
    "ip_address": "request_count",
    "time_diff": "avg_time_between_requests"
}).reset_index()

features["burst_score"] = 1 / (features["avg_time_between_requests"] + 0.001)

X = features[[
    "request_count",
    "avg_time_between_requests",
    "burst_score"
]]

print("Training Isolation Forest model...")

model = IsolationForest(
    contamination=0.3,
    random_state=42
)

model.fit(X)

joblib.dump(model, MODEL_FILE)

print("Model trained and saved successfully as model.pkl")