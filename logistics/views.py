from django.shortcuts import render , redirect, get_object_or_404
from .models import Enquiries , FreightType, JobCategory, Type, Quotations, PaymentType, ClientCurrency



#  home page
def home(request):
    return render(request, 'logistics/home.html')


# pending enquiries
def enquiries(request):

    enquiry_data = Enquiries.objects.all()
    return render(request, 'logistics/enquirylist.html', {'data':enquiry_data})



# Add enquiry
def submit_enquiry(request):
    if request.method == 'POST':
        scope_of_work = request.POST.get('scope_of_work')
        enquiry_date = request.POST.get('enquiry_date')
        # status = request.POST.get('status')
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
        # priority_tags = request.POST.get('priority_tags')
        
        enquiry = Enquiries(scope_of_work=scope_of_work, enquiry_date=enquiry_date, job_category=job_category, customer_name=customer_name, email=email, phone=phone, contact_person=contact_person, sales_person=sales_person, sales_team=sales_team, freight_type=freight_type, type=type, enquiry_details=enquiry_details)
        enquiry.save()

        return render(request, 'logistics/editenquiry.html', {'order': enquiry})
    
    return render(request, 'logistics/enquiryform.html')


#  edit enquiry
def edit_enquiry(request, id): 
    instance = get_object_or_404(Enquiries, pk=id)   
    return render(request, 'logistics/editenquiry.html', {'order':instance})

#  update form
def update_enquiry(request, id):

    instance = get_object_or_404(Enquiries, pk=id)
   

    if request.method == 'POST':
        instance.scope_of_work = request.POST.get('scope_of_work')
        instance.enquiry_date = request.POST.get('enquiry_date')
        instance.job_category = request.POST.get('job_category')
        instance.customer_name = request.POST.get('customer_name')
        instance.email = request.POST.get('email')
        instance.phone = request.POST.get('phone')
        instance.contact_person = request.POST.get('contact_person')
        instance.sales_person = request.POST.get('sales_person')
        instance.sales_team = request.POST.get('sales_team')
        instance.freight_type = request.POST.get('freight_type')
        instance.type = request.POST.get('type')
        instance.enquiry_details = request.POST.get('enquiry_details')

        instance.save()

        return render(request, 'logistics/editenquiry.html', {'order': instance})
    
    freight_types = FreightType.objects.all()
    jobs = JobCategory.objects.all()
    types = Type.objects.all()
    context = {'instance': instance, 'freight_types':freight_types, 'jobs':jobs,
                        'types':types}
    
    return render(request, 'logistics/updateform.html', context)    



# Add Quotation
def quotation_management(request, id):

    instance = get_object_or_404(Enquiries, pk=id)
    freight_types = FreightType.objects.all()
    jobs = JobCategory.objects.all()
    types = Type.objects.all()

    context = {'instance': instance, 'freight_types':freight_types, 'jobs':jobs,
                        'types':types}

    return render(request, 'logistics/quotation.html', context)




#  save quotation
def save_quotation(request, id):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        job_category = request.POST.get('job_category_value')
        freight_type = request.POST.get('freight_type_value')
        type = request.POST.get('type_value')
        sales_person = request.POST.get('sales_person')
        payment_type = request.POST.get('payment_type')
        quotation_date = request.POST.get('quotation_date')
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        final_destination = request.POST.get('final_destination')
        product = request.POST.get('product')
        description = request.POST.get('description')
        unit = request.POST.get('unit')
        quantity = request.POST.get('quantity')
        weight = request.POST.get('weight')
        dimension = request.POST.get('dimension')
        client_currency = request.POST.get('client_currency')
        rate = request.POST.get('rate')
        terms = request.POST.get('terms')

        quotation = Quotations(customer_name=customer_name, freight_type=freight_type, type=type, job_category=job_category, sales_person=sales_person, quantity=quantity, dimension=dimension, payment_type=payment_type, quotation_date=quotation_date, origin=origin, destination=destination, final_destination=final_destination, product=product, description=description, unit=unit, weight=weight, client_currency=client_currency, rate=rate, terms=terms)
        quotation.save()

        return render(request, 'logistics/approvequotation.html', {'quotation':quotation})
    
    return render(request, 'logistics/quotation.html')


#  update quotation
def update_quotation(request, id):

    instance = get_object_or_404(Quotations, pk=id)

    if request.method == 'POST':
        instance.customer_name = request.POST.get('customer_name')
        instance.job_category = request.POST.get('job_category_value')
        instance.freight_type = request.POST.get('freight_type_value')
        instance.type = request.POST.get('type_value')
        instance.sales_person = request.POST.get('sales_person')
        instance.payment_type = request.POST.get('payment_type')
        instance.quotation_date = request.POST.get('quotation_date')
        instance.origin = request.POST.get('origin')
        instance.destination = request.POST.get('destination')
        instance.final_destination = request.POST.get('final_destination')
        instance.product = request.POST.get('product')
        instance.description = request.POST.get('description')
        instance.unit = request.POST.get('unit')
        instance.quantity = request.POST.get('quantity')
        instance.weight = request.POST.get('weight')
        instance.dimension = request.POST.get('dimension')
        instance.client_currency = request.POST.get('client_currency')
        instance.rate = request.POST.get('rate')
        instance.terms = request.POST.get('terms')

        instance.save()
        return render(request, 'logistics/approvequotation.html', {'quotation':instance})




    freight_types = FreightType.objects.all()
    jobs = JobCategory.objects.all()
    types = Type.objects.all()
    payment_types = PaymentType.objects.all()
    client_currency = ClientCurrency.objects.all()
    context = {'instance': instance, 'freight_types':freight_types, 'jobs':jobs,
                        'types':types, 'payment_types':payment_types,
                         'client_currency':client_currency}

    return render(request, 'logistics/updatequotation.html', context)






