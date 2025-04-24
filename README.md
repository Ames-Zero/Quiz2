# Employee Data Generation & Visualization API

A Django REST Framework project for generating, storing, and analyzing synthetic employee data, with PostgreSQL as the backend and interactive API docs via Swagger UI.

## Features

- Generates synthetic employee, department, attendance, performance, and project data using Faker
- Stores data in a normalized PostgreSQL database
- REST API endpoints for CRUD and analytical summaries
- Filtering, pagination, and authentication support
- Interactive Swagger UI documentation
- (Optional) Docker support for easy deployment

---

## Technologies Used

- Python 3.12+
- Django 4.x+
- Django REST Framework
- PostgreSQL
- Faker (for synthetic data)
- drf-yasg (Swagger UI)
- django-filter

---

## ⚡ Quickstart

### 1. Clone the Repository
```
git clone <your-repo-url>
cd <your-repo-folder>
```


### 2. Create and Activate a Virtual Environment
```
virtualenv -p python3 <your-env-name>
source <your-env-name>/bin/activate
```


### 3. Install Dependencies
```
pip install -r requirements.txt
```


### 4. Configure Environment Variables

Create a `.env` file in the project root. It will have a structure similar to:
```
SECRET_KEY=your-secret-key
DEBUG=True
POSTGRES_DB=employee_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```


> Ensure your PostgreSQL server is running and the database/user exist.

### 5. Apply Migrations
```
python manage.py makemigrations
python manage.py migrate
```


### 6. Generate Synthetic Data
```
python employee_app/data_generator.py
```


---

## API Documentation

- **Swagger UI:** [http://127.0.0.1:8000/docs/](http://127.0.0.1:8000/docs/)
- **Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## Core API Endpoints

| Resource     | Endpoint                        | Methods                  |
|--------------|---------------------------------|--------------------------|
| Employees    | `/api/employees/`               | GET, POST                |
| Employee     | `/api/employees/{id}/`          | GET, PUT, PATCH, DELETE  |
| Departments  | `/api/departments/`             | GET, POST                |
| Attendance   | `/api/attendances/`             | GET, POST                |
| Performance  | `/api/performances/`            | GET, POST                |
| Projects     | `/api/projects/`                | GET, POST                |

- Filtering and pagination supported on list endpoints.
- Authentication required for write operations.

---
## Future Plans & Roadmap

future plans to enhance this project with the following features in future iterations:

- **Advanced Analytical Endpoints:**  
  Implement more comprehensive analytics, such as department-wise performance trends, employee tenure analysis, and attendance heatmaps.

- **Custom Data Visualizations:**  
  Integrate dashboard-style charts and graphs using Chart.js, Plotly, or D3.js, either within Swagger UI or a dedicated frontend.

- **Role-Based Access Control:**  
  Add user roles (admin, manager, employee) and permissions for more granular API security.

- **Bulk Data Import/Export:**  
  Enable uploading and exporting employee data in CSV or Excel formats.

- **Automated Testing:**  
  Expand unit and integration test coverage for all API endpoints and data generation scripts.

- **Health and Monitoring Endpoints:**  
  Add `/health/` and `/metrics/` endpoints for monitoring and observability.

- **Enhanced Logging:**  
  Implement structured logging for API usage and error tracking.

- **Continuous Integration (CI):**  
  Add CI pipelines for automated testing, linting, and deployment.

- **Cloud & Docker Deployment:**  
  Improve Docker support and provide deployment guides for cloud providers (AWS, Azure, GCP).

- **Documentation Expansion:**  
  Add a full API reference and user/developer guides, possibly as a project wiki or documentation site.

- **Internationalization (i18n):**  
  Support multiple languages for API responses and documentation.

---


For any issues, please open an issue in the repository.