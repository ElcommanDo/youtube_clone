from django import forms
class LoginForm(forms.Form):
    username = forms.CharField(max_length=200,label="Username")
    password = forms.CharField(widget=forms.PasswordInput,label='Password')
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=200,label='Username')
    password = forms.CharField(widget=forms.PasswordInput,label="Password")
    f_name = forms.CharField(max_length=200,label='First name')
    l_name = forms.CharField(max_length=200,label='Last name')
    email = forms.EmailField(label='Email',required=True)
class New_video(forms.Form):
    title = forms.CharField(max_length=200,label='title')
    description = forms.CharField(widget=forms.Textarea,label='description')
    video = forms.FileField()
    thumb = forms.ImageField()
class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea,label='Comment')



