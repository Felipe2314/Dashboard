from django.http import HttpResponse

def index(request):
    return HttpResponse("dashboad/index.html")


from django.shortcuts import render

def index(request):
    return render(request, 'dashboard/index.html')  # ou o nome certo do template
