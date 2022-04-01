from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Transaction
from .forms import TransactionForm


def index(request):
    return HttpResponse("Hello, world. You're at the index.")



def new_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            # print()
            transaction= Transaction.objects.create(
                cantidad=form.cleaned_data['cantidad'],
                fecha=form.cleaned_data['fecha'],
                concepto = form.cleaned_data['concepto'],
                tipo=form.cleaned_data['tipo'],
                notas=form.cleaned_data['notas'],
            )
            return redirect('transactions')
    else:
        form = TransactionForm()
    return render(request, 'new_transaction.html', {'form': form})



def transactions(request):
    transactions = Transaction.objects.all()
    total = round(sum([float(i) for i in transactions.values_list('cantidad', flat=True)]))
    return render(request, 'transactions.html', {'transactions':transactions, 'total':total})
