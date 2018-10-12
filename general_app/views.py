from django.shortcuts import render,redirect
from .forms import PersonForm


def general_app(request):
    form = PersonForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form = form.save()
        return redirect(success)
    return render(request, 'general_app.html', {'form': form})


def success(request):
    return render(request, 'success.html')
