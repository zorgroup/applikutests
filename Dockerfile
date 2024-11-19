# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Python script into the container
COPY app.py .

# Set the command to run the Python script
CMD ["python", "app.py"]
