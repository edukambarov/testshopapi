import datetime

from django import forms

from .models import Order, Client, Good



class GoodForm(forms.Form):
    good_name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(min_value=0, max_digits=12, decimal_places=2)
    quantity = forms.IntegerField(min_value=0)
    add_date = forms.DateField(initial=datetime.date.today,
                                       widget=forms.DateInput(
                                        attrs={'class': 'form-control', 'type': 'date'}
                                        ))
    image = forms.ImageField()



