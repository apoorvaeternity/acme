from django.urls import path
from .views import FileUploadView

app_name = 'core'

urlpatterns = [
    path('product/upload/', FileUploadView.as_view(), name='product-upload')
]
