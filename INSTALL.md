## Getting Started Setting Up The Virtual Lab
Ensure you have `docker` `docker compose` installed on your machine. 

To spin up a virtual lab, follow these steps:


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