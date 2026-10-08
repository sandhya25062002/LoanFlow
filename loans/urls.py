from django.urls import path
from . import views


urlpatterns = [

    path('apply-loan/',views.apply_loan,name='apply_loan'),
    path('applications/',views.applications,name='applications'),
    path('applications/<int:application_id>/',views.application_detail,name='application_detail'),
    path('applications/<int:application_id>/upload/',views.upload_document,name='upload_document'),
    path('officer/dashboard/',views.officer_dashboard,name='officer_dashboard'),
    path('officer/application/<int:application_id>/',views.review_application,name='review_application'),
    path('documents/<int:document_id>/delete/',views.delete_document,name='delete_document'),

]