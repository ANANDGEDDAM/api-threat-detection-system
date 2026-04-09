from flask import Flask, jsonify, render_template
import datetime
import random
import numpy as np
import joblib
import threading
import webbrowser
import time
from collections import defaultdict

app = Flask(__name__)

# Load ML model
try:
    model = joblib.load("threat_model.pkl")
except:
    model = None

logs = []

metrics = {
    "total_requests": 0,
    "malicious_requests": 0,
    "normal_requests": 0
}

ip_behavior = defaultdict(lambda:{
    "count":0,
    "last_time":None,
    "intervals":[],
    "endpoints":set(),
    "agents":set(),
    "geo":set()
})

ip_pool = [
"192.168.1.12","10.0.0.25","172.16.0.44",
"34.102.12.9","45.33.21.5","91.223.55.2",
"13.89.112.77","8.23.91.10"
]

geo_pool = [
"United States","Germany","India",
"Brazil","Singapore","United Kingdom",
"Japan","Canada"
]

agents = [
"Chrome Browser",
"Firefox Browser",
"Safari Mobile",
"Python Requests Bot",
"Postman Runtime",
"Automated Script",
"curl Client"
]

endpoints = [
"/api/login","/api/admin","/api/data",
"/api/user","/api/config"
]


# 🔥 FINAL — TOP 5 ATTACK TYPES ONLY (SAFE)
def classify_attack(req_count, endpoint_div, agent_div, geo_div, avg_int):

    # 🔴 DDoS → very high traffic, low endpoint diversity
    if req_count > 120 and endpoint_div <= 2:
        return "DDoS"

    # 🟠 Brute Force → repeated attempts, fast timing
    elif endpoint_div <= 2 and avg_int < 0.5:
        return "Brute Force"

    # 🟡 Credential Stuffing → moderate traffic + limited endpoints
    elif req_count > 70 and endpoint_div <= 3:
        return "Credential Stuffing"

    # 🔵 Bot Activity → very low user-agent diversity
    elif agent_div <= 1:
        return "Bot Activity"

    # 🟣 API Abuse → fallback (everything else)
    else:
        return "API Abuse"


def threat_level(score):

    if score > 0.8:
        return "CRITICAL"
    elif score > 0.6:
        return "HIGH"
    elif score > 0.4:
        return "MEDIUM"
    else:
        return "LOW"


def generate_request():

    ip = random.choice(ip_pool)
    endpoint = random.choice(endpoints)
    agent = random.choice(agents)
    geo = random.choice(geo_pool)

    now = datetime.datetime.now()

    behavior = ip_behavior[ip]

    behavior["count"] += 1
    behavior["endpoints"].add(endpoint)
    behavior["agents"].add(agent)
    behavior["geo"].add(geo)

    if behavior["last_time"]:
        interval = (now - behavior["last_time"]).total_seconds()
        behavior["intervals"].append(interval)

    behavior["last_time"] = now

    avg_interval = 0
    if behavior["intervals"]:
        avg_interval = sum(behavior["intervals"]) / len(behavior["intervals"])

    if random.random() < 0.3:

        request_count = random.randint(80,150)
        endpoint_div = random.randint(1,6)
        agent_div = random.randint(1,4)
        geo_div = random.randint(1,5)
        avg_int = random.uniform(0.05,1.0)

    else:

        request_count = behavior["count"]
        endpoint_div = len(behavior["endpoints"])
        agent_div = len(behavior["agents"])
        geo_div = len(behavior["geo"])
        avg_int = avg_interval


    features = np.array([[
        request_count,
        endpoint_div,
        agent_div,
        geo_div,
        avg_int
    ]])

    if model:
        threat_score = float(model.predict_proba(features)[0][1])
    else:
        threat_score = random.random()

    status = "NORMAL"
    if threat_score > 0.6:
        status = "MALICIOUS"

    if status == "MALICIOUS":
        attack_type = classify_attack(request_count, endpoint_div, agent_div, geo_div, avg_int)
    else:
        attack_type = "Normal"

    # ✅ ONLY FIX — DEFINE log HERE
    log = {
        "time": now.strftime("%H:%M:%S"),
        "ip": ip,
        "endpoint": endpoint,
        "geo": geo,
        "agent": agent,
        "score": round(threat_score, 2),
        "status": status,
        "attack_type": attack_type
    }

    logs.append(log)

    metrics["total_requests"] += 1

    if status == "MALICIOUS":
        metrics["malicious_requests"] += 1
    else:
        metrics["normal_requests"] += 1

def attack_simulation():

    while True:
        generate_request()
        time.sleep(1)


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/logs")
def get_logs():
    return jsonify(logs[-30:])


@app.route("/metrics")
def get_metrics():
    return jsonify(metrics)


@app.route("/behavior")
def behavior():

    result=[]

    for ip,data in ip_behavior.items():

        avg_interval=0
        if data["intervals"]:
            avg_interval=sum(data["intervals"])/len(data["intervals"])

        result.append({
            "ip":ip,
            "request_count":data["count"],
            "endpoint_diversity":len(data["endpoints"]),
            "agent_diversity":len(data["agents"]),
            "geo_diversity":len(data["geo"]),
            "avg_interval":round(avg_interval,2)
        })

    return jsonify(result)


@app.route("/graph_data")
def graph_data():

    times=[log["time"] for log in logs[-20:]]
    scores=[log["score"] for log in logs[-20:]]

    return jsonify({
        "times":times,
        "scores":scores
    })


def open_browser():

    time.sleep(1)
    webbrowser.open("http://127.0.0.1:5000")


if __name__ == "__main__":

    threading.Thread(target=open_browser).start()
    threading.Thread(target=attack_simulation).start()

    app.run(debug=True,use_reloader=False)