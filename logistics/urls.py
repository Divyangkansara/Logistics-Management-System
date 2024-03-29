from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('enquiry_list/', views.enquiries, name='enquiry_list'),
    path('enquiry/', views.submit_enquiry, name='enquiryform'),
    path('edit_enquiry/<int:id>/', views.edit_enquiry, name='edit_enquiry'),
    path('edit/<int:id>/', views.update_enquiry, name='edit'),
    path('quotation/<int:id>', views.quotation_management, name='quotation'),
    path('save_quotation/<int:id>/', views.save_quotation, name='save_quotation'),
    path('update_quotation/<int:enquiry_id>/<int:quotation_id>/', views.update_quotation, name='update_quotation'),
    path('send_email/<int:enquiry_id>/<int:quotation_id>/', views.sending_email, name='send_email'),
    path('pending_order/<int:enquiry_id>/<int:quotation_id>/', views.pending_order, name='pending_order'),
    path('update_order/<int:order_id>/<int:enquiry_id>/<int:quotation_id>/', views.update_order, name='update_order'),
    path('login/', views.login_form, name='login_form'),
]