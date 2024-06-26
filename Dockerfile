    # Use an official Python runtime as a parent image
    FROM python:3.10-slim

    # Set the working directory in the container
    WORKDIR /app

    # Copy the current directory contents into the container at /app
    COPY . /app/

    # Install any needed dependencies specified in requirements.txt
    RUN pip install --no-cache-dir -r requirement.txt

    # Expose port 80 to allow communication to/from server
    EXPOSE 8080

    # Run app.py when the container launches
    CMD ["python", "main.py"]