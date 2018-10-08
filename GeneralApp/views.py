from django.shortcuts import render,redirect
from .forms import *
from time import clock
from main import views
from GeneralApp import urls
from django.http import HttpResponseRedirect
def GeneralApp(request):
    form = PersonForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form = form.save()
        return redirect(succsess)
    return render(request, 'GeneralApp.html', {'form': form})

def succsess(request):
    return render(request, 'succsess.html')
