from django import forms
from .models import Data
from django.forms import ModelForm, TextInput

Meses =(
    ("1", "Январь"),
    ("2", "Февраль"),
    ("3", "Март"),
    ("4", "Апрель"),
    ("5", "Май"),
    ("6", "Июнь"),
    ("7", "Июль"),
    ("8", "Август"),
    ("9", "Сентябрь"),
    ("10", "Октябрь"),
    ("11", "Ноябрь"),
    ("12", "Декабрь"),
)
Days =(
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
    ("13", "13"),
    ("14", "14"),
    ("15", "15"),
    ("16", "16"),
    ("17", "17"),
    ("18", "18"),
    ("19", "19"),
    ("20", "20"),
    ("21", "21"),
    ("22", "22"),
    ("23", "23"),
    ("24", "24"),
    ("25", "25"),
    ("26", "26"),
    ("27", "27"),
    ("28", "28"),
    ("29", "29"),
    ("30", "30"),
    ("31", "31")
)

class DataForm(forms.Form):
    #your_name = forms.CharField(label='Your name', max_length=100)
    # class Meta:
    #     model = Data
    #     fields = ['name', 'birthday', 'city', 'street', 'house']
    #
    #     widgets = {
    #         "name": TextInput(
    #             attrs={'class':'t-input js-tilda-rule ',
    #                    'value': '',
    #                    'placeholder':'Имя',
    #                    'data-tilda-rule':'name',
    #                    'style':'color:#000000; background-color:#ffffff; border-radius: 7px; -moz-border-radius: 7px; -webkit-border-radius: 7px;'}
    #         ),
    #         "birthday":forms.DateInput(
    #             attrs={'class':'t-input t-datepicker js-tilda-rule js-tilda-mask ',
    #                    'value':'',
    #                    'placeholder':'Дата рождения',
    #                    'data-tilda-rule':'date',
    #                    'data-tilda-dateformat':'DD-MM-YYYY',
    #                    'data-tilda-datediv':'dash',
    #                    'data-tilda-mask':'99-99-9999',
    #                    'style':'color:#000000; background-color:#ffffff; border-radius: 7px; -moz-border-radius: 7px; '
    #                            '-webkit-border-radius: 7px;'}
    #         ),
    #         "city":forms.TextInput(
    #             attrs={'class':'t-input js-tilda-rule ',
    #                    'value':'',
    #                    'placeholder':'Населенный пункт',
    #                    'style':'color:#000000; background-color:#ffffff; border-radius: 7px; -moz-border-radius: 7px; '
    #                            '-webkit-border-radius: 7px;'}
    #         ),
    #         "street":forms.TextInput(
    #             attrs={'class':'t-input js-tilda-rule ',
    #                    'value':'',
    #                    'placeholder':'Улица',
    #                    'style':'color:#000000; background-color:#ffffff; border-radius: 7px; -moz-border-radius: 7px; '
    #                            '-webkit-border-radius: 7px;'}
    #         ),
    #         "house":forms.TextInput(
    #             attrs={'class':'t-input js-tilda-rule ',
    #                    'value':'',
    #                    'placeholder':'Дом, Корпус, Квартира',
    #                    'style':'color:#000000; background-color:#ffffff; border-radius: 7px; -moz-border-radius: 7px; '
    #                            '-webkit-border-radius: 7px;'}
    #         )
    #     }

    #name = forms.CharField(max_length=100)

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
            attrs={'class':'t-input t-datepicker js-tilda-rule js-tilda-mask ',
                   'value':'',
                   'placeholder':'Дата рождения',
                   'data-tilda-rule':'date',
                   'data-tilda-dateformat':'DD-MM-YYYY',
                   'data-tilda-datediv':'dash',
                   'data-tilda-mask':'99-99-9999',
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
    


    day = forms.ChoiceField(
        choices=Days,
        widget=forms.Select(
            attrs={'placeholder':'birthday', 'class':'t-select js-tilda-rule ',
                   'style':'color:#000000; background-color:#ffffff; '}
        )
    )

    mes = forms.ChoiceField(
        choices=Meses,
        widget=forms.Select(
            attrs={'placeholder': 'mes', 'class': 't-select js-tilda-rule ',
                   'style': 'color:#000000; background-color:#ffffff; '}
        )
    )
    """








