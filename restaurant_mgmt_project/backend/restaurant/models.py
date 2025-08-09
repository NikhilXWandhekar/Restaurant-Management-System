from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    CATEGORY_CHOICES = [('starter','Starter'),('main','Main Course'),('dessert','Dessert'),('drink','Drink')]
    restaurant = models.ForeignKey(Restaurant, related_name='menu_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='main')
    available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.restaurant.name}'

class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='tables', on_delete=models.CASCADE)
    number = models.IntegerField()
    capacity = models.IntegerField(default=4)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'Table {self.number} ({self.restaurant.name})'

class Order(models.Model):
    STATUS_CHOICES = [('pending','Pending'),('preparing','Preparing'),('served','Served'),('cancelled','Cancelled')]
    restaurant = models.ForeignKey(Restaurant, related_name='orders', on_delete=models.CASCADE)
    table = models.ForeignKey(Table, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def save(self, *args, **kwargs):
        self.price = self.menu_item.price * self.quantity
        super().save(*args, **kwargs)