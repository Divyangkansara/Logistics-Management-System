from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('enquiries/', views.enquiries, name='enquiries'),
    path('enquiryform/', views.submit_enquiry, name='enquiryform'),
    path('editenquiry/', views.edit_enquiry, name='editenquiry'),
]