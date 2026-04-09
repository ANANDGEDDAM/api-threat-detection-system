import numpy as np
import pickle
import os

# SAFE MODEL LOAD
if os.path.exists("model.pkl"):
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
else:
    model = None


# EXISTING ATTACK TYPE LOGIC
def classify_attack(features):
    req_freq = features.get("request_frequency", 0)
    endpoint_div = features.get("endpoint_diversity", 0)
    ua_div = features.get("user_agent_diversity", 0)
    time_gap = features.get("avg_time_between_requests", 0)

    if req_freq > 100 and endpoint_div < 2:
        return "DDoS"
    elif endpoint_div <= 2 and time_gap < 1:
        return "Brute Force"
    elif endpoint_div > 5 and ua_div > 3:
        return "API Abuse"
    elif ua_div <= 1:
        return "Bot Activity"
    else:
        return "Unknown"


# 🔥 NEW ADDITIONS (SAFE)
def recommend_action(threat_score, attack_type):
    if threat_score < 0.5:
        return "ALLOW"
    elif threat_score < 0.75:
        return "MONITOR"
    elif attack_type == "Brute Force":
        return "RATE LIMIT"
    elif attack_type == "DDoS":
        return "BLOCK IP"
    elif attack_type == "API Abuse":
        return "THROTTLE TRAFFIC"
    elif attack_type == "Bot Activity":
        return "CAPTCHA"
    else:
        return "ALERT ADMIN"


def predict_future_risk(features):
    req_freq = features.get("request_frequency", 0)

    if req_freq > 120:
        return "HIGH RISK: Possible DDoS incoming"
    elif req_freq > 80:
        return "MEDIUM RISK: Traffic spike detected"
    else:
        return "LOW RISK"


# MAIN FUNCTION
def predict_threat(features):
    arr = np.array(list(features.values())).reshape(1, -1)

    if model:
        prediction = model.predict(arr)[0]
        probability = model.predict_proba(arr)[0][1]
    else:
        prediction = 1 if features["request_frequency"] > 80 else 0
        probability = features["request_frequency"] / 150

    if prediction == 1:
        attack_type = classify_attack(features)
    else:
        attack_type = "Normal"

    # 🔥 NEW OUTPUTS
    action = recommend_action(probability, attack_type)
    future_risk = predict_future_risk(features)

    return prediction, float(probability), attack_type, action, future_risk