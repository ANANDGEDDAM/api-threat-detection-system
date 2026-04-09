import subprocess
import threading
import time
import webbrowser
import sys
import os

def start_flask():
    try:
        subprocess.Popen([sys.executable, "api_server.py"])
    except Exception as e:
        print("Error starting Flask:", e)

def start_streamlit():
    try:
        subprocess.Popen(["streamlit", "run", "dashboard.py"])
    except Exception as e:
        print("Error starting Streamlit:", e)

def open_browser():
    # wait for servers to start
    time.sleep(5)
    webbrowser.open("http://localhost:8501")

if __name__ == "__main__":
    print("🚀 Starting full system...")

    threading.Thread(target=start_flask).start()
    threading.Thread(target=start_streamlit).start()
    threading.Thread(target=open_browser).start()

    # keep script alive
    while True:
        time.sleep(1)