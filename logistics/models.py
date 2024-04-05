import random
import secrets
import string
from django.db import models
from django.contrib.auth.models import User

#  customers-model 
class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    contact = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal = models.CharField(max_length=10)
    profile_picture = models.ImageField(upload_to='customer_photos/', null=True, 
                                        blank=True)
    

#  update currency rate
class Update_Currency(models.Model):
    currency_type = models.CharField(max_length=50)
    rate = models.DecimalField(max_digits=10, decimal_places=2)


#  flights 
class Flight(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10, unique=True)
    country = models.CharField(max_length=50)


#  shipping agents
class Shipping_Agent(models.Model):
    name = models.CharField(max_length=50)
    account_num = models.CharField(max_length=10, unique=True)
    code = models.CharField(max_length=10, unique=True)



#  create enquiries
class Enquirie(models.Model):
        scope_of_work = models.TextField()
        enquiry_date = models.DateField()
        status = models.CharField(max_length=30, default='Enquiry')
        job_category = models.CharField(max_length=30, default='sales')
        customer_name = models.CharField(max_length=50)
        email = models.EmailField(max_length=50)
        phone = models.CharField(max_length=30, default='1212121212')
        contact_person = models.CharField(max_length=50)
        sales_person = models.CharField(max_length=50)
        sales_team = models.CharField(max_length=30)
        freight_type = models.CharField(max_length=30, choices=[('air freight',
                            'air freight'),('sea freight', 'sea freight')])
        type = models.CharField(max_length=30, default='export')
        enquiry_details = models.TextField()


#  quotation management
class Quotation(models.Model):
    # customer_name = models.ForeignKey(Customers, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=50)
    job_category = models.CharField(max_length=20, default='sales')
    payment_type = models.CharField(max_length=20, choices=[('pending','pending'),
                                                     ('collect','collect')])
    sales_person = models.CharField(max_length=50, default='')
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    final_destination = models.CharField(max_length=255, null=True, blank=True)
    freight_type = models.CharField(max_length=20, choices=[('air freight',
                        'air freight'),('sea freight', 'sea freight')])
    type = models.CharField(max_length=20, default='export')
    quotation_date = models.DateTimeField()
    client_currency = models.CharField(max_length=20, choices=[('USD','USD'),
                                            ('AED','AED'),('INR','INR')])
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.CharField(max_length=50)
    description = models.TextField()
    unit = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    dimension = models.CharField(max_length=20)
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    terms = models.CharField(max_length=100, null=True)
    enquiry = models.ForeignKey(Enquirie, on_delete=models.CASCADE, null=True, blank=True)




class Status(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return str(self.name)
    
def generate_order_id(length=6):
    random_string1 = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(length))
    random_string2 = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(length-2))
    return f"LMS-{random_string2}{random_string1}"

# orders
class Order(models.Model):

    ORDER_STATUS = (
    ("PENDING", "Pending"),
    ("IN WAREHOUSE", "in warehouse"),
    ("OUT FOR DELIVERY", "out for delivery"),
    ("DELIVERED", "delivered"),
    )

    order_id = models.CharField(max_length=20, unique=True)
    airline = models.CharField(max_length=50)
    flight_number = models.IntegerField()
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    shipper_name = models.CharField(max_length=500)
    shipper_acc_num = models.IntegerField()
    shipper_address = models.TextField(max_length=255)
    consignee_name = models.CharField(max_length=500)
    consignee_acc_num = models.IntegerField()
    consignee_address = models.TextField(max_length=255)
    shipping_agent = models.CharField(max_length=50)
    shipping_agent_acc_num = models.IntegerField()
    order_date = models.DateField(null=True, blank=True)
    flight_date = models.DateField(null=True, blank=True)
    notify_name = models.CharField(max_length=100, default='')
    notify_acc = models.IntegerField(default=0)
    notify_add = models.TextField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=25,choices=ORDER_STATUS,null=True, blank=True)
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = generate_order_id(6)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_id


# tracking data
class Tracking_Data(models.Model):
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    tracking_number = models.IntegerField(unique=True)
    date = models.DateField()
    operator = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('In transit','In transit'),
                                ('delivered','delivered'),('done','done')])
    remarks = models.TextField(max_length=100, null=True, blank=True)


#  invoices
class Invoice(models.Model):
    invoice_id = models.AutoField(unique=True, primary_key=True)
    sender_name = models.CharField(max_length=50)
    sender_email = models.EmailField(max_length=50, unique=True)
    sender_contact = models.IntegerField(unique=True)
    sender_address = models.TextField(max_length=255)
    recepient_name = models.CharField(max_length=50)
    recepient_email = models.EmailField(max_length=50, unique=True)
    recepient_contact = models.IntegerField(unique=True)
    recepient_address = models.TextField(max_length=255)
    product_weight = models.DecimalField(max_digits=10, decimal_places=2)
    product_quantity = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    sub_total  = models.DecimalField(max_digits=10, decimal_places=2)
    

#  Freight Type
class FreightType(models.Model):
    freight_type = models.CharField(max_length=50)

    def __str__(self):
        return self.freight_type



#  Job Category
class JobCategory(models.Model):
    job_category = models.CharField(max_length=50)

    def __str__(self):
        return self.job_category



#  Type  import / export
class Type(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


#  payment type
class PaymentType(models.Model):
    payment_type = models.CharField(max_length=50)

    def __str__(self):
        return self.payment_type
    

#  client currency
class ClientCurrency(models.Model):
    client_currency = models.CharField(max_length=50)
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.client_currency
    

    

