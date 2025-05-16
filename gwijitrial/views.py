from django.shortcuts import render
from django_daraja.mpesa.core import MpesaClient

from gwijitrial.models import Transaction


# Create your views here.
def home(request, checkout_id=None):
    phone_number = "0717673603"
    amount = 1
    client = MpesaClient()
    response =  client.stk_push(phone_number , amount , "VIP" , "Payment of concert tickets" , "https://example.com")
#TODO store response in a database
    merch_id = response['MerchantRequestID']
    check_id = response['CheckoutRequestID']
    Transaction.objects.create(phone = phone_number , amount = amount , merch_id = merch_id ,  checkout_id = checkout_id )
    return render(request , "home.html")