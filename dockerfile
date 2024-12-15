# Step 1: Use an official Python runtime as a parent image
FROM python:3.10-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the current directory contents into the container at /app
COPY . /app

# Step 4: Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose the port the app will run on
EXPOSE 5000

# Step 6: Define environment variables if needed (optional)
# ENV FLASK_ENV=development

# Step 7: Run the application when the container starts
CMD ["python", "app.py"]