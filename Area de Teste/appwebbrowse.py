from django.shortcuts import render


def hello(request):
    context = {'name': 'John'}
    return render(request, 'hello.html', context)
