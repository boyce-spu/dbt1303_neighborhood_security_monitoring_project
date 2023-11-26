# Welcome to dbt1303_neighborhood_security_monitoring_project

The Neighborhood Incident Tracker is a Python (Django) web application designed to empower users to monitor and report incidents within their community. Whether it's a broken streetlight, a pothole, or a safety concern, this app provides a centralized platform for users to submit and track incident reports.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Running the App](#running-the-app)
- [Project Structure](#project-structure)
- [License](#license)

## Getting Started

### Prerequisites

- [Python](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/boyce-spu/dbt1303_neighborhood_security_monitoring_project.git
   cd dbt1303_neighborhood_security_monitoring_project
   
2. Install dependencies:

``` bash
pip install -r requirements.txt
```
### Running the App
Start the development server
```bash
python manage.py runserver
```
The app will be accessible at http://localhost:8000/home.
### Project Structure
```
/config -> (onfiguration and settings)
/app -> (main app functionality)
/static -> (static files stored here; css, js etc)
/templates -> (HTML files for the app)
```


License
This project is licensed under the MIT License - see the LICENSE.md file for details.