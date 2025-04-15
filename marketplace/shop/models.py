from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """
    Model which represents product(s) by seller

    seller - owner of product (User)
        *- ForeignKey - one user can create many products (many-to-one)
            *- on_delete=models.CASCADE - if user'll be deleted, his all products will be too

    title - name of product
        *- CharField - str with max length 255 symbols

    description - full desc. of product (huge amount of text)
        *- TextField - field for containing desc. (without limits of length)

    price - price of product
        *- DecimalField - field for containing digits (price)
            *- max_digits=10 - max amount of all digits (include after point)
            *- decimal_places=2 - amount of digits after point

    created_at - time when product was created
        *- DateTimeField(auto_now_add=True) - date will be made automatically

    magic method __str__ - return name of product in admin panel or by printing

    """

    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)

    description = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    """
    Model for ordering product(s) by buyer

    buyer - person, who makes order (User)
    *- ForeignKey - one user can make many orders (many-to-one)
        *- on_delete=models.CASCADE - if user'll be deleted, his all orders will be too

    products -
        *- ManyToManyField(Product) -
            one order can include many products
            one product can be included in diff. orders
            (many-to-many)

    created_at - when order was created
        *- DateTimeField(auto_now_add=True) - date will be made automatically

    is_paid - check was order paid or not
        *- default=False

    magic method __str__ - return str, which contains name of buyer and id of order
    """

    buyer = models.ForeignKey(User, on_delete=models.CASCADE)

    products = models.ManyToManyField(Product)

    created_at = models.DateTimeField(auto_now_add=True)

    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id} by {self.buyer.username}"



"""
cmds:

python manage.py makemigrations
python manage.py migrate
"""