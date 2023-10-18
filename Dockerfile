# Use an official Python runtime as a parent image
FROM python:3.9.7-slim-buster

# Install the required system packages
RUN apt-get update && apt-get install -y python3-tk python3-dev && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory in the Docker container
WORKDIR /Users/jawhersaid/Desktop/assis_auto/htcv_ss23project_syntheticassistant

# Copy the content of the local src directory to the working directory
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container (optional)
EXPOSE 80

# Run meetings_automation.py when the container launches
CMD ["python", "./main.py"]
