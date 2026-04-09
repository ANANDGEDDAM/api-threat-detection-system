import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("logs.db")

# Read logs
df = pd.read_sql_query("SELECT * FROM api_logs", conn)

conn.close()

# Convert timestamp to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Calculate request count per IP
request_counts = df.groupby("ip_address").size().reset_index(name="request_count")

print("Feature Data:")
print(request_counts)
