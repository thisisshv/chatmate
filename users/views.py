from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == "POST":
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("Yayy, You've been registered"))
            return redirect('login')

    else:
        register_form = RegistrationForm()
    return render(request, 'register.html', {'register_form': register_form})
