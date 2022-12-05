from django.urls import path
from receipts.views import receipt_view, create_receipt

urlpatterns = [
    path("", receipt_view, name="home"),
    path("create/", create_receipt, name="create_receipt"),
]
