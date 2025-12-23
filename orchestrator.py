import subprocess
import sys
import time
import os

def run_process(cmd, cwd=None):
    return subprocess.Popen(cmd, cwd=cwd)

def main():
    sensor_proc = run_process([sys.executable, "sensor_publisher.py"], cwd=os.path.join(os.getcwd(), "sensor"))
    bridge_proc = run_process([sys.executable, "mqtt_ros2_bridge.py"], cwd=os.path.join(os.getcwd(), "bridge"))
    dashboard_proc = run_process([sys.executable, "app.py"], cwd=os.path.join(os.getcwd(), "dashboard"))

    print("Processes started. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        for p in [sensor_proc, bridge_proc, dashboard_proc]:
            if p and p.poll() is None:
                p.terminate()

if __name__ == "__main__":
    main()
