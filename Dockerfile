# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
# You should create a requirements.txt file with your project's dependencies
# For example:
# Django==4.2.5
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code into the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Run the application
# We use 0.0.0.0 to make it accessible from outside the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
