# Use python 3.12
FROM python:3.12

# Set working directory
WORKDIR /app

# Copy poetry config files
COPY pyproject.toml poetry.lock* /app/

# Install poetry
RUN pip install poetry

# Disable poetry virtualenv creation since it is redundant
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-dev

# Copy the entire broadcast code
COPY broadcast/ /app/broadcast/

# Run the broadcast application
CMD ["python", "broadcast/broadcast.py"]
