# Cloud-Style ML-Based API Threat Detection System

## Project Overview

This project implements a cloud-inspired API threat detection pipeline using Machine Learning.  
The system simulates real-world API traffic, detects anomalous behavior using Isolation Forest, and provides enterprise-style monitoring and export capabilities.

The design mirrors modern cloud security architectures such as:
- Log ingestion systems (e.g., BigQuery / Cloud Logging)
- ML-based anomaly detection (e.g., Vertex AI)
- Security enforcement layers (e.g., Cloud Armor)
- Monitoring and reporting integrations (e.g., SIEM)

---

## System Architecture

The system follows a structured pipeline:

1. Traffic Simulation Layer  
   Generates normal and attack traffic across multiple IPs.

2. Log Storage Layer  
   Stores API logs in a structured SQLite database.

3. Feature Engineering Pipeline  
   Extracts behavioral features:
   - Request count
   - Average time between requests
   - Burst score

4. Machine Learning Layer  
   - Isolation Forest (unsupervised anomaly detection)
   - Model saved as `model.pkl`
   - Loaded during inference

5. Detection Engine  
   - Classifies anomalies
   - Assigns risk level (Low / Medium / High)
   - Calculates detection confidence
   - Measures response time

6. Security Layer  
   - API Key authentication
   - Rate limiting enforcement
   - Structured JSON responses

7. Monitoring & Reporting Layer  
   - Detection run history logging
   - Export detection results as JSON
   - Designed for SIEM integration

---

## Machine Learning Model Used

Isolation Forest (Unsupervised Anomaly Detection)

Reason:
- Suitable for detecting unknown attack patterns
- Works without labeled datasets
- Effective for burst traffic anomaly detection

Features used:
- request_count
- avg_time_between_requests
- burst_score

---

## API Endpoints

### 1. Simulate Traffic
POST /api/v1/simulate

Generates:
- Multi-IP normal traffic
- Burst attack traffic
- High-volume log generation

Header required:
x-api-key: SECURE123

---

### 2. Run Detection
GET /api/v1/detect

Performs:
- Feature extraction
- ML inference
- Risk classification
- Confidence scoring
- Response time measurement

Returns:
- total logs analyzed
- total IPs analyzed
- anomalies detected
- risk levels
- anomaly details

---

### 3. View Detection History
GET /api/v1/history

Shows previous detection runs for auditing and monitoring.

---

### 4. Export Results
GET /api/v1/export

Exports last detection results as structured JSON.
Designed for SIEM integration and reporting systems.

---

## Security Features

- API Key Authentication
- Rate limiting
- Structured anomaly scoring
- Risk classification
- Audit logging of detection runs

---

## How To Run The Project

1. Activate virtual environment:
   source venv/bin/activate

2. Run API server:
   python3 api_server.py

3. Simulate traffic:
   POST /api/v1/simulate

4. Train model:
   Stop API → python3 train_model.py

5. Restart API

6. Run detection:
   GET /api/v1/detect

---

## Cloud Alignment (Conceptual Mapping)

| Cloud Component | Project Equivalent |
|-----------------|--------------------|
| BigQuery        | SQLite log storage |
| Vertex AI       | Isolation Forest ML model |
| Cloud Armor     | API key + rate limiting |
| Log Sink        | Detection history storage |
| Looker Studio   | Export JSON for visualization |
| SIEM            | Exported detection report |

---

## Academic Contribution

This project demonstrates:

- Cloud-inspired architecture without paid cloud subscription
- Unsupervised ML-based anomaly detection
- Multi-layer API protection
- Enterprise-style monitoring and reporting
- Secure API design principles

---

## Author

Master’s Final Project  
Cloud-Era API Security using Machine Learning