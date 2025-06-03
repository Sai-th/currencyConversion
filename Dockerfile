# Use lightweight python image from official python 3.11
FROM python:3.11-slim 

# Set working directory inside /app inside the container 
WORKDIR /app 

# Copy requirements.txt to /app for dependency installation
COPY requirements.txt requirements.txt 

# Install packages and remove cache after installation to save space
RUN pip install --no-cache-dir -r requirements.txt 

# Copy all files and folders to container
COPY . .

# Expose port 5050
EXPOSE 5050

# Run the Flask application when container starts
CMD ["python", "app.py"]
