# Use base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port (change if needed)
EXPOSE 5000

# Run app (adjust if your entrypoint is different)
CMD ["python", "app.py"]