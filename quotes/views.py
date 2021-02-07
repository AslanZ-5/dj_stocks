from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        ticker = request.POST['ticker_symbol']
        import requests
        import json
        api_request = requests.get(
            "https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_3e3c4cff7a7c4df684e55115360ea253")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "It doesn't work...."

        return render(request, 'quotes/home.html', {"api": api})
    else:
        return render(request, 'quotes/home.html', {"ticker": "Enter a Ticker Symbole Above..."})


def about(request):
    return render(request, 'quotes/about.html')


def add_stock(request):
    import requests
    import json
    ticker = Stock.objects.all()
    api_items = []
    for ticker_item in ticker:
        api_request = requests.get(
            "https://cloud.iexapis.com/stable/stock/" + str(
                ticker_item) + "/quote?token=pk_3e3c4cff7a7c4df684e55115360ea253")
        try:
            api = json.loads(api_request.content)
            api_items.append(api)
        except Exception as e:
            api = "It doesn't work...."
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Stock has been added successfully')
            return redirect('quotes:add_stock')
    else:
        form = StockForm()
    tt = {
        "ticker": ticker,
        "form": form,
        "api": api_items
    }

    return render(request, 'quotes/add_stock.html', tt)


def delStock(request, pk):
    item = Stock.objects.get(pk=pk)
    item.delete()
    messages.success(request, 'Stock Has been Delete')
    return redirect('quotes:delete_stock')


def delete_stock(request):
    ticker = Stock.objects.all()
    return render(request, 'quotes/delete_stock.html',{'ticker':ticker})

