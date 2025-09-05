FROM python:3.10-slim

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install postgres client for wait-for-db.sh
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

# Copy code
COPY . .

# Make wait-for-db.sh executable
RUN chmod +x wait-for-db.sh

# Default command (will be overridden by docker-compose entrypoint)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
