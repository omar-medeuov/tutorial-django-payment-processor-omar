from django.urls import path
from . import views
urlpatterns = [
    path("confirm/<int:order_id>/<str:order_secret>", views.confirm),
    path("orders/<int:order_id>", views.order),
]