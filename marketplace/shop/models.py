from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class CustomerUser(AbstractUser):
    """
    ROLE_CHOICES - variants of roles: buyer, seller (1st in db - 2nd in admin panel)
    
    role - field for role (max 10 symbols)
    """
    ROLE_CHOICES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="buyer")

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

    seller = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

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

    buyer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    products = models.ManyToManyField(Product)

    created_at = models.DateTimeField(auto_now_add=True)

    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id} by {self.buyer.username}"

class Category(models.Model):
    """
    name - name/str of category, contains max 100 symbols
    
    magic method __str__ - return name of category in admin panel
    
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Review(models.Model):
    """
    product - linked with review, if product'll be deleted - all reviews too
    
    author - linked with user, who made review

    rating - (e.g in scale 1-5)

    comment - comment by product

    created_at - time when review of product was created
        *- DateTimeField(auto_now_add=True) - date will be made automatically
    
    magic method __str__ - return review in admin panel (name product and author)
    
    """
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="reviews")
    
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    rating = models.IntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.author.username}"

class ShippingInfo(models.Model):
    """
    order -
    *- OneToOneField -
        one order can include one shipping
        (one-to-one)
    
    address, city, postal_code, country - fields of shipping
    
    magic method __str__ - return order and total address in admin panel
    """
    order = models.OneToOneField("Order", on_delete=models.CASCADE, related_name="shipping_info")

    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.order} - {self.address}"

"""
cmds:

python manage.py makemigrations
python manage.py migrate
"""