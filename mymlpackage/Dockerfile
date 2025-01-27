# The base image for the container
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy project files into the container
RUN mkdir -p /mymlpackage
COPY . /mymlpackage

# Install system dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

# Install Python dependencies
COPY requirements.txt /mymlpackage
RUN pip install -r /mymlpackage/requirements.txt
#--mount=type=cache,target=/root/.cache/pip \


# Expose ports for external access
EXPOSE 5000

# Run additional setup commands (optional)
RUN echo "Setting up environment..."

# Specify the default command to run when the container starts
CMD ["python", "/mymlpackage/nbgenerate.py"]
