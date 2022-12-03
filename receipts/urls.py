from django.urls import path
from receipts.views import receipt_view

urlpatterns = [path("", receipt_view, name="home")]
