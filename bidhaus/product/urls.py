from django.urls import path

from product.views import ProductDetail
from product.views import ProductList


app_name = "product"

urlpatterns = [
    path("", ProductList.as_view(), name="product-list"),
    path("<int:pk>/", ProductDetail.as_view(), name="product-detail"),
]
