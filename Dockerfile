FROM python:3.10-slim

# Install PostgreSQL development libraries
RUN apt-get update && apt-get install -y libpq-dev
RUN apt-get update && apt-get install -y build-essential libpq-dev

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application files
COPY . /app/

# Expose the port your app will run on
EXPOSE 8000

# Set the command to run your application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
