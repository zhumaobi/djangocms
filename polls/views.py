from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
# Create your views here.
"""存在冗余代码的视图函数
def index(request):
	#依据字段'pub_date'对所有Question对象进行排序，并选取前三个
	latest_question_list = Question.objects.order_by('-pub_date')[:3]
	context = {
        'latest_question_list': latest_question_list,
        }
    #快捷函数render(request, 'app/xxxx.html', context)，其中context必须为字典
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request,'polls/results.html', {'question': question})
"""
""" 经过改良的视图函数"""

class IndexView(generic.ListView):
	model = Question
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'
	#重载get_queryset(self)函数
	def get_queryset(self):
		now = timezone.now()
		return Question.objects.filter(pub_date__lte=now).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

def vote(request, question_id):
	#快捷函数get_objiect_or_404，第一个参数为models类，第二个参数为主键值
	q = get_object_or_404(Question, pk=question_id)
	try:
		#request.POST['choice']从POST表单中获取name=choice的输入的值, choice = ("value=")choice.id
		#同时始终返回一个字符串, q.choice_set是模型Choice设置了将Question作为外健由django生成的一个集合，
		#名字为modelnamelower_set,它可以供Question的对象调用，比如question.choice_set.all()返回一个可迭代的choice迭代器
		selected_choice = q.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
				'question' : q,
				'erro_message' : "You didn't select a choice!",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		#为防止用户双击投票的操作，在投票完成后，将url重定向到polls/#q.id/results
		return HttpResponseRedirect(reverse('polls:results', args=(q.id,)))