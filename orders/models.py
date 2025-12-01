import random
from django.db import models


class Order(models.Model):
    secret = models.CharField(max_length=1000, default="", blank=True)
    amount = models.DecimalField(default=0)
    paid = models.BooleanField(default=False)
    checkout_url = models.CharField(max_length=1000, default="", blank=True)

    def generate_secret(self):
        self.secret = str(random.randint(10000, 99999))