# FastAPI-and-Azure-Development--CarVach

# FastAPI CRUD Application with PostgreSQL on Azure

## Introduction

This repository contains a Python-based CRUD (Create, Read, Update, Delete) API developed using FastAPI, integrated with a PostgreSQL database, and deployed on Azure Cloud Infrastructure. The purpose of this project is to demonstrate the process of building and deploying a scalable and secure web application.

## Features

- **CRUD Operations:** Allows creation, reading, updating, and deletion of items in a PostgreSQL database.
- **Database Integration:** Uses PostgreSQL for robust data management.
- **Security:** Implements OAuth2 authentication and JWT tokens for secure API access.
- **Scalability:** Deployed on Azure with considerations for handling increased load.
- **Docker Integration:** Containerized with Docker for ease of deployment and isolation.
- **Azure Deployment:** Hosted on Azure for high availability and reliability.

## Prerequisites

- Python 3.6+
- PostgreSQL
- Docker
- Azure account
- Basic understanding of Python, FastAPI, SQL, and Docker

## Local Setup

### 1. Development Environment

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-github-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Virtual Environment:**

   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   source venv/bin/activate # macOS/Linux
   ```

3. **Install Dependencies:**

   ```bash
   pip install fastapi uvicorn sqlalchemy databases[postgresql] asyncpg
   ```

### 2. Database Setup

- Install and configure PostgreSQL locally.
- Create a new database for the API.

### 3. Running the Application

- Start the FastAPI application:

  ```bash
  uvicorn main:app --reload
  ```

- Access the API documentation at `http://127.0.0.1:8000/docs`.

## Docker Integration

1. **Build the Docker Image:**

   ```bash
   docker build -t my_fastapi_app .
   ```

2. **Run the Docker Container:**

   ```bash
   docker run -d --name myapi_container -p 80:80 my_fastapi_app
   ```


### Azure Account and Resource Setup

1. **Create an Azure Account:**
   - Sign up for an Azure account if you don't already have one.

2. **Create a Resource Group:**
   - In the Azure portal, navigate to "Resource Groups" and create a new group, providing a name and region.

### Azure Database for PostgreSQL

1. **Provision the Database:**
   - Go to "Databases" in the Azure portal and select "Azure Database for PostgreSQL".
   - Click on "Create" and fill in the necessary details like server name, admin login, and password.
   - Ensure the database is created within the previously created resource group.

2. **Configure Database:**
   - Once the database server is created, navigate to its settings.
   - Set up firewall rules to allow specific IP addresses or enable public access as per your requirement.
   - Create a new database instance that will be used by your FastAPI application.

### Azure Container Registry (ACR)

1. **Create the Registry:**
   - In the Azure portal, go to "Container registries" and create a new registry.
   - Enter details like registry name, resource group, and location.
   - Enable the admin user for the registry and note down the login server and credentials.

2. **Push Docker Image:**
   - Log in to ACR from your local machine using Docker CLI:
     ```bash
     docker login <loginServer> -u <username> -p <password>
     ```
   - Tag your local Docker image to match the ACR repository:
     ```bash
     docker tag my_fastapi_app <loginServer>/my_fastapi_app:v1
     ```
   - Push the image to ACR:
     ```bash
     docker push <loginServer>/my_fastapi_app:v1
     ```

### Azure App Service

1. **Create the App Service:**
   - In the Azure portal, go to "App Services" and click on "Create".
   - Select the same resource group, provide a unique name, and choose Docker Container as the publish option.
   - Select the appropriate region and choose a pricing tier.

2. **Configure App Service:**
   - In the "Docker" tab, select "Single Container".
   - Set the Image Source to "Azure Container Registry".
   - Choose the registry, image, and tag (version) of your Docker image.

3. **Deployment and Configuration:**
   - Deploy the application by clicking "Review and Create" and then "Create".
   - Once deployed, navigate to the "Configuration" settings of the App Service.
   - Add necessary environment variables such as `DATABASE_URL` to match your Azure PostgreSQL database credentials and any other required configuration.

### Testing and Validation

- After deployment, visit the provided URL (e.g., `[https://moulik-carvach.azurewebsites.net/docs]`) to check if the application is running and accessible.
- Perform CRUD operations via the FastAPI interactive documentation to ensure the application is interacting correctly with the Azure PostgreSQL database.

### Monitoring and Maintenance

- Utilize Azure Monitor and Application Insights to keep track of the application's performance and health.
- Regularly check logs and metrics to identify and address any issues.
