Sure, here's the Dockerfile code:

```
# Base image
FROM python:3.9-slim-buster

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy application files
COPY http_monitor.py .

# Expose port
EXPOSE 8000

# Start application
CMD ["python3", "http_monitor.py"]
```