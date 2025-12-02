from pydoc import describe

try:
    import stripe
    print("success importing stripe library")
except:
    print("cannot import stripe")


stripe.api_key = "sk_test_51RPeaAKkX97SaZuk7qJzrqAkTYp2ul8c6uniXYpMyQt1chFp101IkQkyBJPM9zejhQlWtOvGMaiazSYmhjuhQXB7009iMMSB8p"

starter_subscription = stripe.Product.create(
    name="Starter Subscription",
    description="$12/Month subscription",
)

starter_subscription_price = stripe.Price.create(
    unit_amount=1200,
    currency="usd",
    recurring={"interval": "month"},
    product=starter_subscription['id'],
)

# Save these identifiers
print(f"Success! Here is your starter subscription product id: {starter_subscription.id}")
print(f"Success! Here is your starter subscription price id: {starter_subscription_price.id}")