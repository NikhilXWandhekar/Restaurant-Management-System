from django.contrib import admin
from .models import Restaurant, MenuItem, Table, Order, OrderItem

admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(Table)
admin.site.register(Order)
admin.site.register(OrderItem)