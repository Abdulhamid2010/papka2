from rest_framework import viewsets
from .serializers import ProductSerializers,CreateAPIView
from .models import Product

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class ProductCreateAPIView(viewsets.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers