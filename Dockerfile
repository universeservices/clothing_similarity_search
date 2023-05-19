# Use the official Python base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project code to the container
COPY . .

# Set the entry point for the function
CMD ["python", "deployment/cloud_run.py"]
