from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import LoanApplicationForm, LoanDocumentForm
from .models import LoanApplication, LoanDocument


@login_required
def apply_loan(request):

    if request.method == 'POST':

        form = LoanApplicationForm(request.POST)

        if form.is_valid():

            application = form.save(commit=False)

            application.customer = request.user

            application.save()

            return redirect(
                'applications'
            )

    else:
        form = LoanApplicationForm()

    return render(
        request,
        'apply_loan.html',
        {
            'form': form
        }
    )


@login_required
def applications(request):

    user_applications = LoanApplication.objects.filter(
        customer=request.user
    ).order_by('-created_at')

    return render(
        request,
        'applications.html',
        {
            'applications': user_applications
        }
    )


@login_required
def application_detail(request, application_id):

    application = get_object_or_404(
        LoanApplication,
        id=application_id,
        customer=request.user
    )

    documents = application.documents.all()

    identity_uploaded = documents.filter(
        document_type='identity'
    ).exists()

    income_uploaded = documents.filter(
        document_type='income'
    ).exists()

    address_uploaded = documents.filter(
        document_type='address'
    ).exists()

    return render(
        request,
        'application_detail.html',
        {
            'application': application,
            'documents': documents,
            'identity_uploaded': identity_uploaded,
            'income_uploaded': income_uploaded,
            'address_uploaded': address_uploaded,
        }
    )


@login_required
def upload_document(request, application_id):

    application = get_object_or_404(
        LoanApplication,
        id=application_id,
        customer=request.user
    )

    selected_type = request.GET.get('type', '')

    if request.method == 'POST':

        form = LoanDocumentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            document_type = form.cleaned_data['document_type']

            # Prevent duplicate document type
            if application.documents.filter(
                document_type=document_type
            ).exists():

                form.add_error(
                    'document_type',
                    'This document has already been uploaded.'
                )

            else:

                document = form.save(commit=False)

                document.application = application

                document.save()

                return redirect(
                    'application_detail',
                    application_id=application.id
                )

    else:

        form = LoanDocumentForm(
            initial={
                'document_type': selected_type
            }
        )

    return render(
        request,
        'upload_document.html',
        {
            'form': form,
            'application': application,
            'selected_type': selected_type,
        }
    )



@login_required
def officer_dashboard(request):

    # Only Loan Officers can access
    if not hasattr(request.user, 'userprofile') or request.user.userprofile.role != 'officer':
        return redirect('dashboard')

    applications = LoanApplication.objects.all().order_by('-created_at')

    total_applications = applications.count()
    pending_applications = applications.filter(status='pending').count()
    review_applications = applications.filter(status='review').count()
    approved_applications = applications.filter(status='approved').count()
    rejected_applications = applications.filter(status='rejected').count()

    return render(
        request,
        'officer_dashboard.html',
        {
            'applications': applications,
            'total_applications': total_applications,
            'pending_applications': pending_applications,
            'review_applications': review_applications,
            'approved_applications': approved_applications,
            'rejected_applications': rejected_applications,
        }
    )


@login_required
def review_application(request, application_id):

    # Only Loan Officers can access
    if not hasattr(request.user, 'userprofile') or request.user.userprofile.role != 'officer':
        return redirect('dashboard')

    application = get_object_or_404(
        LoanApplication,
        id=application_id
    )

    documents = application.documents.all()

    if request.method == 'POST':

        new_status = request.POST.get('status')

        if new_status in ['review', 'approved', 'rejected']:
            application.status = new_status
            application.save()

        return redirect(
            'review_application',
            application_id=application.id
        )

    return render(
        request,
        'review_application.html',
        {
            'application': application,
            'documents': documents,
        }
    )

@login_required
def delete_document(request, document_id):

    document = get_object_or_404(
        LoanDocument,
        id=document_id,
        application__customer=request.user
    )

    application_id = document.application.id

    if request.method == 'POST':

        # Delete uploaded file from media folder
        if document.document:
            document.document.delete(save=False)

        document.delete()

        return redirect(
            'application_detail',
            application_id=application_id
        )

    return redirect(
        'application_detail',
        application_id=application_id
    )