from django import forms

# Create your form here.
class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'type':'text', 'class':'form-control', 'id':'uid', 'name':'uid', 'placeholder':'您的大名'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'type':'password', 'class':'form-control', 'id':'pwd', 'name':'pwd', 'placeholder':'看不见的密码'}))

class LogupForm(forms.Form):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'type':'email', 'class':'form-control', 'id':'email', 'name':'email', 'placeholder':'随便输个邮箱地址哦～'}))
	username = forms.CharField(widget=forms.TextInput(attrs={'type':'text', 'class':'form-control', 'id':'uid', 'name':'uid', 'placeholder':'随便起个名字！'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'type':'password', 'class':'form-control', 'id':'pwd', 'name':'pwd', 'placeholder':'密码的话随意啦！'}))