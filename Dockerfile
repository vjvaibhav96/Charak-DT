# Use an official Python runtime as a parent image
FROM python:3.9.6

# Set environment variables for Python to run in unbuffered mode (recommended for Docker)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the Django project into the container
COPY . /app/

# Expose port 8000 for Apache
EXPOSE 8000

# Start Apache (will also run your Django application)
CMD ["python", "app.py", "runserver", "0.0.0.0:8000"]
