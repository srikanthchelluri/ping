from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from list.models import Ping
from list.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
	return render(request, 'list/index.html')

def login_auth(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/list/home/')
		else:
			return render(request, 'list/login.html', {'failed_message': "that wasn't right - try again."})
	else:
		return render(request, 'list/login.html')
def signup_auth(request):
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			user = authenticate(username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password'])
			login(request, user)
			return HttpResponseRedirect('/list/home/')
	else:
		user_form = UserForm()
	return render(request, 'list/signup.html', {'user_form': user_form})
def logout_auth(request):
	logout(request)
	return HttpResponseRedirect('/list/')

def home(request):
	user = request.user
	ping_list = Ping.objects.filter(owner=request.user).order_by('time')
	sent_list = Ping.objects.filter(requester=request.user).order_by('time')
	return render(request, 'list/home.html', {'user': user, 'ping_list': ping_list, 'sent_list': sent_list})

def send_ping(request):
	if request.method == 'POST':
		ownerInput = request.POST.get('owner')
		description = request.POST.get('description')
		ownerSet = User.objects.filter(username=ownerInput)
		if len(ownerSet) != 1:
			return HttpResponseRedirect('/list/home/')
		owner = ownerSet[0]
		priority = request.POST.get('submit') == "priority"
		ping = Ping(
			requester=request.user,
			owner=owner,
			description=description,
			priority=priority,
		)
		ping.save()
		return HttpResponseRedirect('/list/home/')
	else:
		return HttpResponseRedirect('/list/home/')
def delete_ping(request, ping_slug):
	ping = Ping.objects.filter(slug=ping_slug).delete()
	return HttpResponseRedirect('/list/home/')
