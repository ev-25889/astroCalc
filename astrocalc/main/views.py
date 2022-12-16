from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    submitbutton = request.POST.get("submit")

    firstname = ''
    lastname = ''
    emailvalue = ''
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            name = form.cleaned_data.get("your_name")
            day = form.cleaned_data.get("day")
            mes = form.cleaned_data.get("mes")
            #return HttpResponseRedirect('/thanks/')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()


    context = {'form': form, 'name': name,
                'day': day, 'submitbutton': submitbutton,
             'mes': mes}


    return render(request, 'main/calc.html', context)