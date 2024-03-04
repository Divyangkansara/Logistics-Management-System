from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('enquiry/', views.add_enquiry, name='enquiry'),
    path('', views.home),
]