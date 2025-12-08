FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Set Python path
ENV PYTHONPATH=/app

# Run demo
CMD ["python", "orchestrator/run_demo.py"]
