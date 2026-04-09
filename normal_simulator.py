import requests
import time

url = "http://127.0.0.1:5000/api"

print("Generating normal traffic...")

for i in range(10):
    response = requests.get(url)
    print(f"Normal Request {i+1}: {response.status_code}")
    time.sleep(1)  # 1 second delay (normal behavior)

print("Normal traffic finished.")