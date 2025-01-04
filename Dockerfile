
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application source code to the container
COPY . /app

# Install system dependencies (if required)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Flask will run on
EXPOSE 8080

# Define the command to run the Flask application
CMD ["flask", "--app", "src.app.main", "run", "--host=0.0.0.0", "--port=8080"]