from django.shortcuts import render, redirect
from receipts.models import Receipt, ExpenseCategory, Account
from django.contrib.auth.decorators import login_required
from receipts.forms import ReceiptForm, AccountForm, ExpenseCategoryForm


@login_required
def receipt_view(request):
    # receipt = Receipt.objects.all()
    receipt = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipt_view": receipt,
    }
    return render(request, "receipts/list.html", context)


@login_required
def category_list(request):
    category = ExpenseCategory.objects.filter(owner=request.user)
    context = {"category_list": category}
    return render(request, "receipts/categories.html", context)


@login_required
def account_list(request):
    account = Account.objects.filter(owner=request.user)
    context = {"account_list": account}
    return render(request, "receipts/accounts.html", context)


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


@login_required
def create_account(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            create_account = form.save()
            return redirect("home")


@login_required
def create_expensecategory(request):
    if request.method == "POST":
        form = ExpenseCategoryForm(request.POST)
        if form.is_valid():
            create_receipt = form.save(commit=False)
            create_receipt.owner = request.user
            create_receipt.save()
            return redirect("category_list")
    else:
        form = ExpenseCategoryForm

    context = {"form": form}

    return render(request, "receipts/categories/create.html", context)
