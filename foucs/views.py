from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect,Http404
from .forms import LoginForm, LogupForm, CommentForm
from .models import MyUser, Artical, Comment, Poll
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from urllib.parse import urljoin
import markdown2
# Create your views here.

def index(request):
	artical_latest = Artical.objects.filter(column__column='新闻').order_by('-pub_date')[:3]
	if request.method == 'POST':
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				render(request, 'index.html', { 'login_form': login_form,
												'artical_latest': artical_latest,
											})
			else:
				render(request, 'index.html', { 'login_form': login_form,
												'artical_latest': artical_latest,
											})
	else:
		login_form = LoginForm()

	context = { 'login_form' : login_form, 'artical_latest': artical_latest }
	return render(request,'index.html', context)

def log_in(request):
	if request.method == 'POST':
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				url = request.POST.get('source_url', '/foucs/')
				return redirect(url)
			else:
				render(request, 'log_in.html', { 'login_form': login_form})
	else:
		login_form = LoginForm()
	return render(request,'log_in.html',{'login_form': login_form})

def artical_detail(request, artical_id):
	try:
		artical = Artical.objects.get(pk=artical_id)
	except Artical.DoesNotExit:
		raise Http404('Artical does not exit!')
	content = markdown2.markdown(artical.content, extras=["code-friendly", "fenced-code-blocks", "header-ids", "toc", "metadata"])
	comments = Comment.objects.filter(artical=artical_id)
	comment_form = CommentForm()

	if request.method == 'POST':
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				render(request, 'artical_detail.html', {'artical': artical,
														'content': content,
														'comments': comments,
														'comment_form': comment_form,
														'login_form': login_form,
														})
			else:
				render(request, 'artical_detail.html', { 'login_form': login_form,
														'artical': artical,
														'content': content,
														'comments': comments,
														'comment_form': comment_form,
											})
	else:
		login_form = LoginForm()
	context = { 'artical': artical,
				'content': content,
				'comments': comments,
				'comment_form': comment_form,
				'login_form': login_form,
	}
	return render(request,'artical_detail.html',context)


@login_required(login_url='/foucs/log_in')
def comment(request, artical_id):
	comment_form = CommentForm(request.POST)
	if comment_form.is_valid():
		user = request.user
		artical = Artical.objects.get(pk=artical_id)
		new_comment = comment_form.cleaned_data['content']
		artical.comment_nums += 1
		comment_a = Comment(comment_text=new_comment, artical = artical, user=user)
		comment_a.save()
	url = urljoin('/foucs/artical/', artical_id)
	return redirect(url)

@login_required(login_url='/foucs/log_in')
def poll_artical_indetail(request, artical_id):
	logged_user = request.user
	artical = Artical.objects.get(pk=artical_id)
	articals = []
	polls = logged_user.poll_set.all()
	url = urljoin('/foucs/artical/', artical_id)
	for poll in polls:
		articals.append(poll.artical)
	if artical in articals:
		return redirect(url)
	else:
		artical.poll_nums += 1
		artical.save()
		poll_a = Poll(user=logged_user, artical=artical)
		poll_a.save()
		return redirect(url)

def log_up(request):
	if request.method == 'POST':
		logup_form = LogupForm(request.POST)
		if logup_form.is_valid():
			email = logup_form.cleaned_data['email']
			username = request.POST['username']
			password = request.POST['password']
			if not User.objects.filter(email = email):
				user = User.objects.create_user(username=username, password=password, email=email)
				user.save()
				return render_to_response('logup_succeed.html',{'username': user.username})
			else:
				render(request, 'log_up.html', {'logup_form': logup_form})
	else:
		logup_form = LogupForm()
	
	context = {'logup_form': logup_form}
	return render(request, 'log_up.html', context)

#登出，即使用户未登陆也不会报错
@login_required
def log_out(request):
	logout(request)
	url = request.POST.get('source_url', '/foucs/')
	return HttpResponseRedirect(url)


