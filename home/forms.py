from django import forms
from django.core.exceptions import ValidationError

from .models import PayModel


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, label='Имя',
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, label='Фамилия',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    email_address = forms.EmailField(max_length=150, label='E-mail',
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(max_length=2000, label='Сообщение',
                              widget=forms.Textarea(attrs={'class': 'form-control'}))


class PayForm(forms.ModelForm):
    class Meta:
        model = PayModel
        fields = ['first_name', 'second_name', 'adres', 'phone', 'product_id', 'user']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'second_name': forms.TextInput(attrs={'class': 'form-control'}),
            'adres': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'product_id': forms.HiddenInput(),
            'user': forms.HiddenInput(),

        }

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(str(phone)) > 11:
            raise ValidationError(
                'Номер не может быть больше 11 символов, вводите номер без спец знаков, без пробелов и без плюса в начале')
        return phone
