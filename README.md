# Project Title
## Project Year: 2024

## Team Members

- Alexandros Kartelias | 45525

## Introduction
This Docker Compose project was created for the purposes of the Cloud Computing Lab Exam 2024. It provides a set of services for numpy. This README file provides an overview of the project, including its services and how to use them.

### Services

_The Docker Compose project includes the following services:_

1. **numpy:** This service builds a flask restful server to get data from numpy. It is accessible via port 8080.
   - Resources:
     - CPU Limit: 0.10
     - Memory Limit: 500M
     - CPU Reservation: 0.05
     - Memory Reservation: 50M

2. **cli_numpy:** This service builds a cli numpy that returns sum of provided data. It is configured to run a specific command.
   - Command: plot [array of number]. For example `plot 1 2 3 4 5`
   - Resources:
     - CPU Limit: 0.10
     - Memory Limit: 500M
     - CPU Reservation: 0.05
     - Memory Reservation: 50M

3. **portainer:** This service runs Portainer for Docker management.
   - Resources:
     - CPU Limit: 0.10
     - Memory Limit: 50M
     - CPU Reservation: 0.05
     - Memory Reservation: 50M

## Getting Started

To run this project, follow these steps:

1. Clone the repository.
2. Navigate to the project directory.
3. Run `docker compose build` to build the containers.
4. Run `docker compose up -d` to start the containers.
4. Access the services via the following URLs:
   - numpy: [http://localhost:8080](http://localhost:8080)
   - portainer: [http://localhost:9000](http://localhost:9000)

Another approach would be to:
1. Clone the repository.
2. Navigate to the project directory.
3. Run `make build-project` to build the containers.
4. Run `make start-project` to start the containers.
4. Access the services via the following URLs:
   - numpy: [http://localhost:8080](http://localhost:8080)
   - portainer: [http://localhost:9000](http://localhost:9000)
5. Finished your work? Run `make stop-project` to stop the containers.