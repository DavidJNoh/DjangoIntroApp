from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    answer = "placeholder to display a new form to create a new blog"
    return HttpResponse(answer)

def create(request):
    return redirect ('/')

def show(request, number):
    print (number)
    answer= "placeholder to display blog" + number
    return HttpResponse(answer)

def edit(request, number):
    print(number)
    answer= "placeholder to edit blog" + number
    return HttpResponse(answer)

def kill(request):
    return redirect('/')
