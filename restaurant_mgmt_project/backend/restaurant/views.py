from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Restaurant, MenuItem, Table, Order, OrderItem
from .serializers import RestaurantSerializer, MenuItemSerializer, TableSerializer, OrderSerializer, OrderItemSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer

    @action(detail=True, methods=['post'])
    def set_status(self, request, pk=None):
        order = self.get_object()
        status_val = request.data.get('status')
        if status_val in dict(Order.STATUS_CHOICES):
            order.status = status_val
            order.save()
            return Response({'status':'ok'})
        return Response({'error':'invalid status'}, status=400)