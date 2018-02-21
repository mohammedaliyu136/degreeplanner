from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from planner.forms import LoginForm, UserForm, Student_enroll_profile_Form
from planner.models import Profile


def index(request):
    form = LoginForm()
    userForm = UserForm()
    profileForm = Student_enroll_profile_Form()
    context = {'loginForm': form,
               'signupForm': userForm,
               'profileForm': profileForm}
    return render(request, 'accounts/ashraf.html', context)


def login_user(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        userForm = Student_enroll_profile_Form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            id_number = form.cleaned_data['id_number']
            password = form.cleaned_data['password']
            user = authenticate(username=id_number, password=password)
            if user is not None:
                login(request, user)
                check = Profile.objects.all().get(user=request.user)
                if check.is_advisor:
                    return redirect("/advisor/students")
                else:
                    return redirect("/student/plan/edit/")
            else:
                form = LoginForm()
                userForm = UserForm()
                profileForm = Student_enroll_profile_Form()
                context = {'loginForm': form,
                           'signupForm': userForm,
                           'profileForm': profileForm,
                           'errors': 'Login Failed'}
                return render(request, 'accounts/ashraf.html', context)
                # if a GET (or any other method) we'll create a blank form
        else:
            redirect('/account/')


def register2(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        id_number = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=id_number, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/student/enroll_profile")

    context = {
        "form": form,
    }

    return render(request, 'accounts/register.html', {'form': form})


def register(request):
    userForm = UserForm(request.POST or None)
    profileForm = Student_enroll_profile_Form(request.POST or None)
    if userForm.is_valid():
        if profileForm.is_valid():
            user = userForm.save(commit=False)
            id_number = userForm.cleaned_data['id_number']
            password = userForm.cleaned_data['password']
            user.set_password(password)
            user.save()
            profile = profileForm.save(commit=False)
            profile.user = user
            profile.save()
            user = authenticate(username=id_number, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("/student/plan/edit/")

    return HttpResponse("test")


def logout_user(request):
    logout(request)

    return redirect("/account/")


def profile(request):
    return HttpResponse('your profile ')
