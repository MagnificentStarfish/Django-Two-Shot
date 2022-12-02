from django.shortcuts import render
from receipts.models import Receipt


def receipt_view(request):
    receipt = Receipt.objects.all()
    context = {
        "receipt_view": receipt,
    }
    return render(request, "receipts/list.html", context)
