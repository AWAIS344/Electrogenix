from django.urls import path
from .views import Product,Product_Detail

urlpatterns = [
    path("",Product,name="product"),
    path("<int:id>/",Product_Detail,name="product_detail")
]
