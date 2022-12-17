from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
# from convert import convert_to_num


from .forms import NameForm

def get_info(request):
    # if this is a POST request we need to process the form data
    submitbutton = request.POST.get("submit")

    name = ''
    birthday = ''
    mes = ''
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            name = form.cleaned_data.get("your_name")
            birthday = form.cleaned_data.get("birthday")
            mes = form.cleaned_data.get("mes")
            #return HttpResponseRedirect('/thanks/')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()


    context = {'form': form,
               'birthday': birthday,
               'submitbutton': submitbutton,
               'mes': mes}


    return render(request, 'main/calc.html', context) # , redirect('results')

def result_page(request, id):
    if id == 1:
        return HttpResponse(id)
    if id == 2:
        return HttpResponse(id)

    return render(request, 'main/resultOct.html', {})

