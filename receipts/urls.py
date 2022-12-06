from django.urls import path
from receipts.views import receipt_view, create_receipt, category_list, account_list

urlpatterns = [
    path("", receipt_view, name="home"),
    path("create/", create_receipt, name="create_receipt"),
    path("categories/", category_list, name="category_list"),
    path("accounts/", account_list, name="account_list"),
]
