from django.contrib import admin
from .models import LoanApplication, LoanDocument

admin.site.register(LoanApplication)
admin.site.register(LoanDocument)