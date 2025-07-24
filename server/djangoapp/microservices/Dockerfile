FROM python:3.9.18-slim-bookworm

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements file first to leverage Docker layer caching
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy the entire microservices content into the /app directory
# Based on your 'ls -l /app' output, app.py is directly in this directory.
COPY . .

# For debugging (can be removed after successful deployment)
RUN ls -l /app
RUN ls -l /app/sentiment # This will likely show an empty 'sentiment' folder or other files, but not app.py

# Command to run the application, explicitly pointing to its actual location
CMD ["python3", "app.py"]
