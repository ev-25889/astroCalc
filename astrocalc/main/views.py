from django.shortcuts import render
from .forms import UserForm


def get_info(request):
    submitbutton = request.POST.get("submit")

    firstname = ''
    lastname = ''
    emailvalue = ''

    form = UserForm(request.POST or None)
    if form.is_valid():
        firstname = form.cleaned_data.get("first_name")
        lastname = form.cleaned_data.get("last_name")
        emailvalue = form.cleaned_data.get("email")

    context = {'form': form, 'firstname': firstname,
               'lastname': lastname, 'submitbutton': submitbutton,
               'emailvalue': emailvalue}

    return render(request, 'main/calc.html', context)
