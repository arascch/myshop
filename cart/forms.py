from django import forms
from flask import flash

PRODUCT_QUANTITY_CHOICES = [(i , str(i)) for i in range(1,21)]

class CartAddProdictForm(forms.Form):
    quantity = forms.TypedChoiceField(choices= PRODUCT_QUANTITY_CHOICES , coerce=int)
    override = forms.BooleanField(required=False , initial=False , widget=forms.HiddenInput)