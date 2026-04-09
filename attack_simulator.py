import requests

url = "http://127.0.0.1:5000/api"

print("Starting attack simulation...")

for i in range(500):
    try:
        response = requests.get(url)
        print(f"Request {i+1}: {response.status_code}")
    except Exception as e:
        print("Error:", e)

print("Attack simulation finished.")