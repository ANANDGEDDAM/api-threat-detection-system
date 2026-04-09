\import subprocess
import time
import requests

print("🚀 Starting API Server...")

# Start Flask
server = subprocess.Popen(["python3", "api_server.py"])

time.sleep(5)

print("🧠 AI Engine Running...")

while True:
    try:
        response = requests.get("http://127.0.0.1:5000/logs")
        data = response.json()

        if data:
            latest = data[-1]

            score = latest.get("score", 0)
            attack_type = latest.get("attack_type", "Unknown")

            if score > 0.85:
                action = "BLOCK IP"
                future = "HIGH RISK"
            elif score > 0.7:
                action = "RATE LIMIT"
                future = "MEDIUM RISK"
            else:
                action = "MONITOR"
                future = "LOW RISK"

            print("\n====== AI SECURITY ENGINE ======")
            print(f"[AI] Attack Type        : {attack_type}")
            print(f"[AI] Recommended Action: {action}")
            print(f"[AI] Future Risk       : {future}")
            print("================================\n")

    except Exception as e:
        print("Error:", e)

    time.sleep(3)