from django.shortcuts import render
from .forms import EnquiryForm
# Create your views here.


def home(request):
    return render(request, 'logistics/home.html')


def add_enquiry(request):
    form = EnquiryForm()
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'logistics/enquiryform.html', {'form': form})
