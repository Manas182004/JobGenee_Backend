# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY Pipfile Pipfile.lock 

# Install the dependencies and netcat
RUN apt-get update && apt-get install -y netcat-openbsd && \
    pip install --no-cache-dir pipenv && \
    pipenv install && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the entrypoint script and application code into the container
COPY entrypoint.sh /app/entrypoint.sh
COPY . /app/

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Set the entrypoint to the script
ENTRYPOINT ["/app/entrypoint.sh"]

# Run the Django development server
CMD ["pipenv","run","python", "manage.py", "runserver", "0.0.0.0:8000"]
