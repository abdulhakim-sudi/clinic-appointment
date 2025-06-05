# Clinic Appointment Project

This project is a Clinic Appointment management system built with Python and SQLite, featuring:

- Database models for clinic appointments
- Alembic migrations for database version control
- Seed data to populate the database
- CLI (Command Line Interface) for interacting with the system

## Features

- Create, view, update, and delete clinic appointments
- Database schema managed with Alembic migrations
- Easy database seeding with initial data
- Simple CLI interface for managing appointments

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/abdulhakim-sudi/clinic-appointment.git
   cd clinic-appointment
2. Create and activate a virtual environment
pipenv shell
3. Install dependencies
pipenv install
4. Run Alembic migrations to set up the database
alembic upgrade head
5. Seed the database
python lib/db/seed.py
6. Run the CLI
python lib/cli.py
Technologies Used
Python 3.x

SQLite

Alembic (for database migrations)

Pipenv (for dependency management)

Author
Abdulhakim Sudi

License
This project is licensed under the MIT License.


