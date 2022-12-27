from django import forms
from .models import Data
from django.forms import ModelForm, TextInput


class DataForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'t-input js-tilda-rule ',
                   'value': '',
                   'placeholder':'Имя',
                   # 'data-tilda-rule':'name',
                   'style':'color:#000000; background-color:#ffffff; border-radius: 7px; -moz-border-radius: 7px; -webkit-border-radius: 7px;'}
        )
    )

    birthday = forms.DateField(
        widget=forms.DateInput(
            attrs={'id':'date',
                   'class':'t-input t-datepicker js-tilda-rule js-tilda-mask ',
                   'value':'',
                   'placeholder':'Дата рождения',
                   'data-tilda-rule':'date',
                   'data-tilda-dateformat':'DD-MM-YYYY',
                   'data-tilda-datediv':'dot',
                   'data-tilda-mask':'99.99.9999',
                   'style':'color:#000000; background-color:#ffffff; border-radius: 7px; -moz-border-radius: 7px; '
                           '-webkit-border-radius: 7px;'}
        )
    )

    city = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'t-input js-tilda-rule ',
                   'value':'',
                   'placeholder':'Населенный пункт',
                   'style':'color:#000000; background-color:#ffffff; border-radius: 7px; -moz-border-radius: 7px; '
                           '-webkit-border-radius: 7px;'}
        )
    )
    """
    street =forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'t-input js-tilda-rule ',
                   'value':'',
                   'placeholder':'Улица',
                   'style':'color:#000000; background-color:#ffffff; border-radius: 7px; -moz-border-radius: 7px; '
                           '-webkit-border-radius: 7px;'}
        )
    )
    house = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'t-input js-tilda-rule ',
                   'value':'',
                   'placeholder':'Дом, Корпус, Квартира',
                   'style':'color:#000000; background-color:#ffffff; border-radius: 7px; -moz-border-radius: 7px; '
                           '-webkit-border-radius: 7px;'}
        )
    )
    """
    
class OSForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={'autocomplete':'email',
                   'name':'Email',
                   'class':'t-input js-tilda-rule ',
                   'value':'',
                   'placeholder':'Your Email',
                   'data-tilda-req':'1',
                   'data-tilda-rule':'email',
                   'style':'color:#000000; border:1px solid #000000; '}
        )
    )

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'autocomplete':'name',
                   'name':'Name',
                   'class':'t-input js-tilda-rule ',
                   'value':'',
                   'placeholder':'Name',
                   'data-tilda-rule':'name',
                   'style':'color:#000000; border:1px solid #000000; '
            }
        )
    )

    tel = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Phone',
                'class': 't-input js-tilda-rule ',
                'style':'color:#000000; border:1px solid #000000; '
            }
        )
    )










