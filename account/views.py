from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,UpdateView
from django.template.loader import render_to_string
from account.models import UserFile
from .forms import loginForm,emailForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect

def show_profile(request,user):
	return render(request,'account/profile.html',{'user':user})

def login_view(request):
    form=loginForm(request.POST or None)
    all_users = UserFile.objects.all()

    # authentication
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        for user in all_users:
            if user.name==username and user.password==password:
                user_s = user
                return show_profile(request,user_s)

    return render(request,'account/invalid.html')

def home(request):
	return render(request,'home.html')
def signup(request):
    if request.method == 'GET':
        return render(request, 'account/signup.html')
    else:

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        last_name = request.POST['re_type_password']
        if password == last_name:

            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                return redirect('signup')
            except IntegrityError:
                return render(request, 'account/signup.html',
                              {'error': 'username has used previously please try with another one'})


def edit_email(request,user_id):
    form=emailForm(request.POST or None)
    
    # update email_address field
    if form.is_valid():
        email_address = form.cleaned_data['email_address']
        user_t = UserFile.objects.get(id=user_id)
        user_t.email_address=email_address
        user_t.save()

    user_t = UserFile.objects.get(id=user_id)
    return show_profile(request,user_t)


# Create your views here.
