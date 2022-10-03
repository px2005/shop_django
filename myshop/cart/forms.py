from django import forms

# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    # quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control text-center',
            'type': 'number',
            'value': '1',
        })
    )
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)