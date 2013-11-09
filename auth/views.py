from django.contrib.auth.views import login as auth_login_view
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

def login(request):
	newUserForm = UserCreationForm()
	return auth_login_view(request, template_name='auth/login.html', extra_context={"newUserForm": newUserForm})

def logout(request):
        auth_logout(request)
        return redirect('/')

def newUser(request):
	newUserForm = UserCreationForm(request.POST)

	if not newUserForm.is_valid():
		request.method = "GET"
		return auth_login_view(request, template_name='auth/login.html', extra_context={"newUserForm": newUserForm})

	username = newUserForm.clean_username()
	password = newUserForm.clean_password2()
	newUserForm.save()
	user = authenticate(username=username, password=password)
	auth_login(request, user)
	return redirect("/")

