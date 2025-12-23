# Temperature Sensor Simulation 

Software-only temperature monitoring pipeline: sensor simulator -> MQTT -> ROS2-like bridge -> Flask live dashboard.

## Instructions on how to run the system:

Step 1 : Install Mosquitto MQTT broker on Windows 11:

Download and install from the official Mosquitto site.

Start the Mosquitto broker so it listens on port 1883 (default).
​

Step 2 : Open a terminal in VS Code and Create and activate a virtual environment (recommended): 

python -m venv .venv
   
.\.venv\Scripts\activate


Step 3 : Install dependencies:

pip install -r requirements.txt


Step 4 : Start the broker :

python orchestrator.py


Step 5 : Open the dashboard in your browser:

Go to: http://localhost:5000/


