from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, reverse

from .models import Data
# from convert import convert_to_num
from .convert import get_num_of_place, get_num_of_birthday, get_main_num

from .forms import DataForm

def about(request):
    return render(request, 'newversion/about.html')

def result(request, main, matrix, num):
    template = 'newversion/res{main}.html'.format(main=main)
    matrix = 'newversion/png/ma' + str(matrix) + '.png'
    num = 'newversion/png/num' + str(num) + '.png'
    return render(request, template, {'matrix':matrix, 'num':num})
def result1(request, matrix, num):
    matrix = 'newversion/png/ma' + str(matrix) + '.png'
    num = 'newversion/png/num' + str(num) + '.png'
    return render(request, 'newversion/res1.html', {'matrix':matrix, 'num':num})

def result2(request, matrix, num):
    matrix = 'newversion/png/ma' + str(matrix) + '.png'
    num = 'newversion/png/num' + str(num) + '.png'
    return render(request, 'newversion/res2.html', {'matrix':matrix, 'num':num})

def result3(request):
    return render(request, 'newversion/res3.html')

def result4(request):
    return render(request, 'newversion/res4.html')

def result5(request):
    return render(request, 'newversion/res5.html')

def result6(request):
    return render(request, 'newversion/res6.html')

def result7(request, matrix, num):
    matrix = 'newversion/png/ma' + str(matrix) + '.png'
    num = 'newversion/png/num' + str(num) + '.png'
    return render(request, 'newversion/res7.html', {'matrix':matrix, 'num':num})

def result8(request, matrix, num):
    matrix = 'newversion/png/ma' + str(matrix) + '.png'
    num = 'newversion/png/num' + str(num) + '.png'
    return render(request, 'newversion/res8.html', {'matrix':matrix, 'num':num})

def result9(request, matrix, num):
    matrix = 'newversion/png/ma' + str(matrix) + '.png'
    num = 'newversion/png/num' + str(num) + '.png'
    return render(request, 'newversion/res9.html', {'matrix':matrix, 'num':num})

def result10(request, matrix, num):
    matrix = 'newversion/png/ma' + str(matrix) + '.png'
    num = 'newversion/png/num' + str(num) + '.png'
    return render(request, 'newversion/res10.html', {'matrix':matrix, 'num':num})

def result11(request, matrix, num):
    matrix = 'newversion/png/ma' + str(matrix) + '.png'
    num = 'newversion/png/num' + str(num) + '.png'
    return render(request, 'newversion/res11.html', {'matrix':matrix, 'num':num})
def result12(request, matrix, num):
    matrix = 'newversion/png/ma' + str(matrix) + '.png'
    num = 'newversion/png/num' + str(num) + '.png'
    return render(request, 'newversion/res12.html', {'matrix':matrix, 'num':num})

def result13(request, matrix, num):
    matrix = 'newversion/png/ma' + str(matrix) + '.png'
    num = 'newversion/png/num' + str(num) + '.png'
    return render(request, 'newversion/res13.html', {'matrix':matrix, 'num':num})

def result14(request, matrix, num):
    matrix = 'newversion/png/ma' + str(matrix) + '.png'
    num = 'newversion/png/num' + str(num) + '.png'
    return render(request, 'newversion/res14.html', {'matrix':matrix, 'num':num})

def result15(request, matrix, num):
    matrix = 'newversion/png/ma' + str(matrix) + '.png'
    num = 'newversion/png/num' + str(num) + '.png'
    return render(request, 'newversion/res15.html', {'matrix':matrix, 'num':num})

def result16(request):
    return render(request, 'newversion/res2.html')

def result17(request):
    return render(request, 'newversion/res3.html')

def result18(request):
    return render(request, 'newversion/res4.html')

def result19(request):
    return render(request, 'newversion/res5.html')

def result20(request):
    return render(request, 'newversion/res6.html')

def result21(request):
    return render(request, 'newversion/res7.html')

def result22(request):
    return render(request, 'newversion/res1.html')




def get_info(request):
    # if this is a POST request we need to process the form data
    submitbutton = request.POST.get("submit")
    #error = ''
    name = ''
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DataForm(request.POST or None)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #form.save()
            name = form.cleaned_data.get("name")
            #birthday = form.cleaned_data.get("birthday")
            #mes = form.cleaned_data.get("mes")
            # return redirect('result')
            #return HttpResponseRedirect('/thanks/')
            data = {
                'form': form,
                # 'error':error,
                'name': name
            }
            return render(request, 'newversion/calc.html', data)
        else:
            error = 'форма неправильно заполнена'
    form = DataForm
    data = {
        'form': form,
        #'error':error,
        'name':name
    }

    return render(request, 'newversion/calc.html', data)


def result_page(request, ):
    submitbutton = request.POST.get("submit")
    name = ''
    birthday = ''

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DataForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            name = form.cleaned_data.get("name")
            birthday = form.cleaned_data.get("birthday")
            #return HttpResponseRedirect('/thanks/')
    context = {'name':name,
               'birthday': birthday
               }
    return render(request, 'newversion/result.html', context=context)

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



