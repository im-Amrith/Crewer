# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (if any are needed for your specific tools)
# For example, build-essential for compiling some python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose port 8501 for Streamlit
EXPOSE 8501

# Healthcheck to ensure the app is running
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Run app.py when the container launches
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
