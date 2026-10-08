from django import forms
from .models import LoanApplication, LoanDocument


class LoanApplicationForm(forms.ModelForm):

    class Meta:
        model = LoanApplication

        fields = [
            'loan_type',
            'amount',
            'tenure',
            'monthly_income',
            'purpose',
        ]

        widgets = {
            'loan_type': forms.Select(attrs={
                'class': 'form-control'
            }),

            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter loan amount',
                'min': '1000'
            }),

            'tenure': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter tenure in months',
                'min': '1'
            }),

            'monthly_income': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter monthly income',
                'min': '0'
            }),

            'purpose': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Explain the purpose of the loan',
                'rows': 4
            }),
        }


class LoanDocumentForm(forms.ModelForm):

    class Meta:
        model = LoanDocument

        fields = [
            'document_type',
            'document',
        ]

        widgets = {
            'document_type': forms.Select(attrs={
                'class': 'form-control'
            }),

            'document': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.jpg,.jpeg,.png'
            }),
        }

    def clean_document(self):
        document = self.cleaned_data.get('document')

        if document:

            # Maximum file size = 5 MB
            if document.size > 5 * 1024 * 1024:
                raise forms.ValidationError(
                    'File size must be less than 5 MB.'
                )

            # Allowed file types
            allowed_types = [
                'application/pdf',
                'image/jpeg',
                'image/png',
            ]

            if document.content_type not in allowed_types:
                raise forms.ValidationError(
                    'Only PDF, JPG, JPEG and PNG files are allowed.'
                )

        return document