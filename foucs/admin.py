from django.contrib import admin
from .models import MyUser, Artical, Comment, Poll, Column, Author
from django.contrib.auth.models import User

# Register your models here.
class MyUserInline(admin.StackedInline):
	model = MyUser
	can_delete = False
	verbose_name_plural = 'myuser'

class UserAdmin(admin.ModelAdmin):
	inlines = (MyUserInline,)
class ArticalAdmin(admin.ModelAdmin):
	list_display =('title','author','pub_date', 'poll_nums')

class CommentAdmin(admin.ModelAdmin):
	list_display =('comment_text', 'artical_id','user_id','poll_nums')

class ColumnAdmin(admin.ModelAdmin):
	list_display =('column',)

class AuthorAdmin(admin.ModelAdmin):
	list_display =('name','email','profile')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Artical, ArticalAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(Author, AuthorAdmin)