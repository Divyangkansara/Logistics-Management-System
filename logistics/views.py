import threading
import pdfkit
from django.shortcuts import render , redirect, get_object_or_404, HttpResponse
from .models import Enquirie, FreightType, JobCategory, Type, Quotation, PaymentType, ClientCurrency, Order
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .middlewares import auth, user
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import JsonResponse


#  home page
def home(request):
    if request.user.is_authenticated:
        user = request.user
        user_name = user.get_username()
        return render(request, 'logistics/home.html', {'username':user_name})
    return render(request, 'logistics/home.html')

@ user
#  signup
def signup_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, email=email, password=password)
        group = Group.objects.get(name='Staff')
        user.groups.add(group)
        messages.success(request, 'Please login to continue.')
        return redirect('login_form') 
    else:
        return render(request, 'logistics/login_form.html')


@ user
# login
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)    
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Invalid username or password')
            return render(request, 'logistics/login_form.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'logistics/login_form.html')
    

def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You have successfully logged out!')
        return redirect('home')
    


@login_required(login_url='/login')
def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        user_name = user.get_username()
        return render(request, 'logistics/dashboard.html', {'username':user_name})



# enquiry list    
@ login_required(login_url='/login')
def enquiries(request):
    if request.user.is_authenticated:
        enquiry_data = Enquirie.objects.all()
        user = request.user
        user_name = user.get_username()
        gps = user.groups.all()
        return render(request, 'logistics/enquiry_list.html', {'data':enquiry_data,
                                                               'username':user_name,
                                                              'groups':gps})



# Add enquiry
@ login_required(login_url='/login')
def submit_enquiry(request):
    if request.user.is_authenticated:
        user = request.user
        user_name = user.get_username()
        if request.method == 'POST':
            data = request.POST.dict()
            data.pop("csrfmiddlewaretoken")
            data['enquiry_date'] = request.POST.get('enquiry_date')
            enquiry = Enquirie.objects.create(**data)
            return render(request, 'logistics/edit_enquiry.html', {'order': enquiry, 'username':user_name})
    
    return render(request, 'logistics/enquiry_form.html', {'username':user_name})


#  Enquiry Information 
@ login_required(login_url='/login')
def edit_enquiry(request, id): 
    instance = get_object_or_404(Enquirie, pk=id)   
    return render(request, 'logistics/edit_enquiry.html', {'order':instance})



#  Update Enquiry Information
@ login_required(login_url='/login')
def update_enquiry(request, id):
    instance = get_object_or_404(Enquirie, pk=id)
    if request.user.is_authenticated:
        user = request.user
        user_name = user.get_username()
        if request.method == 'POST':
            data = request.POST.dict()
            data.pop('csrfmiddlewaretoken')
            data['enquiry_date'] = request.POST.get('enquiry_date')
            instance.__dict__.update(data)
            instance.save()
            return render(request, 'logistics/edit_enquiry.html', {'order': instance, 'username':user_name})
        
        freight_types = FreightType.objects.all()
        jobs = JobCategory.objects.all()
        types = Type.objects.all()
        context = {'instance': instance, 'freight_types':freight_types, 'jobs':jobs,
                            'types':types, 'username':user_name}
    
    return render(request, 'logistics/update_form.html', context)    



#  all quotations
@ login_required(login_url='/login')
def all_quotations(request):
    if request.user.is_authenticated:
        user = request.user
        user_name = user.get_username()
        quotations = Quotation.objects.all()
        return render(request, 'logistics/quotation_list.html', {'data':quotations,
                                                               'username':user_name})


# Add Quotation
@ login_required(login_url='/login')  
def quotation_management(request, id):
    if request.user.is_authenticated:
        user = request.user
        user_name = user.get_username()
        instance = get_object_or_404(Enquirie, pk=id)
        freight_types = FreightType.objects.all()
        jobs = JobCategory.objects.all()
        types = Type.objects.all()
        context = {'instance': instance, 'freight_types':freight_types, 'jobs':jobs,
                            'types':types, 'username':user_name}
    return render(request, 'logistics/quotation.html', context)




#  Save Quotation
@ login_required(login_url='/login')
def save_quotation(request, id):
    if request.user.is_authenticated:
        user = request.user
        user_name = user.get_username()
        instance = get_object_or_404(Enquirie, pk=id)

        if request.method == 'POST':
            data = request.POST.dict()
            data.pop('csrfmiddlewaretoken')
            data['quotation_date'] = request.POST.get('quotation_date')
            data['enquiry']  = instance
            quotation = Quotation.objects.create(**data)   
            return render(request, 'logistics/approve_quotation.html', {'quotation':quotation,
                                     'instance':instance, 'username':user_name})
    return render(request, 'logistics/quotation.html')


#  Update Quotation Information
@ login_required(login_url='/login')
def update_quotation(request, quotation_id, enquiry_id):
    if request.user.is_authenticated:
        user = request.user
        user_name = user.get_username()
        instance = get_object_or_404(Quotation, pk=quotation_id)
        enquiry = get_object_or_404(Enquirie, pk=enquiry_id)
        if request.method == 'POST':
            data = request.POST.dict()
            data.pop('csrfmiddlewaretoken')
            data['quotation_date'] = request.POST.get('quotation_date')
            instance.__dict__.update(data)
            instance.save()
            return render(request, 'logistics/approve_quotation.html', {'quotation':instance,
                                      'instance':enquiry, 'username':user_name})
        freight_types = FreightType.objects.all()
        jobs = JobCategory.objects.all()
        types = Type.objects.all()
        payment_types = PaymentType.objects.all()
        client_currency = ClientCurrency.objects.all()
        context = {'quotation': instance, 'freight_types':freight_types, 'jobs':jobs,
                            'types':types, 'payment_types':payment_types,
                            'client_currency':client_currency, 'instance':enquiry, 'username':user_name}

    return render(request, 'logistics/update_quotation.html', context)




#  send email
@ login_required(login_url='/login')
def sending_email(request, enquiry_id, quotation_id):
    if request.user.is_authenticated:
        user = request.user
        user_name = user.get_username()
        print("sending email", enquiry_id, quotation_id)
        enquiry = get_object_or_404(Enquirie, pk=enquiry_id)

        threading.Thread(target=lambda: send_mail(
            'Testing Mail',
            'Here is the testing message. Just for confirmation. Logistics Management System project',
            'divyang.kansara@technostacks.com',
            [enquiry.email],
            fail_silently=False
        )).start()

        quotation = get_object_or_404(Quotation, pk=quotation_id)
        return render(request, 'logistics/sent_email.html', {'quotation':quotation,
                                                            'instance':enquiry, 'username':user_name})





#  Creating Order 
@ login_required(login_url='/login')
def pending_order(request, enquiry_id, quotation_id):
    if request.user.is_authenticated:
        user = request.user
        user_name = user.get_username()
        enquiry = get_object_or_404(Enquirie, pk=enquiry_id)
        quotation = get_object_or_404(Quotation, pk=quotation_id)
        if request.method == 'POST':
            data = request.POST.dict()
            data.pop('csrfmiddlewaretoken')
            data['order_date'] = request.POST.get('order_date')
            data['flight_date'] = request.POST.get('flight_date')
            data['quotation']  = quotation
            order = Order.objects.create(**data)
            return render(request, 'logistics/confirm_orders.html', {'order':order,
                                                                    'instance':enquiry,
                                                                    'quotation':quotation,
                                                                    'username':user_name})
    return render(request, 'logistics/orders.html', {'instance':enquiry,
                                                     'quotation':quotation,
                                                     'username':user_name})



#  Update Order Information
@ login_required(login_url='/login')
def update_order(request, order_id, enquiry_id, quotation_id):
    if request.user.is_authenticated: 
        user = request.user
        user_name = user.get_username()
        instance = get_object_or_404(Order, pk=order_id)
        enquiry = get_object_or_404(Enquirie, pk=enquiry_id)
        quotation = get_object_or_404(Quotation, pk=quotation_id)
        context = {'order':instance, 'instance':enquiry, 'quotation':quotation, 'username':user_name}
        if request.method == 'POST':
            data = request.POST.dict()
            data.pop('csrfmiddlewaretoken')
            data['order_date'] = request.POST.get('order_date')
            data['flight_date'] = request.POST.get('flight_date')
            instance.__dict__.update(data)
            instance.save()
            return render(request, 'logistics/confirm_orders.html', context)
    return render(request, 'logistics/update_order.html', context)





#  Invoice
@ login_required(login_url='/login')
def invoice(request, enquiry_id, quotation_id, order_id):
     if request.user.is_authenticated:
        user = request.user
        user_name = user.get_username()
        enquiry = get_object_or_404(Enquirie, pk=enquiry_id)
        quotation = get_object_or_404(Quotation, pk=quotation_id)
        order = get_object_or_404(Order, pk=order_id)
        return render(request, 'logistics/invoice.html', {'username':user_name,
                                                          'instance':enquiry,
                                                          'quotation':quotation,
                                                          'order':order})
     
def temp_invoice(request, enquiry_id, quotation_id, order_id):
    enquiry = get_object_or_404(Enquirie, pk=enquiry_id)
    quotation = get_object_or_404(Quotation, pk=quotation_id)
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'logistics/temp_invoice.html', {'instance':enquiry,
                                                            'quotation':quotation,
                                                            'order':order})



