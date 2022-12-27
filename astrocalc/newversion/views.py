from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, reverse

from django.core.mail import send_mail, BadHeaderError

from .models import Data
# from convert import convert_to_num
from .convert import get_num_of_place, get_num_of_birthday, get_main_num

from .forms import DataForm, OSForm

def about(request):
    return render(request, 'newversion/about.html')

def result(request, main, matrix, num):
    template = 'newversion/res{main}.html'.format(main=main)
    matrix = 'newversion/png/ma' + str(matrix) + '.png'
    num = 'newversion/png/num' + str(num) + '.png'

    submitbutton = request.POST.get("submit")

    form = OSForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        tel = form.cleaned_data.get("tel")
        context = {'form': form, 'submitbutton': submitbutton,
                   'name': name, 'email':email, 'tel':tel}


        return render(request, 'newversion/calc.html', context=context)
    return render(request, template, {'matrix':matrix, 'num':num, 'form': form})




def get_info2(request):
    submitbutton = request.POST.get("submit")

    name = ''
    #lastname = ''
    #emailvalue = ''

    form = DataForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")
        birthday = form.cleaned_data.get("birthday")
        city = form.cleaned_data.get("city")
        context = {'form': form, 'submitbutton': submitbutton,
                   'name': name}
        for i in city:
            if i.lower() not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
                context = {'form': form, 'submitbutton': submitbutton,
                           'name': name, 'error': 'введен неправильный город'}
                return render(request, 'newversion/calc.html', context=context)


        #lastname = form.cleaned_data.get("last_name")
        #emailvalue = form.cleaned_data.get("email")

        num_of_city = get_num_of_place(city)
        num_of_birthday = get_num_of_birthday(birthday)
        main_num = get_main_num(city, birthday)
        #matrix =  'newversion/png/ma' + str(num_of_birthday) + '.png'
        #num = 'newversion/png/num' + str(num_of_city) + '.png'
        #context = {'matrix':matrix, 'num':num}

               #'lastname': lastname, ,
               #'emailvalue': emailvalue}
        #url = 'result/' + str(num_of_name)
        # return redirect(url, name)
        # url = 'result/{page}'.format(page=main_num) + '/?matrix="' + matrix + '"&num="' + num + '"'
        url = 'result/{page}/{matrix}/{num}'.format(page=main_num, matrix=num_of_birthday, num=num_of_city)
        template = 'newversion/res' + str(main_num) + '.html'
        # return render(request, template, context=context)
        return redirect(url)
        #return redirect(url, {'matrix':matrix})

    num_of_name = get_num_of_place(name)
    context = {'form': form, 'num_of_name': num_of_name, 'submitbutton': submitbutton,
               'name': name}

    return render(request, 'newversion/calc.html', context=context)


