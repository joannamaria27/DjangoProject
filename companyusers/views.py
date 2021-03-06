from django.shortcuts import render, redirect
from .forms import CompanyRegisterForm
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CompanyRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = CompanyRegisterForm()
    return render(request, 'companyusers/register.html', {'form': form})

def signup(request):
    return render(request,'companyusers/signup.html',{'title':'signup'})


