# The base image for the container
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

# Install Python dependencies
COPY ../requirements.txt /app/requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

# Expose ports for external access
EXPOSE 5000

# Run additional setup commands (optional)
RUN echo "Setting up environment..."

# Specify the default command to run when the container starts
CMD ["python", "nbgenerate.py"]
