from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views.generic.base import View,HttpResponse
from .forms import LoginForm, RegisterForm,New_video,CommentForm
from.models import Comment,Video,User
from django.contrib.auth import login,logout,authenticate
import random,string
# Create your views here.
class Index(View):
    template_name = 'tube/index.html'
    context = {'key','value'}
    def get(self,request):
        #return HttpResponse('This is a GET request')

         most_recent_videos = Video.objects.order_by('-datetime')[:10]
         context = {'most_recent_videos':most_recent_videos}
         return render(request, self.template_name,context)

    def post(self,request):
        return HttpResponse('this is a POST request')
##############################################################



class Login(View):
    template_name = 'tube/login.html'
    def get(self,request):
        form = LoginForm()
        context = {'LoginForm':form}
        return render(request, self.template_name,context)

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
            return HttpResponseRedirect('/')



        return HttpResponse('this is a POST request')



#####################################
class Register(View):
    template_name = 'tube/register.html'
    def get(self,request):
        form = RegisterForm()
        context = {'RegisterForm':form}
        return render(request, self.template_name,context)

    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            f_name = form.cleaned_data['f_name']
            l_name = form.cleaned_data['l_name']
            user = User(username=username,email=email,first_name=f_name,last_name=l_name)
            user.set_password(password)
            user.save()
        return HttpResponseRedirect ('/')
####################################
class new_video(View):
    template_name = 'tube/new_video.html'
    context = {'key','value'}
    def get(self,request):

        if request.user.is_authenticated==False:
            return HttpResponse('you must be logged in in order to upload video')
            #just in case user type path in url and we alse can use login required

        form = New_video()
        context = {'new_video':form}
        return render(request, self.template_name,context)

    def post(self,request):
        form = New_video(request.POST,request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            file = form.cleaned_data['video']
            thumb = form.cleaned_data['thumb']
            random_char = ''.join(random.choices(string.ascii_uppercase + string.digits,k=15))
            #path = random_char +file.name
            video = Video(title=title,description = description,file=file,user=request.user,thumb=thumb)
            video.save()
        else:
            return HttpResponse('your data is not valid please try again ')
        return redirect('index')


class VideoView(View):
    template_name = 'tube/video.html'

    def get(self,request,id):
        video_by_id= Video.objects.get(id=id)
        context = {'video':video_by_id}
        if request.user.is_authenticated:
         comment = CommentForm()
         context['form'] = comment
        all_comments = Comment.objects.filter(video=video_by_id).order_by('-datetime')
        context['comments'] = all_comments
        return render(request,self.template_name,context)
    def post(self,request,id):
        video_by_id= Video.objects.get(id=id)
        comment = CommentForm(request.POST)
        if comment.is_valid():
            content = comment.cleaned_data['content']
            new_comment = Comment(content = content,user=request.user,video=video_by_id)
            new_comment.save()
        return HttpResponseRedirect('/video/'+str(id)+'/')



##########################################################3
class logoutView(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect('/')