def send_email_async(subject, message, sender, recipient, attachment_filename, attachment_content, attachment_content_type):
    email = EmailMessage(subject, message, sender, [recipient])
    email.attach(attachment_filename, attachment_content, attachment_content_type)
    email.send()

def print_pdf(request, enquiry_id, quotation_id, order_id):
    enquiry = get_object_or_404(Enquirie, pk=enquiry_id)
    quotation = get_object_or_404(Quotation, pk=quotation_id)
    order = get_object_or_404(Order, pk=order_id)
    template = render_to_string('logistics/temp_invoice.html', {'instance':enquiry,
                                                                'quotation':quotation,
                                                                'order':order})
   
    pdf = pdfkit.from_string(template, False)
    filename = f"invoice_1{enquiry.id}.pdf"
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="' + filename + '"'

    subject = f'Invoice [EQ-1{enquiry.id}] for {quotation.product}'
    message = f"Dear {enquiry.customer_name},\n\nwe hope you're well. Please find the invoice [EQ-1{enquiry.id}] attached. Please feel free to reach out if you have any questions. \n\nThank you. \n "

    threading.Thread(
        target=send_email_async,
        args=(subject, message, 'divyang.kansara@technostacks.com', enquiry.email, filename, response.content, 'application/pdf')
    ).start()

    return response 



#  Track Orders
def track_order(request):
    if request.method == 'POST':
        tracking_email = request.POST.get('tracking_email')
        tracking_num = request.POST.get('tracking_num')
        try:
            order = Order.objects.get(order_id = tracking_num , quotation__enquiry__email = tracking_email)
            status = order.status
            return JsonResponse({'order':status})
        except Order.DoesNotExist:
            return JsonResponse({'error':'No data found for the given tracking number'})
    return render(request, 'logistics/track_order.html')
