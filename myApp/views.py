from django.shortcuts import render
from django.shortcuts import render

from django.contrib.auth import logout
from django.shortcuts import redirect

from django.contrib.auth.forms import UserCreationForm
from myapp.forms import RegisterForm
from restaccount.models import DriverUser


def register(request):
    if request.user.is_authenticated:
        return redirect('myapp:logout')
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('myprofile:list')
        else:
            form = RegisterForm()

            args = {'form': form}
            return render(request, 'myapp/register.html', args)



