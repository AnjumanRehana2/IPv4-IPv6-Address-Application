# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy backend code
COPY backend/ backend/

# Install dependencies
RUN pip install --upgrade pip \
    && pip install -r backend/requirements.txt \
    && pip install gunicorn

# Expose the port the app runs on
EXPOSE 5050

# Start the app with Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5050", "backend.app:app"]
