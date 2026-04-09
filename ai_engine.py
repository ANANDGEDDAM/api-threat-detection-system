import requests
import time

API_URL = "http://127.0.0.1:5000/logs"

def analyze():
    try:
        response = requests.get(API_URL)
        data = response.json()

        if not data:
            return

        latest = data[-1]

        score = latest.get("score", 0)
        attack_type = latest.get("attack_type", "Unknown")

        # 🔥 AI RESPONSE
        if score > 0.85:
            action = "BLOCK IP"
        elif score > 0.7:
            action = "RATE LIMIT"
        else:
            action = "MONITOR"

        # 🔥 FUTURE RISK
        if score > 0.85:
            future = "HIGH RISK: Attack Escalation"
        elif score > 0.6:
            future = "MEDIUM RISK: Suspicious Pattern"
        else:
            future = "LOW RISK"

        print("\n====== AI SECURITY ENGINE ======")
        print(f"[AI] Attack Type        : {attack_type}")
        print(f"[AI] Recommended Action: {action}")
        print(f"[AI] Future Risk       : {future}")
        print("================================\n")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    print("🚀 AI Engine Started...")

    while True:
        analyze()
        time.sleep(3)