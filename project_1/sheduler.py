import time
import subprocess

UPDATE_INTERVAL = 3600  # 1 hour

while True:
    print("Checking for new knowledge...")
    subprocess.run(["python", "ingest.py"])
    time.sleep(UPDATE_INTERVAL)