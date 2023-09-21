![Logo KravelaCloud](imgs/round_logo_v00.png)
***
# FHIR Converter and Database Setup

This repository contains a solution for converting patient data from CSV to NDJSON format and then loading it into a FHIRbase database using Docker.

## Table of Contents

- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup and Usage](#setup-and-usage)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

```
fhir-data-project/
│
├── converter/                  # All files related to the converter service
│   ├── Dockerfile              # Dockerfile for the converter service
│   └── converting.py           # Python script for the converter
│
├── fhirbase/                   # All files related to the fhirbase service
│   ├── Dockerfile              # Dockerfile for the fhirbase service
│   └── init-fhirbase.sh        # Initialization script for fhirbase
│
├── data/                       # Data files
│   └── patients.csv            # CSV data file
│
├── schema/                     # Schema files
│   ├── patients.fhir.json      # FHIR schema for patients
│   └── fhir.schema.json        # General FHIR schema
│
├── imgs/                       # Images and media
│   └── logo.png                # Logo image
│
├── docker-compose.yml          # Docker Compose file
├── LICENSE                     # License file
└── README.md                   # This file
```

## Prerequisites

- Docker
- Docker Compose

## Setup and Usage

1. **Clone the Repository**:
   ```bash
   git clone [https://github.com/fellrock/fhir-data-project.git]
   cd [fhir-data-project]
   ```

2. **Build and Run the Services**:
   ```bash
   docker-compose up --build
   ```

3. **Access the FHIRbase Web Demo**:
   Once the services are up and running, you can access the FHIRbase web demo at `http://localhost:3000`.

## Contributing

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

## License

This project is licensed under the terms of the [MIT license](LICENSE).