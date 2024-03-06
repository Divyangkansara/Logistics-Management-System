from django.shortcuts import render
from .models import Enquiries   



#  home page
def home(request):
    return render(request, 'logistics/home.html')


# pending enquiries
def enquiries(request):

    enquiry_data = Enquiries.objects.all()
    return render(request, 'logistics/enquiries.html', {'data':enquiry_data})



# submit enquiry
def submit_enquiry(request):
    if request.method == 'POST':
        scope_of_work = request.POST.get('scope_of_work')
        enquiry_date = request.POST.get('enquiry_date')
        status = request.POST.get('status')
        job_category = request.POST.get('job_category')
        customer_name = request.POST.get('customer_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact_person = request.POST.get('contact_person')
        sales_person = request.POST.get('sales_person')
        sales_team = request.POST.get('sales_team')
        freight_type = request.POST.get('freight_type')
        type = request.POST.get('type')
        enquiry_details = request.POST.get('enquiry_details')
        priority_tags = request.POST.get('priority_tags')
        
        enquiry = Enquiries(scope_of_work=scope_of_work, enquiry_date=enquiry_date, job_category=job_category, customer_name=customer_name, email=email, phone=phone, contact_person=contact_person, sales_person=sales_person, sales_team=sales_team, freight_type=freight_type, type=type, enquiry_details=enquiry_details)
        enquiry.save()

        return render(request, 'logistics/editenquiry.html', {'order': enquiry})
    
    return render(request, 'logistics/enquiryform.html')


#  edit enquiry
def edit_enquiry(request):
    return render(request, 'logistics/editenquiry.html')