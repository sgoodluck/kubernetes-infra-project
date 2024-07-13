# Use python 3.12
FROM python:3.12

# Set working directory
WORKDIR /app

# Copy poetry config files
COPY pyproject.toml poetry.lock* /app/

# Install poetry
RUN pip install poetry

# Disable virtualenv creation since it is redundant
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-dev

# Copy the receive code
COPY receive/ /app/receive/

# Run the receive application
CMD ["python", "receive/receive.py"]
