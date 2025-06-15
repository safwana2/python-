# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy the Python script
COPY info.py .

# Run the script
CMD ["python", "info.py"]