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

# Disable virtualenv creation
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --without dev

# Copy the receive code
COPY receive/ /app/receive/

# Expose port 80
EXPOSE 80

# Run the receive application
CMD ["python", "receive/receive.py"]
