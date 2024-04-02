from django.contrib import admin
from .models import Customer, Update_Currency, Flight, Shipping_Agent, Enquirie, Quotation, Tracking_Data, Order, Invoice, FreightType, JobCategory, Type, PaymentType, ClientCurrency

@admin.register(Customer)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact', 'address', 'city', 'state',
                     'country', 'postal', 'profile_picture')
    
@admin.register(Update_Currency)
class Update_CurrencyAdmin(admin.ModelAdmin):
    list_display = ('currency_type', 'rate')

@admin.register(Flight)
class FlightsAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'country')


@admin.register(Shipping_Agent)
class Shipping_AgentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'account_num', 'code')


@admin.register(Enquirie)
class EnquiriesAdmin(admin.ModelAdmin):
    list_display = ('scope_of_work', 'enquiry_date','status', 'job_category',
                     'customer_name', 'email', 'phone', 'contact_person','sales_person',
        'sales_team', 'freight_type', 'type', 'enquiry_details', 'priority_tags')


@admin.register(Quotation)
class QuotationsAdmin(admin.ModelAdmin):
    list_display = ('customer_name','job_category','payment_type','sales_person',
                    'origin','destination','final_destination','freight_type',
                    'type','quotation_date','client_currency','rate','product',
                    'description','unit','quantity','weight','dimension')        


@admin.register(Tracking_Data)
class Tracking_DataAdmin(admin.ModelAdmin):
     list_display = ('tracking_number', 'date', 'operator','status','remarks', 'customer_name')



@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
     list_display = ('airline','flight_number','origin','destination',
                     'shipper_name','shipper_acc_num','shipper_address',
                     'consignee_name','consignee_acc_num','consignee_address',
                     'shipping_agent','shipping_agent_acc_num',
                     'order_date', 'flight_date', 'notify_name', 'notify_acc', 'notify_add')
     


@admin.register(Invoice)
class InvoicesAdmin(admin.ModelAdmin):
     list_display = ('invoice_id','sender_name','sender_email','sender_contact',
                     'sender_address','recepient_name','recepient_email',
                     'recepient_contact','recepient_address','product_weight',
                     'product_quantity','date','time','total_amount','sub_total')

admin.site.register(FreightType)

admin.site.register(JobCategory)

admin.site.register(Type)

admin.site.register(PaymentType)

admin.site.register(ClientCurrency)

admin.site.site_header = 'Logistics Management System'
admin.site.index_title = 'Logistics Management System'