# Use official Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all necessary files
COPY . .

# Install required dependencies
RUN pip install -r requirements.txt

# Expose necessary ports
EXPOSE 5000 6000

# Run both services simultaneously
CMD ["sh", "-c", "python ml-model.py & python personal-api.py"]
