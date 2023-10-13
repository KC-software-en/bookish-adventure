# Use the latest pypy base image for a lightweight and efficient Python runtime
FROM pypy:latest

# Create and set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .

# Install the Python dependencies listed in requirements.txt
RUN pip install -r requirements.txt

# Copy the entire project into the container
COPY . /app

# Set the default command to run the script when the container starts
CMD python task_manager.py