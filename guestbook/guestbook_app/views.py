from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import UserRegisterForm, MessageForm
from .models import Guestbookentry
# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect("guestbook")
        
    else:
        form = UserCreationForm()
    return render(request,'guestbook_app/register.html',{"form":form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('guestbook')
    else:
        form = AuthenticationForm()
    return render(request,'guestbook_app/login.html',{'form':form})

def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def guestbook(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            return redirect('guestbook')
    else:
        form = MessageForm()
        
    message_list = Guestbookentry.objects.all().order_by('-create_at')
    paginator = Paginator(message_list, 10)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'guestbook_app/guestbook.html',{'form':form, 'page_obj':page_obj})
