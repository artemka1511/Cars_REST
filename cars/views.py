from django.shortcuts import render
from rest_framework import generics
from cars.serializers import CarDetailSerializer, CarListDetailSerializer
from cars.models import Car
from cars.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class CarsListView(generics.ListAPIView):
    serializer_class = CarListDetailSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticated, )


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
