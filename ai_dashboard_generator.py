import requests
import time
import os
import webbrowser

FILE = "ai_dashboard_live.html"

print("AI Threat Intelligence System Starting...")

# Auto open browser
webbrowser.open("file://" + os.path.abspath(FILE))


def get_action(attack):
    return {
        "DDoS": "Block IP / Enable Rate Limiting",
        "Brute Force": "Lock Account / Add CAPTCHA",
        "Credential Stuffing": "Enable MFA / Force Password Reset",
        "Bot Activity": "Block Bot / Apply Firewall Rules",
        "API Abuse": "Throttle Requests / Monitor Usage"
    }.get(attack, "Monitor Activity")


def get_prediction(attack):
    return {
        "DDoS": "System overload likely if not mitigated",
        "Brute Force": "Account compromise risk",
        "Credential Stuffing": "Multiple account breaches possible",
        "Bot Activity": "Automated exploitation may increase",
        "API Abuse": "Service degradation expected"
    }.get(attack, "No immediate risk predicted")


# 🔥 NEW: DETAILED SUGGESTIONS
def get_suggestion(attack):
    return {
        "DDoS": "Activate firewall rules and scale server resources immediately",
        "Brute Force": "Temporarily lock accounts and monitor login attempts",
        "Credential Stuffing": "Force password reset and notify affected users",
        "Bot Activity": "Deploy bot detection mechanisms and block suspicious traffic",
        "API Abuse": "Apply API throttling and monitor abnormal usage patterns"
    }.get(attack, "Continue monitoring system behavior")


while True:
    try:
        res = requests.get("http://127.0.0.1:5000/logs", timeout=2)

        try:
            data = res.json()
        except:
            data = []

        attack_types = [
            "DDoS",
            "Brute Force",
            "Credential Stuffing",
            "Bot Activity",
            "API Abuse"
        ]

        rows = ""

        for attack in attack_types:

            recent = [log for log in data[-10:] if log.get("attack_type") == attack]

            if recent:
                risk = "HIGH"
                color = "red"
                status = "ACTIVE"
            else:
                risk = "LOW"
                color = "lime"
                status = "NORMAL"

            action = get_action(attack)
            prediction = get_prediction(attack)
            suggestion = get_suggestion(attack)

            rows += f"""
            <tr>
                <td>{attack}</td>
                <td>{action}</td>
                <td>{suggestion}</td>
                <td>{prediction}</td>
                <td style='color:{color}; font-weight:bold'>{risk}</td>
                <td>{status}</td>
            </tr>
            """

        html = f"""
        <html>
        <head>
            <meta charset="UTF-8">
            <title>AI Threat Intelligence Panel</title>
            <meta http-equiv="refresh" content="3">
        </head>

        <body style="background:#050a14; color:#00ffcc; font-family:Arial; text-align:center;">

            <h1>AI Threat Intelligence Panel</h1>

            <h3 style="color:lime;">LIVE MONITORING</h3>

            <table border="1" style="margin:auto; width:95%; border-collapse:collapse;">
                <tr style="background:#111;">
                    <th>Attack Type</th>
                    <th>Immediate Action</th>
                    <th>Suggested Response</th>
                    <th>Future Prediction</th>
                    <th>Risk Level</th>
                    <th>Status</th>
                </tr>
                {rows}
            </table>

            <br>
            <p>Real-Time AI Detection | Suggestion | Prediction Engine</p>

        </body>
        </html>
        """

        with open(FILE, "w") as f:
            f.write(html)

        print("AI Dashboard Updated")

    except Exception as e:
        print("ERROR:", e)

    time.sleep(3)