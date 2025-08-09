from rest_framework import serializers
from .models import Restaurant, MenuItem, Table, Order, OrderItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

class RestaurantSerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(many=True, read_only=True)
    class Meta:
        model = Restaurant
        fields = '__all__'

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        total = 0
        for it in items_data:
            menu_item = it['menu_item']
            qty = it.get('quantity',1)
            oi = OrderItem.objects.create(order=order, menu_item=menu_item, quantity=qty, price=menu_item.price*qty)
            total += oi.price
        order.total = total
        order.save()
        return order