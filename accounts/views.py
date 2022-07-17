from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout 
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from store.models import Customer

# Create your views here.

# ........ user registration and login handling  codes ........#
def register(request):
	if request.method == "POST":
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			Customer.objects.create(
				user = user,
				name = user.first_name + user.last_name,
				email = user.email,
				)
			return redirect('login')
	else:
		form = UserRegistrationForm()
	return render(request, 'accounts/register.html' , {'form':form})

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data= request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)

			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			else:
				return redirect('store')

	else:
		form = AuthenticationForm()
   
	return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
	if request.method == 'GET':
		logout(request)
		return render(request, 'accounts/logout.html')


def profile(request):
	return render(request, 'accounts/profile.html')

	
        
        
    