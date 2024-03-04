from django.db import models

#  customers-model 
class Customers(models.Model):
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
class Flights(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10, unique=True)
    country = models.CharField(max_length=50)


#  shipping agents
class Shipping_Agents(models.Model):
    name = models.CharField(max_length=50)
    account_num = models.CharField(max_length=10, unique=True)
    code = models.CharField(max_length=10, unique=True)



#  create enquiries
class Enquiries(models.Model):
    scope_of_work = models.TextField()
    enquiry_date = models.DateField()
    status = models.CharField(max_length=20, default='enquiry')
    job_category = models.CharField(max_length=20, default='sales')
    customer_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=15, unique=True, null=True)
    contact_person = models.CharField(max_length=50, unique=True, null=True)
    sales_person = models.CharField(max_length=50, unique=True, null=True)
    sales_team = models.CharField(max_length=20)
    freight_type = models.CharField(max_length=20, choices=[('air freight',
                        'air freight'),('sea freight', 'sea freight')])
    type = models.CharField(max_length=20, default='export')
    enquiry_details = models.TextField()
    priority_tags = models.CharField(max_length=20, default='normal', choices=
                      [('low', 'low'),('normal', 'normal'), ('high', 'high')])
    

#  quotation management
class Quotations(models.Model):
    customer_name = models.ForeignKey(Customers, on_delete=models.CASCADE)
    job_category = models.CharField(max_length=20, default='sales')
    payment_type = models.CharField(max_length=20, choices=[('pending','pending'),
                                                     ('collect','collect')])
    sales_person = models.CharField(max_length=50, unique=True, null=True)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    final_destination = models.CharField(max_length=255, null=True, blank=True)
    freight_type = models.CharField(max_length=20, choices=[('air freight',
                        'air freight'),('sea freight', 'sea freight')])
    type = models.CharField(max_length=20, default='export')
    enquiry_date = models.DateField()
    client_currency = models.CharField(max_length=20, choices=[('USD','USD'),
                                            ('AED','AED'),('INR','INR')])
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.CharField(max_length=50)
    description = models.TextField()
    units = models.CharField(max_length=10)
    quantity = models.IntegerField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    dimensions = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)

#  quotation approval
class Approved_Quotations(models.Model):
    customer_name = models.ForeignKey(Customers, on_delete=models.CASCADE)
    job_category = models.CharField(max_length=20, default='sales')
    payment_type = models.CharField(max_length=20, choices=[('pending','pending'),
                                                     ('collect','collect')])
    sales_person = models.CharField(max_length=50, unique=True, null=True)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    final_destination = models.CharField(max_length=255, null=True, blank=True)
    freight_type = models.CharField(max_length=20, choices=[('air freight',
                        'air freight'),('sea freight', 'sea freight')])
    type = models.CharField(max_length=20, default='export')
    enquiry_date = models.DateField()
    client_currency = models.CharField(max_length=20, choices=[('USD','USD'),
                                            ('AED','AED'),('INR','INR')])
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.CharField(max_length=50)
    description = models.TextField()
    units = models.CharField(max_length=10)
    quantity = models.IntegerField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    dimensions = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    approved_by = models.CharField(max_length=50)


# orders
class Orders(models.Model):
    customer_name = models.ForeignKey(Customers, on_delete=models.CASCADE)
    job_category = models.CharField(max_length=20, default='sales')
    payment_type = models.CharField(max_length=20, choices=[('pending','pending'),
                                                     ('collect','collect')])
    freight_type = models.CharField(max_length=20, choices=[('air freight',
                        'air freight'),('sea freight', 'sea freight')])
    type = models.CharField(max_length=20, default='export')
    airline = models.CharField(max_length=50)
    flight_number = models.IntegerField(unique=True)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    shipper_name = models.CharField(max_length=500)
    shipper_acc_num = models.IntegerField(unique=True)
    shipper_address = models.TextField(max_length=255, unique=True)
    consignee_name = models.CharField(max_length=500)
    consignee_acc_num = models.IntegerField(unique=True)
    consignee_address = models.TextField(max_length=255, unique=True)
    shipping_agent = models.CharField(max_length=50)
    shipping_agent_acc_num = models.IntegerField(unique=True)
    shipping_agent_code = models.IntegerField(unique=True)
    date = models.DateField()


# tracking data
class Tracking_Data(models.Model):
    customer_name = models.ForeignKey(Customers, on_delete=models.CASCADE)
    tracking_number = models.IntegerField(unique=True)
    date = models.DateField()
    operator = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('In transit','In transit'),
                                ('delivered','delivered'),('done','done')])
    remarks = models.TextField(max_length=100, null=True, blank=True)


#  invoices
class Invoices(models.Model):
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
    



