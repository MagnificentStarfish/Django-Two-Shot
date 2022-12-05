from django.shortcuts import render, redirect
from receipts.models import Receipt
from django.contrib.auth.decorators import login_required
from receipts.forms import ReceiptForm


@login_required
def receipt_view(request):
    # receipt = Receipt.objects.all()
    receipt = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipt_view": receipt,
    }
    return render(request, "receipts/list.html", context)


@login_required
def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():

            create_receipt = form.save(commit=False)
            create_receipt.purchaser = request.user
            create_receipt.save()
            return redirect("home")

    else:
        form = ReceiptForm

    context = {"form": form}

    return render(request, "receipts/create.html", context)
