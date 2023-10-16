from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    just_text="Hello Universe!"
    return render(request,"food/index.html",context=None)