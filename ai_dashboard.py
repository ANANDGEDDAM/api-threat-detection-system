from flask import Flask
import requests
import threading
import webbrowser
import time

app = Flask(__name__)

def analyze():
    try:
        res = requests.get("http://127.0.0.1:5000/logs", timeout=2)
        data = res.json()

        if not data:
            return "No Data", "No Data", "No Data"

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

        return attack_type, action, future

    except Exception as e:
        print("ERROR:", e)
        return "Connecting...", "Connecting...", "Connecting..."


@app.route("/")
def dashboard():
    attack_type, action, future = analyze()

    return f"""
    <!DOCTYPE html>
    <html>
    <body style="background:black; color:lime; text-align:center; font-family:Arial;">
        <h1>AI Threat Intelligence Panel</h1>

        <p>Attack Type: {attack_type}</p>
        <p>Recommended Action: {action}</p>
        <p>Future Risk: {future}</p>
    </body>
    </html>
    """


def open_browser():
    time.sleep(3)
    webbrowser.open("http://127.0.0.1:6000")


if __name__ == "__main__":
    print("🧠 AI Dashboard running at http://127.0.0.1:6000")

    threading.Thread(target=open_browser).start()

    app.run(port=6000)