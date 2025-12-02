from django.http import HttpResponse
import stripe
from django.shortcuts import render
from the_project.settings import STRIPE_SECRET_KEY as sk


def index(request):



    return render(request,"index.html")


def create_subscription(request, name="Starter Subscription", description="$12/Month subscription"):
    stripe.api_key = sk
    # try:
    starter_subscription = stripe.Product.create(name=name, description=description)
    return HttpResponse(starter_subscription.id)
    # except:
    #     return HttpResponse("No subscription could be created")

