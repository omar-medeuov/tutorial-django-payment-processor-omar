import json
from django.http import HttpResponse
from django.shortcuts import render
from .models import Order

from the_project.settings import STRIPE_SECRET_KEY


def confirm(request, order_id: int, order_secret: str):
    order = Order.objects.get(pk=order_id)
    if order.secret == order_secret:
        order.paid = True
        order.save()
    return HttpResponse("OK") # The return value does not matter

def pay(request):
    #Payment functionality. By tutorial can be in any view function.
    order = Order.objects.create(
        amount = 1000, #can be a custom amount
    )
    order.generate_secret()
    order.save()

    #Payment data
    data = {
        "amount": 100, #product.price*100,
        "success_url":
        f"https://website.com/confirm/{order.id}/{order.secret}",
        "back_url": f"https://website.com/orders/{order.id}",
    }
    url="httpsLstage-api.ioka.kz/v2/orders"
    response = request.post(url, headers={
        "API-KEY": STRIPE_SECRET_KEY,
        "Content-Type": "application/json"
    }, data=json.dumps(data))