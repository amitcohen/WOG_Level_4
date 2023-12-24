# Use the official Python image with Alpine Linux as the base image
FROM python:alpine

# Set the working directory in the container
WORKDIR /app

# Create a non-root user and group with specified UID and GID
RUN addgroup -g 1000 nonrootgroup && adduser -D -u 1000 -G nonrootgroup nonrootuser

# Set ownership of the /app directory to the non-root user
RUN chown nonrootuser:nonrootgroup /app

# Switch to the non-root user
USER nonrootuser

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Expose port 8777
EXPOSE 8777

# Command to run the application
CMD ["python", "app.py"]
