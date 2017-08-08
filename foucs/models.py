from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MyUser(models.Model):
	user = models.OneToOneField(User)
	profile = models.TextField('profile')

class Artical(models.Model):
	title = models.CharField(max_length=256)
	author = models.ForeignKey('Author')
	content = models.TextField('content', blank=True)
	poll_nums = models.IntegerField(default=0)
	comment_nums = models.IntegerField(default=0)
	keep_nums = models.IntegerField(default=0)
	user = models.ManyToManyField('MyUser', blank=True)
	pub_date = models.DateTimeField(auto_now_add=True)
	latest_pub_date = models.DateTimeField(auto_now=True)
	column = models.ForeignKey('Column')

	def __str__(self):
		return self.title

class Column(models.Model):
	column = models.CharField(max_length=256, blank=True)
	def __str__(self):
		return self.column

class Author(models.Model):
	name = models.CharField(max_length=256)
	email = models.EmailField('email')
	password = models.CharField('password', max_length=256)
	register_date = models.DateTimeField(auto_now_add=True)
	profile = models.CharField('profile',max_length=256)

	def __str__(self):
		return self.name

class Comment(models.Model):
	comment_text = models.TextField('comment_text')
	user = models.ForeignKey(MyUser)
	artical = models.ForeignKey(Artical)
	poll_nums = models.IntegerField(default=0)
	pub_date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.coment_text

class Poll(models.Model):
	user = models.ForeignKey(MyUser)
	artical = models.ForeignKey(Artical)
	comment = models.ForeignKey(Comment)
