from django import forms
from django.core.validators import MinLengthValidator, RegexValidator

class NumberForm(forms.Form):
    # digit_zero = forms.IntegerField(max_value=9, min_value=0, label='')
    # digit_one = forms.IntegerField(max_value=9, min_value=0, label='')
    # digit_two = forms.IntegerField(max_value=9, min_value=0, label='')
    # digit_three = forms.IntegerField(max_value=9, min_value=0, label='')
    digits_input = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'class': 'digit', 'maxlength': '4', 'minlength': '4', 'autocomplete': 'off'}),
            validators=[RegexValidator(regex=r'^(?!.*(.).*\1)\d{4}$')]
        )
