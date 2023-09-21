![Logo KravelaCloud](imgs/tinny_round_logo_v00.png)
***
# FHIR Converter and Database Setup

This repository contains a solution that use Python to converting patient data from CSV (latin-1) to NDJSON (UTF-8) format and then loading it into a FHIRbase database using Docker. I used a Linux environment over PoP!OS to implement it. This project was part of a [Munai Health technical test](https://github.com/robo-laura/dataops-teste) to the DataOps Back-End Developer job placement.

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
│   └── "logo files".png        # Logo images
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

3. **Access the FHIRbase Web**:
   Once the services are up and running, you can access the FHIRbase web demo at `http://localhost:3000`.

## 🚀 Future Upgrades

1. **Docker Secrets**: Implement Docker secrets to securely manage sensitive information like database passwords, API keys, and other credentials. This ensures that such data isn't exposed in configuration files or Docker Compose files.

2. **Environment Variables**: Use environment variables for configuration settings that are likely to change between deployment environments, such as database connection details or external service URLs.

3. **Database Encryption**: Implement encryption at rest for the PostgreSQL database to enhance data security. This ensures that even if data is accessed directly from storage, it remains encrypted and unreadable without the appropriate decryption key.

4. **Logging and Monitoring Enhancements**: Implement advanced logging and monitoring solutions like ELK Stack or Grafana to provide real-time dashboards and deeper insights into the system's operations.

5. **Automated Testing**: Introduce automated testing frameworks to ensure code quality, functionality, and to catch potential issues early in the development cycle.

6. **Continuous Integration/Continuous Deployment (CI/CD)**: Implement a CI/CD pipeline to automate the testing and deployment process, ensuring that any changes to the codebase are automatically tested and deployed to production.

7. **Rate Limiting**: Implement rate limiting to prevent any single user or service from overloading the system. This can be crucial for maintaining system performance and availability.

8. **Backup and Recovery**: While PostgreSQL offers backup solutions, automating the backup process ensures that data is regularly backed up without manual intervention. This can be crucial for disaster recovery and ensuring data integrity.

9. **Database Replication**: Implementing replication for the PostgreSQL database can enhance availability and fault tolerance.

10. **API Gateway Integration**: Integrate an API Gateway to manage, monitor, and secure microservices, providing features like request routing, API composition, and rate limiting.

11. **Service Mesh Implementation**: Consider integrating a service mesh like Istio or Linkerd for reliable and secure communication in microservices architectures.

12. **Enhanced Security Protocols**: Implement advanced security measures like end-to-end encryption, intrusion detection systems, and regular security audits.

13. **Documentation and User Guides**: Keep documentation updated and create comprehensive user guides and tutorials to assist both end-users and developers.

14. **User Feedback and Iteration**: Regularly gather feedback from end-users and stakeholders to guide future upgrades.

# Enhancing Performance with NiFi and Kafka Integration

In my journey to optimize the performance of the FHIRbase-based healthcare data application, I extensively researched various data ingestion and processing solutions. While I initially considered integrating Apache NiFi and Apache Kafka into the architecture, due to time constraints and the project's scope, I opted for a simpler approach to ensure functionality. However, having invested considerable time in planning this more intricate path, I believe it's valuable to share the insights I've gathered. In this section, I'll discuss the potential benefits of this approach and why it might be a more effective solution given ample time and resources.

## Why NiFi and Kafka?

### Scalability
While FHIRbase is adept at managing FHIR data within a PostgreSQL database, efficient data ingestion becomes paramount when grappling with vast volumes of healthcare data. NiFi offers a scalable and dependable mechanism to gather, transform, and route data from a myriad of sources to Kafka topics. Kafka facilitates distributed data streaming, making it apt for high-throughput scenarios.

### Data Transformation
NiFi shines in data transformation tasks. It empowers us to morph data from diverse formats (e.g., CSV, JSON) into FHIR resources with the requisite structure. This transformation ensures that the data fed into FHIRbase is in harmony with the FHIR standard.

### Real-time Processing
Kafka's integration paves the way for real-time data processing and analytics. Healthcare applications frequently demand prompt insights and interventions based on fresh data, such as patient updates or pivotal events. Kafka's publish-subscribe paradigm allows us to digest data as it streams in, enhancing our application's reactivity.

### Fault Tolerance and Reliability
Both NiFi and Kafka come equipped with features bolstering fault tolerance and data recovery. In the realm of healthcare, data integrity and reliability are of the essence. These tools fortify our system against data loss, even amidst system hiccups.

## Ideal Implementation

Outlined below is the envisaged implementation:

1. **Data Ingestion with NiFi**:
   - Utilize NiFi to harvest data from diverse sources, spanning CSV files, external APIs, to IoT devices.
   - Undertake data transformation within NiFi to transmute incoming data into FHIR resources.
   - Channel the transformed data to Kafka topics awaiting further refinement.

2. **Real-time Processing with Kafka**:
   - Establish Kafka topics to assimilate data from NiFi.
   - Craft Kafka consumers to process the incoming FHIR data.
   - Conduct requisite data enrichment, validation, or aggregation.
   - Commit the data into the FHIRbase database, either as new entries or updates.

3. **Scalability and Monitoring**:
   - Dynamically scale NiFi and Kafka clusters to accommodate burgeoning data inflows.
   - Integrate monitoring and alerting mechanisms to oversee the vitality and efficacy of the data pipeline.
   - Relentlessly fine-tune data processing and ingestion for peak efficiency.

4. **Data Analytics and Reporting**:
   - Harness Kafka's real-time prowess to facilitate data analytics and reporting.
   - Construct dashboards or reporting tools to furnish insights to healthcare practitioners and overseers.

5. **Security and Compliance**:
   - Roll out security protocols, encompassing data encryption, access governance, and adherence to healthcare data norms (e.g., HIPAA).

By championing this architecture, our aspiration is to amplify the performance, scalability, and real-time proficiencies of our healthcare data application, all while safeguarding data integrity and dependability.

We invite you to peruse our codebase and documentation to gain deeper insights into our implementation and to discern how you might adapt similar methodologies for your healthcare data endeavors.

# Contributing

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

# License

This project is licensed under the terms of the [MIT license](LICENSE).