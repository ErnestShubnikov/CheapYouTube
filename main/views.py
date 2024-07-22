from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from .models import Video, CustomUser
from .forms import UploadForm, RegForm, LoginForm

def register(request):
	if request.method == 'POST':
		form = RegForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.set_psw(form.cleaned_data['password1'])
			user.save()
			return redirect('login')
	else:
			form = RegForm()
	return render(request,'main/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid(): 
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = CustomUser.objects.filter(email=email).first()
            if user and user.check_psw(password):
                request.session['user_id'] = user.id
                return redirect('home')
            else:
                form.add_error(None, 'Invalid email or password.')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})
		
def logout(request):
	request.session.flush()
	return redirect('home')

def index(request):
	videos  = Video.objects.all()
	return render(request, 'main/index.html', {'videos': videos})

def upload(request):
	if request.method == "POST":
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			title = form.cleaned_data['title']
			photo = form.cleaned_data['photo']
			video = form.cleaned_data['video']
			user = CustomUser.objects.get(id=request.session['user_id'])

			upload_inst = Video(title = title, preview=photo, video=video, uploader = user)
			upload_inst.save()

			return redirect('/')


	else: 
		form = UploadForm()
	return render(request, 'main/upload.html',{'form': form})




def video(request, id=None):
	article  = get_object_or_404(Video, id=id)
	article.views += 1
	article.save()
	user = article.uploader
	username = user.username
	user_id = user.id
	user_video_count = Video.objects.filter(uploader=user).count()
	return render(request, 'main/video.html', {'article': article, 'username':username, 'user_video_count': user_video_count, 'user_id':user_id})


def author(request, id=None):
	user = get_object_or_404(CustomUser, id=id)
	username = user.username
	author_videos = Video.objects.filter(uploader=user)
	return render(request, 'main/author.html', {'videos': author_videos, 'username':username})