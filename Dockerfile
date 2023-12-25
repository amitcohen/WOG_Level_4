# Use the official Python image with Alpine Linux as the base image
FROM python:alpine

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy the requirements.txt file into the container at /app
# COPY requirements.txt /app/

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8777 available to the world outside this container
EXPOSE 8777

# Define environment variable
ENV AWS_PUBLIC_IP 3.81.115.199

# Run app.py when the container launches
# CMD ["python", "webapp.py"]

# Command to run the application
# CMD flask run --host 0.0.0.0 --port 8000
# CMD ["python", "app.py"]
CMD ["sh", "-c", "flask run --host 0.0.0.0 --port 8777 & python app.py"]
