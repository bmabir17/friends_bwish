from datetime import date, datetime
import json
from django.http import JsonResponse
from django.shortcuts import render
# from django import generics, status
# from django import Response
from .models import Customer
# from .serializers import CustomerSerializer
# Create your views here.

# from .models import Customer
from django.views.decorators.csrf import csrf_exempt

# @app.task
# def send_birthday_emails():
#     today = date.today()
#     for customer in Customer.objects.all():
#         if customer.birthday.month == today.month and customer.birthday.day == today.day:
#             # Simulate email sending (Optional)
#             print(f"Sending birthday email to {customer.name}")
#             # Implement logic to track sent emails for the year (Optional)




# def customer_register(request):
#     product_type_form = RegistrationForm()
#     context = {'product_type_form': product_type_form}
#     # print(settings.TEMPLATES[0]['DIRS'])

#     return render(request, 'dashboard.html', context=context)

@csrf_exempt
def submit_customer_register(request):

    if request.method == 'POST':
        received_data = json.loads(request.body)
        date = received_data.get('date')
        cust_name = received_data.get('cust_name')
        cust_email = received_data.get('cust_email')
        print(f'Input Date {date}')
        print(f'Input cust_name {cust_name}')
        print(f'Input cust_email {cust_email}')

        date=datetime.strptime(date, '%Y-%m-%d')

        #check if email exists
        if Customer.objects.filter(email=cust_email).exists():
            data = {'message': f'Email: {cust_email} Alredy Registered'}
        else:
            customer_date=Customer(
                name=cust_name,
                email=cust_email,
                birthday=date
            )
            customer_date.save()
            data = {'message': f' Customer Registered Successfully'}

    return JsonResponse(data)