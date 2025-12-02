from django.urls import path
from .views import index, create_subscription


urlpatterns = [
    path("", index),
    path("createsubscription/", create_subscription, name="create_subscription")
]