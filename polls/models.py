from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
#一个模型类对应数据库中的一个表，类的实例question代表 表的一个记录，类的属性代表一个字段名
class Question(models.Model):
	question_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date publish')
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		now = timezone.now()
		return now >= self.pub_date >= (now - datetime.timedelta(days=1))
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'
class Choice(models.Model):

	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text