# LoanFlow – Loan Application & Verification Management System

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
        ?
Apply for Loan
        ?
Upload Documents
        ?
Loan Officer Review
        ?
Under Review
        ?
Approve / Reject
        ?
Customer Tracks Status

## Tech Stack

- Python
- Django
- SQLite
- HTML5
- CSS3
- JavaScript

## Project Structure

Loan flow/
¦
+-- accounts/
+-- loans/
+-- loanflow/
+-- templates/
+-- static/
+-- media/
+-- manage.py
+-- requirements.txt
+-- .gitignore

## Installation

### 1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL

### 2. Open the project

cd "Loan flow"

### 3. Create and activate virtual environment

python -m venv venv

Windows:

venv\Scripts\activate

### 4. Install dependencies

pip install -r requirements.txt

### 5. Run migrations

python manage.py migrate

### 6. Start the development server

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

## Future Improvements

- PostgreSQL database
- Email notifications
- Loan EMI calculation
- Officer remarks storage
- Application history tracking
- Production deployment

## Author

Sandhya Verma

Python / Django Developer
