# LoanFlow - Loan Application & Verification Management System

LoanFlow is a Django-based loan application and verification management system designed for customers, loan officers, and administrators.

## Features

### Customer
- User registration and login
- Apply for different types of loans
- View submitted loan applications
- Track application status
- Upload required documents
- Preview and download uploaded documents
- Delete uploaded documents
- Duplicate document prevention
- File type and file size validation

### Loan Officer
- Officer authentication
- View all loan applications
- Review customer and loan details
- View uploaded documents
- Mark applications as Under Review
- Approve or Reject applications

### Admin
- Manage users and user profiles
- Manage loan applications
- Manage uploaded loan documents

## Loan Workflow

Customer Registration/Login
        |
        v
Apply for Loan
        |
        v
Upload Documents
        |
        v
Loan Officer Review
        |
        v
Under Review
        |
        v
Approve / Reject
        |
        v
Customer Tracks Status

## Tech Stack

- Python
- Django
- HTML5
- CSS3
- JavaScript
- SQLite for local development
- PostgreSQL for production deployment
- WhiteNoise for static files
- Gunicorn for production server

## Project Structure

LoanFlow/
|
+-- accounts/
+-- loans/
+-- loanflow/
+-- templates/
+-- static/
+-- manage.py
+-- requirements.txt
+-- build.sh
+-- render.yaml
+-- .gitignore
+-- README.md

## Installation

### 1. Clone the repository

git clone https://github.com/sandhya25062002/LoanFlow.git

### 2. Open the project

cd "Loan flow"

### 3. Create a virtual environment

python -m venv venv

### 4. Activate the virtual environment on Windows

venv\Scripts\activate

### 5. Install dependencies

pip install -r requirements.txt

### 6. Run migrations

python manage.py migrate

### 7. Start the development server

python manage.py runserver

Open:

http://127.0.0.1:8000/

## Security

- Login-protected views
- Role-based officer access
- Customer-specific application access
- Customer-specific document access
- CSRF protection
- File type validation
- File size validation
- Duplicate document prevention
- Secret key stored using environment variables in deployment

## Deployment

The project is configured for deployment on Render using:

- Render Web Service
- Render PostgreSQL
- Gunicorn
- WhiteNoise
- Environment variables
- Automated database migrations
- Static file collection

## Future Improvements

- Email notifications
- Loan EMI calculation
- Officer remarks storage
- Application history tracking
- Payment integration
- Production monitoring
- Cloud file storage for uploaded documents

## Author

Sandhya Verma

Python / Django Developer
