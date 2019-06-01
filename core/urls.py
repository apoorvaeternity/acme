from django.urls import path
from .views import FileUploadView, HomeView, ProductDeleteView, ProductView

app_name = 'core'

urlpatterns = [
    path('product/upload/', FileUploadView.as_view(), name='product-upload'),
    path('product/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('product/', ProductView.as_view(), name='product'),
    path('', HomeView.as_view(), name='home'),
]
