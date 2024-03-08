from django.contrib import admin
from .models import Customers, Update_Currency, Flights, Shipping_Agents, Enquiries, Quotations, Approved_Quotations, Tracking_Data, Orders, Invoices, FreightType, JobCategory, Type

@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact', 'address', 'city', 'state',
                     'country', 'postal', 'profile_picture')
    
@admin.register(Update_Currency)
class Update_CurrencyAdmin(admin.ModelAdmin):
    list_display = ('currency_type', 'rate')

@admin.register(Flights)
class FlightsAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'country')


@admin.register(Shipping_Agents)
class Shipping_AgentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'account_num', 'code')


@admin.register(Enquiries)
class EnquiriesAdmin(admin.ModelAdmin):
    list_display = ('scope_of_work', 'enquiry_date','status', 'job_category',
                     'customer_name', 'email', 'phone', 'contact_person','sales_person',
        'sales_team', 'freight_type', 'type', 'enquiry_details', 'priority_tags')


@admin.register(Quotations)
class QuotationsAdmin(admin.ModelAdmin):
    list_display = ('customer_name','job_category','payment_type','sales_person',
                    'origin','destination','final_destination','freight_type',
                    'type','quotation_date','client_currency','rate','product',
                    'description','unit','quantity','weight','dimension')

@admin.register(Approved_Quotations)
class Approved_QuotationsAdmin(admin.ModelAdmin):
        list_display = ('customer_name','job_category','payment_type','sales_person',
                    'origin','destination','final_destination','freight_type',
                    'type','enquiry_date','client_currency','rate','product',
                    'description','units','quantity','weight','dimensions','price','approved_by')
        


@admin.register(Tracking_Data)
class Tracking_DataAdmin(admin.ModelAdmin):
     list_display = ('tracking_number', 'date', 'operator','status','remarks', 'customer_name')



@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
     list_display = ('customer_name','job_category','payment_type','freight_type',
                     'type','airline','flight_number','origin','destination',
                     'shipper_name','shipper_acc_num','shipper_address',
                     'consignee_name','consignee_acc_num','consignee_address',
                     'shipping_agent','shipping_agent_acc_num','shipping_agent_code',
                     'date')
     


@admin.register(Invoices)
class InvoicesAdmin(admin.ModelAdmin):
     list_display = ('invoice_id','sender_name','sender_email','sender_contact',
                     'sender_address','recepient_name','recepient_email',
                     'recepient_contact','recepient_address','product_weight',
                     'product_quantity','date','time','total_amount','sub_total')

admin.site.register(FreightType)

admin.site.register(JobCategory)

admin.site.register(Type)