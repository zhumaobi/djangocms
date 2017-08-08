from django.contrib import admin
from .models import Question, Choice

# Register your models here.
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):

	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	#search_fields = ['question']
	fieldsets = [
		(None, 		{'fields' : ['question_text']}),
		('date information', {'fields' : ['pub_date']}),
	]
	inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

#admin.site.register(Choice)