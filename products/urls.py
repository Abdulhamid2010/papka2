from django.urls import path
from .views import  ProductViewSet,ProductCreateAPIView

urlpatterns = [
    path('', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='product-list'),
    path('create/', ProductCreateAPIView.as_view(), name='product-create'),
]