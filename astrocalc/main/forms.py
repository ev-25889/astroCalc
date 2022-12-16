from django import forms

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

class NameForm(forms.Form):
    #your_name = forms.CharField(label='Your name', max_length=100)
    your_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'name', 'class':'t-input js-tilda-rule ',
                   'style':'color:#000000; background-color:#ffffff; '}
        )
    )

    day = forms.ChoiceField(
        choices=Days,
        widget=forms.Select(
            attrs={'placeholder':'day', 'class':'t-select js-tilda-rule ',
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
widget=forms.TextInput(
                attrs={'placeholder':'day', 'class':'t-select js-tilda-rule ',
                   'style':'color:#000000; background-color:#ffffff; '}
            )
"""




