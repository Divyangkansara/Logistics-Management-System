from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('enquiry/', views.submit_enquiry, name='enquiry'),
    path('thankyou/', views.thankyou, name='thankyou')
]