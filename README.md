# Flask Application with MongoDB, Celery, and Bunnet ORM

## Overview
This is a Flask-based REST API that utilizes MongoDB as the database with Bunnet ORM. The application processes background jobs using Celery, validates API payloads with Cerberus, and includes unit testing with pytest-flask, pytest-factoryboy, and coverage. It also sends email notifications for any unhandled exceptions.

## Features
- Uses MongoDB as the database.
- Implements Bunnet ORM for MongoDB interactions.
- Processes background tasks using Celery.
- Validates API payloads using Cerberus.
- Supports unit testing with pytest-flask, pytest-factoryboy, and coverage.
- Sends email notifications for unhandled exceptions.

## Installation

### Prerequisites
- Python 3.7+
- Flask
- MongoDB
- Redis (for Celery)
- Docker

### Setup

1. Clone the repository:
   ```sh
   git clone git@github.com:arvindnikam/flask-mongodb-application.git
   cd flask-mongodb-application
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Configure environment variables in `.env`

5. Run the application:
   ```sh
   flask run
   ```
6. Start the Celery worker:
   ```sh
   celery -A app.celery worker --loglevel=info
   ```

## Running with Docker

### Build and Start Containers
1. Ensure Docker is installed.
2. Build and start the containers:
   ```sh
   docker build -t base_application -f Dockerfile .
   ```
3. Remove currently running container
   ```sh
   docker rm -f base_application
   ```
4. To run in detached mode:
   ```sh
   docker run -d --name base_application -p 5000:5000 -p 5050:5050 base_application
   ```

## API Endpoints

### Base Endpoint
| Method | Route | Description          |
|--------|-------|----------------------|
| GET    | `/`   | Returns health check |

### Master Data Endpoints
| Method | Route                                      | Description                 |
|--------|--------------------------------------------|-----------------------------|
| POST   | `/api/v1/master_data/locations/search`    | Searches for locations      |
| POST   | `/api/v1/master_data/locations/analyze`   | Analyzes location data      |

### Support Queries Endpoints
| Method    | Route                                  | Description                     |
|-----------|----------------------------------------|---------------------------------|
| POST      | `/api/v1/support_queries/create`      | Creates a new support query    |
| PUT/PATCH | `/api/v1/support_queries/<query_id>/update` | Updates a support query    |
| POST      | `/api/v1/support_queries/search`      | Searches for support queries   |

## Background Processing
- Celery is used for executing background tasks such as sending emails or processing large data.

## Error Handling & Notifications
- The application sends email notifications for any unhandled exceptions to ensure quick resolution.

## Testing
Run the test suite using:
```sh
pytest --cov=app
```

## Project Structure
```
flask-application/
|-- app/
|   |-- controllers/
|   |   |-- base_controller.py
|   |   |-- master_data/
|   |   |   |-- location_controller.py
|   |   |-- support_query_controller.py
|   |-- db/
|   |-- exceptions/
|   |-- helpers/
|   |-- jobs/
|   |-- lib/
|   |-- models/
|   |-- repositories/
|   |-- services/
|   |-- validators/
|   |-- __init__.py
|   |-- celery.py
|   |-- config.py
|   |-- routes.py
|-- config/
|-- log/
|-- tests/
|-- .env
|-- Dockerfile
|-- requirements.txt
|-- settings.py
|-- wsgi.py
```

## License
This project is licensed under the MIT License.
