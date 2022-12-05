from django.shortcuts import render
from receipts.models import Receipt
from django.contrib.auth.decorators import login_required


@login_required
def receipt_view(request):
    # receipt = Receipt.objects.get(username == purchaser)
    # receipt = Receipt.objects.all()
    receipt = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipt_view": receipt,
    }
    return render(request, "receipts/list.html", context)
