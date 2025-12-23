# Temperature Sensor Simulation 

Software only temperature monitoring pipeline: sensor simulator -> MQTT -> ROS2-like bridge -> Flask live dashboard.

## Instructions on how to run the system & dependencies required:

###   Step 1 : Install Mosquitto MQTT broker on Windows 11:

Download and install from the official Mosquitto site.

Start the Mosquitto broker so it listens on port 1883 (default).
​

###   Step 2 : Open a terminal in VS Code and Create and activate a virtual environment (recommended): 

python -m venv .venv
   
.\.venv\Scripts\activate


###   Step 3 : Install dependencies:

pip install -r requirement.txt


###   Step 4 : Start the broker :

python orchestrator.py


###   Step 5 : Open the dashboard in your browser:

Go to: http://localhost:5000/

#   Proxie Intern Assignment: Temperature Sensor Simulation + MQTT + ROS2 + Flask Dashboard  

Overview 

Your task is to design and implement a software-only temperature monitoring system 
using: 

● MQTT (Mosquitto or similar broker) 

● ROS2 (Humble/Foxy recommended) 

● Python 

● Flask (for a web-based dashboard) 

No physical sensors, microcontrollers, or hardware of any kind should be used. All sensor 
data must be simulated in software. 

This assignment evaluates your ability to work with robotics middleware, IoT messaging 
and real-time data visualization. 


<img width="669" height="660" alt="Screenshot (88)" src="https://github.com/user-attachments/assets/87366cda-3365-404f-bbf5-3d907e45b6f0" />
