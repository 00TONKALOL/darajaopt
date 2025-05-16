from django.http import HttpResponse
from django.shortcuts import render
from django_daraja.mpesa.core import MpesaClient

from gwijitrial.models import Transaction


# Create your views here.
def home(request, checkout_id=None):
    phone_number = "254717673603"
    amount = 1
    client = MpesaClient()
    url = "https://crane-grown-notably.ngrok-free.app/confirm/payment"
    response =  client.stk_push(phone_number , amount , "VIP" , "Payment of concert tickets" , "https://example.com")
    merch_id = response.merchant_request_id
    check_id = response.checkout_request_id
    print("Saving")
    Transaction.objects.create(phone = phone_number , amount = amount , merchant_id = merch_id ,  check_id = check_id )
    return render(request , "home.html")


def csrf_excempt(args):
    pass
@csrf_excempt
def confirm(request):
    if request.method == "POST":
        body = request.data.get("Body")
        merch_id = body["stkCallback"]["MerchantRequestId"]
        code = body["stkCallback"]["ResultCode"]
        trans = Transaction.objects.get(merch_id = merch_id)
        if trans and code == 0:
            trans.status =  True
            trans.save()
            return HttpResponse("Success")
    return None