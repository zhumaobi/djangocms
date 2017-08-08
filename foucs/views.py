from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, LogupForm
from .models import User, Artical
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
	artical_latest = Artical.objects.order_by('pub_date')[:3]
	if request.method == 'POST':
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return render(request, 'index.html')
			else:
				render(request,'index.html',{'login_form': login_form,
											'artical_latest': artical_latest,
											})
	else:
		login_form = LoginForm()

	context = {'login_form' : login_form, 'artical_latest': artical_latest}
	return render(request,'index.html', context)

def artical_detail(request, artical_id):
	try:
		artical = Artical.objects.get(pk=artical_id)
	except Artical.DoesNotExit:
		raise 



def log_up(request):
	if request.method == 'POST':
		logup_form = LogupForm(request.POST)
		if logup_form.is_valid():
			email = logup_form.cleaned_data['email']
			username = logup_form.cleaned_data['username']
			password = logup_form.cleaned_data['password']
			if not User.objects.filter(email = email):
				user = User(username=username, password=password, email=email)
				user.save()
				return render_to_response('logup_succeed.html',{'username': user.username})
			else:
				render(request, 'log_up.html', {'logup_form': logup_form})
	else:
		logup_form = LogupForm()
	
	context = {'logup_form': logup_form}
	return render(request, 'log_up.html', context)

#logout即使用户未登陆也不会报错
def log_out(request):
	logout(request)
	url = request.POST.get('source_url', '/foucs/')
	return HttpResponseRedirect(url)


