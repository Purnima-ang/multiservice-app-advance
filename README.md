# My Multi-Service Application

This project is a simple multi-service application demonstrating Docker containerization and a CI/CD pipeline. It consists of a web service that interacts with a Redis database.

## Services

*   **Web Service:** A simple web application (e.g., Flask) that provides endpoints to set and get key-value pairs.
*   **Redis Service:** A Redis instance used as a database to store the key-value pairs.

## Prerequisites

*   Docker 20.10 or later
*   Docker Compose 1.27 or later
*   A Docker Hub account (or other Docker registry) for pushing images
*   A GitHub account (or other CI/CD platform) for the CI/CD pipeline

## Setup and Running Locally

1.  **Clone the repository:**
    ```bash
    git clone <your-github-repo-link>
    cd my-multi-service-app
    ```

2.  **Build and run the application using Docker Compose:**
    ```bash
    docker-compose up --build -d
    ```
    *   `--build`: Builds the web service image before starting the containers.
    *   `-d`: Runs the containers in detached mode (in the background).

3.  **Access the web service:**
    The web service should be accessible at `http://localhost:8000`.

    *   **Set a value:**
        ```bash
        curl -X POST http://localhost:5000/set/mykey/myvalue
        ```
    *   **Get a value:**
        ```bash
        curl http://localhost:5000/get/mykey
        ```

4.  **Stop the application:**
    ```bash
    docker-compose down
    ```
    This will stop and remove the containers, but the `redis_data` volume will persist.

5.  **Clean up (optional):**
    To remove the named volume and all images:
    ```bash
    docker-compose down -v --rmi all
    ```

## CI/CD Pipeline (GitHub Actions)

This project includes a CI/CD pipeline configured with GitHub Actions. The pipeline is triggered on pushes and pull requests to the `main` branch.

The pipeline performs the following steps:

1.  **Checkout code:** Clones the repository.
2.  **Set up Docker Buildx:** Configures Buildx for efficient image building.
3.  **Log in to Docker Hub:** Authenticates with Docker Hub using secrets.
4.  **Build and push web service image:** Builds the Docker image for the web service and pushes it to Docker Hub with `latest` and commit SHA tags.
5.  **Run tests:** Starts the necessary services using Docker Compose and runs your application tests.
6.  **Deploy (Placeholder):** This step is a placeholder for your actual deployment logic.

**To set up the CI/CD pipeline:**

1.  **Create a GitHub repository** and push your code.
2.  **Go to your repository settings** on GitHub.
3.  **Navigate to "Secrets" -> "Actions".**
4.  **Add two new repository secrets:**
    *   `DOCKERHUB_USERNAME`: Your Docker Hub username.
    *   `DOCKERHUB_TOKEN`: Your Docker Hub access token (generate one in your Docker Hub account settings).

Once the secrets are added, the CI/CD pipeline will automatically run on pushes and pull requests to the `main` branch. You can view the pipeline status and logs in the "Actions" tab of your GitHub repository.

## Security Considerations

*   **Dockerfiles:**
    *   Using smaller base images (`-slim`, `-alpine`).
    *   Using multi-stage builds to reduce the attack surface.
    *   Copying only necessary files.
    *   (For production) Consider running the application as a non-root user.
*   **Docker Compose:**
    *   Avoid exposing unnecessary ports.
    *   Use secrets for sensitive information (like database passwords) instead of environment variables in production.

## Bonus: Logging and Monitoring

(Describe your chosen logging and monitoring solution here, how it's integrated, and how to access the dashboards.)

## Screenshots of CI/CD Pipeline

(Include screenshots of your GitHub Actions workflow runs showing successful build, test, and deployment steps.)
