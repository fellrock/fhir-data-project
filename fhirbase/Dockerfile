# Use the official PostgreSQL image
FROM postgres:14

# Set environment variables
ENV DATABASE_NAME=fb
ENV FHIR_VERSION=3.0.1

# Install necessary tools and download FHIRbase
RUN apt-get update && \
    apt-get install -y wget && \
    wget https://github.com/fhirbase/fhirbase/releases/download/v0.0.6/fhirbase-linux-amd64 -O /usr/local/bin/fhirbase && \
    chmod +x /usr/local/bin/fhirbase

# Add an initialization script
COPY /fhirbase/init-fhirbase.sh /docker-entrypoint-initdb.d/

# Set the entrypoint to the PostgreSQL entrypoint script
ENTRYPOINT ["docker-entrypoint.sh"]

# Default command to run PostgreSQL
CMD ["postgres"]
