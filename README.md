# HTCV_SS23Project_SyntheticAssistant

## Overview
HTCV_SS23Project_SyntheticAssistant commenced with the goal of collecting interaction data to facilitate AI model training for automated email response systems. Due to time constraints, the focus was adjusted to create a software-like automation tool for email-related tasks, leveraging object detection.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
+ Docker (for the automation program)
+ Python 3.x

### Setup
1. **Install Python:**
   Ensure Python 3.x is installed on your system. Python can be downloaded from the [official Python website](https://www.python.org/downloads/).

2. **Clone Repository:**
   Clone the project repository to your local machine.

   ```bash
   git clone git@git.tu-berlin.de:cvrs/htcv_ss23project_syntheticassistant.git
   ```
3. **Install Dependencies:**
  In the project directory, install the necessary Python libraries by running this in the Terminal:
   ```bash 
   pip install -r requirements.txt
   ```
## Data Collection Deployment (Only necessary when you want to collect new data, it would also work if you skip this step)
   
1. **Run the Logger Script:**
Execute the Keyboard+Mouse_Logger.py script to start the logging process (located in the "cross_platform2" branch):
   ```bash
   python Keyboard+Mouse_Logger.py 
   ``` 
   To finish and save the recorded data, press the 'Escape' key.
   This will terminate the logging process and save the recorded keyboard and mouse activities, as well as the video.

## Automation Program Deployment with Docker
### Prerequisites
Docker must be installed on your system. You can download it from the Docker website. Use the "finalBranch" for macOS and the ""olafsBranch2" for Ubuntu.

### Steps to Run the Program in Docker

1. **Running the Screenshot Server:**
To enable the screenshot functionality, you need to run a Flask server by executing the following Python script in a separate terminal:
   ```bash
   python screenshot_server.py
   ```
   This script launches a Flask server on http://0.0.0.0:5005 to handle screenshot-related requests.


2. **Build the Docker Image:**
Open a terminal and navigate to the directory with your Dockerfile. Build the Docker image with:
   ```bash 
   docker build -t <image-name> .
   ```
   Replace <image-name> with a name of your choice for the Docker image.


3. **Run the Docker Container:**
Launch the Docker container from the built image:
   ```bash
   docker run -p <host-port>:<container-port> <image-name> 
   ```
   + Replace <host-port> with the port number on your host machine you want to use. 
   + Replace <container-port> with the port number your application uses inside the container.
   + Ensure <image-name> matches the name you used when building the image.

   This command starts the automation program inside the container and exposes it on the specified port of your local machine.


4. **Access the Program:**
Once the container is running, the automation program will operate automatically.

## Project Status
The project is in the development phase. The data collection infrastructure is ready for deployment, and the email automation program is operational within a Docker environment.

**Completion Status:** The current version of the project has been completed and is functional for its intended purposes.

**Future Work:** While the project has achieved its primary goals, there are opportunities for further enhancement. One potential avenue for future work involves leveraging the collected data for training deep learning models, enhancing the capabilities of the email automation system.

## Authors and Acknowledgment
The project is made by Jawher Said, Yassine Dhieb, and Safouane Nciri under the supervision of Professor Olaf Hellwich at Technische Universität Berlin.

## License
This project is released under the Unlicense.

