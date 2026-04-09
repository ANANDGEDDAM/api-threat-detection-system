## AI-Based Behavioral API Threat Detection System

# API Threat Detection System
...

This project is an AI-based API Threat Detection System that uses behavioral analysis per IP address to detect malicious activity in real time.

The system not only detects threats but also provides recommended actions and future predictions, similar to a Security Operations Center (SOC).

---

## Key Features

- Behavioral Analysis per IP address
- Real-time API traffic simulation
- Machine Learning-based threat detection
- Attack classification:
  - DDoS
  - Brute Force
  - Credential Stuffing
  - Bot Activity
  - API Abuse
- AI-based Suggestions (What action to take)
- Future Prediction (What may happen next)
- SOC-style monitoring dashboard

---

## How It Works

## System Flow

API Request → Feature Extraction → Behavioral Analysis per IP → ML Model → Attack Detection → Suggestion → Prediction → Dashboard

1. API traffic is simulated.
2. Each IP is monitored based on:
   - Request frequency
   - Endpoint diversity
   - User-agent diversity
   - Request timing behavior
3. Machine learning model detects abnormal patterns.
4. System classifies attack type.
5. AI module provides:
   - Detection
   - Suggestion
   - Prediction

---

## Project Structure
api-threat-detection-system/
│
├── api_server.py # Main API simulation and detection
├── detection_engine.py # Threat prediction logic
├── feature_engineering.py # Feature extraction per IP
├── ai_dashboard_generator.py # AI dashboard (suggestions + predictions)
├── model.pkl # Trained ML model
├── README.md # Project documentation


---

## How to Run

### Step 1: Start API Server
python3 api_server.py

This will:
- Start the backend
- Open the main dashboard

---

### Step 2: Start AI Dashboard

python3 ai_dashboard_generator.py

This will:
- Open second browser
- Show:
  - Attack Detection
  - Suggested Actions
  - Future Predictions

---

## Output

The system provides:

- Real-time threat detection
- Recommended actions (mitigation steps)
- Future risk prediction

---

## Why This Project is Special

- Detects attacks using behavioral analysis per IP
- Not just rule-based detection
- Provides suggestions (what to do)
- Provides predictions (what may happen next)
- Works like a mini SOC system

## Author

Anand P Geddam
