from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from main_app.serializers import UserSerializer
from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.permissions import IsAuthenticated
from main_app.serializers import (
    ProductSerializer,
    OrderSerializer,
    UserSerializer,
)
from main_app.models import Product, Order, User


class UserView(GenericViewSet,
               mixins.ListModelMixin,  # TODO: remove after tests are completed
               mixins.CreateModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ProductView(GenericViewSet,
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin):
    permission_classes = (IsAuthenticated, )
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class OrderView(GenericViewSet,
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin):
    permission_classes = (IsAuthenticated, )
    serializer_class = OrderSerializer
    queryset = Order.objects.all()