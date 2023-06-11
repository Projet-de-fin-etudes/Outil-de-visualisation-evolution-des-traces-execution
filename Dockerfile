# Use the base image with Ubuntu latest
FROM ubuntu:latest

# Set the working directory
WORKDIR /app

# Copy the code into the container
COPY . /app

# Install dependencies
RUN apt-get update && apt-get install -y python3.10 python3.10-venv

# Create and activate virtual environment
RUN python3.10 -m venv venv
RUN /bin/bash -c "source venv/bin/activate"

# Install pip
RUN apt-get install -y python3-pip

# Upgrade pip
RUN pip3 install --upgrade pip

# Install requirements
RUN pip install -r requirements.txt

# Set the working directory for running tests
WORKDIR /app/src

# Update the WORKDIR directive above if necessary

# Define the default command to run when the container starts
CMD ["/app/venv/bin/python", "main.py"]
