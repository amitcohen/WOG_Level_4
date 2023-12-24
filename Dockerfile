# Use the official Python image with Alpine Linux as the base image
FROM python:alpine

# Set the working directory in the container
WORKDIR /

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
# COPY . /app

# Expose port 8777
EXPOSE 8777

# Command to run the application
CMD ["python", "app.py"]
