from django.forms import models
from .models import Stock


class StockForm(models.ModelForm):
    class Meta:
        model = Stock
        fields = ['ticker']
