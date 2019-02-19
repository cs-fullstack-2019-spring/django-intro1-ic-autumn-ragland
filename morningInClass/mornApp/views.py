from django.http import HttpResponse


def index(request):
    return HttpResponse("This is a bad request. Use one of the other routes")

def lang(request):
    return HttpResponse("JavaScript is my fav language!")

def system(request):
    return HttpResponse("My fav operating system is Windows")

def terminal(request):
    return HttpResponse("I do not like using the terminal to push my projects")
