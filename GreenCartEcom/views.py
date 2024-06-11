from django.shortcuts import render


def index(request):
    return render(request, 'Dashboard/index.html')

def contact(request):
    return render(request, 'Dashboard/contact.html')
