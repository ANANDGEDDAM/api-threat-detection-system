import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

print("=====================================")
print("Training Hybrid Threat Detection Model")
print("Supervised Model: Logistic Regression")
print("Feature Inspiration: Isolation Forest Behavioral Concepts")
print("=====================================")

# ------------------------------------
# Generate synthetic behavioral dataset
# ------------------------------------

np.random.seed(42)

rows = 1000

data = {
    "request_count": np.random.randint(1, 120, rows),
    "endpoint_diversity": np.random.randint(1, 10, rows),
    "agent_diversity": np.random.randint(1, 6, rows),
    "geo_diversity": np.random.randint(1, 5, rows),
    "avg_interval": np.random.uniform(0.1, 5, rows)
}

df = pd.DataFrame(data)

# ------------------------------------
# Label generation (simulate attacks)
# ------------------------------------

df["label"] = (
    (df["request_count"] > 80) |
    (df["endpoint_diversity"] > 6) |
    (df["avg_interval"] < 0.5)
).astype(int)

# ------------------------------------
# Features and labels
# ------------------------------------

X = df[[
    "request_count",
    "endpoint_diversity",
    "agent_diversity",
    "geo_diversity",
    "avg_interval"
]]

y = df["label"]

# ------------------------------------
# Train Logistic Regression model
# ------------------------------------

model = LogisticRegression(max_iter=200)

print("Training model...")

model.fit(X, y)

# ------------------------------------
# Save trained model
# ------------------------------------

joblib.dump(model, "threat_model.pkl")

print("Model training completed successfully")
print("Saved as: threat_model.pkl")

print("Training dataset size:", len(df))
print("Features used:")
print(X.columns.tolist())

print("=====================================")
print("Model ready for SOC threat detection demo")
print("=====================================")