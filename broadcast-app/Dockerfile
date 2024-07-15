# Use python 3.12 slim
FROM python:3.12-slim

# Install build dependencies
RUN apt-get update && \
    apt-get install -y gcc libffi-dev && \
    apt-get clean

# Install poetry
RUN pip install poetry

# Set working directory
WORKDIR /app

# Copy poetry config files
COPY pyproject.toml poetry.lock* /app/

# Disable poetry virtualenv creation
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --without dev

# Copy the broadcast code
COPY broadcast /app/broadcast/

# Expose port 80
EXPOSE 80

# Set the entry point to run the application
CMD ["python", "broadcast/broadcast.py"]
