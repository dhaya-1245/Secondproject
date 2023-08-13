from django.http import HttpResponse


def evenodd_fun(request):
    x=[20,11,17,16]
    y=[i for i in x if i%2==0]
    return HttpResponse(f'even numbers are {y}')
