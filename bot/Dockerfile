FROM python:3.9-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

COPY . /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --user -r requirements.txt

# Run app.py when the container launches
CMD ["python", "bot.py"]