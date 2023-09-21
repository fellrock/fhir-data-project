FROM python:3.9-slim

WORKDIR /app

# Copy the Python script
COPY ./converter/csv_to_ndjson.py /app/

# Copy the CSV data file from the data directory
COPY ./data/patients.csv /app/data/

CMD ["python", "/app/csv_to_ndjson.py"]
