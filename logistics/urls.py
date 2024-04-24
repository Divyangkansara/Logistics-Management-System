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
    path('signup', views.signup_page, name='signup_form'),
    path('login/', views.login_page, name='login_form'),
    path('logout/', views.log_out, name='logout'),
    path('quotation_list/', views.all_quotations, name='quotation_list'),
    path('order_list/', views.all_orders, name='order_list'),
    path('invoice/<int:enquiry_id>/<int:quotation_id>/<int:order_id>/', views.invoice, name='invoice'),
    path('temp_invoice/<int:enquiry_id>/<int:quotation_id>/<int:order_id>/', views.temp_invoice, name='temp_invoice'),
    path('pdf/<int:enquiry_id>/<int:quotation_id>/<int:order_id>/', views.print_pdf, name='print_pdf'),
    path('track_orders/', views.track_order, name='track_order'),
]