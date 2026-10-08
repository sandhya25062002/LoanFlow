from django.db import models
from django.contrib.auth.models import User


class LoanApplication(models.Model):

    LOAN_TYPES = [
        ('personal', 'Personal Loan'),
        ('home', 'Home Loan'),
        ('education', 'Education Loan'),
        ('business', 'Business Loan'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('review', 'Under Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='loan_applications'
    )

    loan_type = models.CharField(
        max_length=20,
        choices=LOAN_TYPES
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    tenure = models.PositiveIntegerField()

    monthly_income = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    purpose = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.username} - {self.loan_type}"


class LoanDocument(models.Model):

    DOCUMENT_TYPES = [
        ('identity', 'Identity Proof'),
        ('income', 'Income Proof'),
        ('address', 'Address Proof'),
    ]

    application = models.ForeignKey(
        LoanApplication,
        on_delete=models.CASCADE,
        related_name='documents'
    )

    document_type = models.CharField(
        max_length=20,
        choices=DOCUMENT_TYPES
    )

    document = models.FileField(
        upload_to='loan_documents/'
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.application} - {self.document_type}"