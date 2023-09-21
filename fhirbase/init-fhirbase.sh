#!/bin/bash
set -e

# Wait for PostgreSQL to start
until pg_isready; do
  sleep 1
done

# Create a new database
psql -U postgres -c "CREATE DATABASE $DATABASE_NAME;"

# Initialize the database with FHIR schema using Unix domain socket
fhirbase -d $DATABASE_NAME --fhir=$FHIR_VERSION --host=/var/run/postgresql init

# Load the NDJSON file into Fhirbase
fhirbase -d $DATABASE_NAME --fhir=$FHIR_VERSION --host=/var/run/postgresql load /app/shared/patients.ndjson

# Initialize the database with FHIR schema using Unix domain socket
fhirbase -d $DATABASE_NAME --fhir=$FHIR_VERSION --host=/var/run/postgresql web