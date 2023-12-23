from django.shortcuts import render, redirect
from .forms import UserForm, StudentForm, HODForm, CompanyForm, JobForm, JobApplicationForm
from .models import Student
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

forms_dict = {'user':UserForm, 'student':StudentForm, 'hod':HODForm, 'company':CompanyForm}

# Create your views here.
def login_request(request):
	if request.method == "POST":
		form = UserForm(request, data=request.POST)
		if form.is_valid():
			user_id = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			role = form.cleaned_data.get('role')
			user = authenticate(username=user_id, password=password, role=role)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {user_id}.")
				return redirect('college_placement_system:user_home',user_role=form.role)
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = UserForm()
	return render(request=request, template_name="college_placement_sys\login.html", context={"login_form":form})

@login_required(login_url="")
def registration(request,user_role):
	form_ = forms_dict[f'{user_role}']
	if request.method == "POST":
		form = form_(request, data=request.POST)
		if form.is_valid():
			# if form_type == 'student'
			# 	image  = form.cleaned_data.get('image')
			user = form.save()
			if user is not None:
				# login(request, user)
				messages.info(request, f"You have successfully registered {user}.")
				# return redirect("main:homepage")
			else:
				messages.error(request,"Invalid registration")
		else:
			messages.error(request,"Invalid username or password.")
	form = form_()
	return render(request=request, template_name="college_placement_sys\login.html", context={"login_form":form})