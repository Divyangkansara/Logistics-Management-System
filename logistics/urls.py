from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('enquiry_list/', views.enquiries, name='enquiry_list'),
    path('enquiry/', views.submit_enquiry, name='enquiryform'),
    path('edit_enquiry/<int:id>/', views.edit_enquiry, name='edit_enquiry'),
    path('edit/<int:id>/', views.update_enquiry, name='edit'),
    path('quotation/<int:id>', views.quotation_management, name='quotation'),
    path('save_quotation/<int:id>/', views.save_quotation, name='save_quotation'),
    path('update_quotation/<int:id>/', views.update_quotation, name='update_quotation'),
]