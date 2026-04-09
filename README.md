# API Threat Detection System

This project is an AI-based API Threat Detection System that analyzes API traffic using behavioral analysis per IP address. The system detects malicious activities in real time and provides suggestions and future predictions for security actions.

## Key Features

- Behavioral Analysis per IP
- Real-time API traffic simulation
- Machine Learning-based threat detection
- Attack classification (DDoS, Brute Force, Credential Stuffing, Bot Activity, API Abuse)
- AI-based recommendations (what action to take)
- Future prediction (what may happen next)
- SOC-style dashboard for monitoring

## Technologies Used

- Python
- Flask
- Machine Learning (Logistic Regression)
- HTML Dashboard

## How the System Works

1. API traffic is simulated.
2. Each IP is monitored for:
   - Request frequency
   - Endpoint diversity
   - User-agent behavior
   - Time patterns
3. The model detects abnormal behavior.
4. Attacks are classified.
5. The system provides:
   - Detection
   - Suggestions
   - Predictions

## How to Run the Project

### Step 1: Start API Server
python3 api_server.py

This will start the backend system and open the main dashboard.

### Step 2: Start AI Dashboard
python3 ai_dashboard_generator.py

This will open the AI Threat Intelligence Panel showing:

- Attack Detection
- Suggested Actions
- Future Predictions

## Author

Anand P Geddam
