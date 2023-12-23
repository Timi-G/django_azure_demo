from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from college_placement_system.models import User,Student,HOD,Job,Company,JobApplication

# form for registering to website


class UserForm(AuthenticationForm):
    ROLE_CHOICES = [
        ('select role', 'Select Role'),
        ('admin', 'Admin'),
        ('hod', 'HOD'),
        ('student', 'Student'),
        ('company', 'Company')
    ]

    password = forms.CharField(widget=forms.PasswordInput, max_length=50)
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ("username", "password", "role")

    # def save(self, commit=True):
    #     user = super(UserForm, self).save(commit=False)
    #     user.user_id = self.cleaned_data['user_id']
    #     user.password = self.cleaned_data['password']
    #     user.role = self.cleaned_data['role']
    #     if commit:
    #         user.save()
    #     return user

class StudentForm(ModelForm):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    # student_name = forms.CharField(max_length=100, required=True)
    # address = forms.CharField(max_length=400, required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    # email_id = forms.EmailField(required=True)
    # date_of_birth = forms.DateField(widget=forms.DateInput(format='%m-%Y-%d'))
    # phone = forms.IntegerField(required=True)
    # branch = forms.CharField(max_length=200, required=True)
    # password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Student
        fields = ('name', 'address','gender','email','date_of_birth','phone','image','branch','password')

    # save function will be called on successful registration
    def save(self,commit=True):
        user = super(StudentForm, self).save(commit=False)
        user.user = self.cleaned_data['user']
        user.name = self.cleaned_data['name']
        user.address = self.cleaned_data['address']
        user.gender = self.cleaned_data['gender']
        user.email = self.cleaned_data['email']
        user.date_of_birth = self.cleaned_data['date_of_birth']
        user.phone = self.cleaned_data['phone']
        user.image = self.cleaned_data['image']
        user.branch = self.cleaned_data['branch']
        user.password = self.cleaned_data['password']
        if commit:
            user.save()
        return user

class HODForm(ModelForm):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)

    class Meta:
        model = HOD
        fields = ('name', 'address','gender','email','department','phone','password')

    # save function will be called on successful registration
    def save(self,commit=True):
        user = super(HODForm, self).save(commit=False)
        user.user = self.cleaned_data['user']
        user.name = self.cleaned_data['name']
        user.address = self.cleaned_data['address']
        user.gender = self.cleaned_data['gender']
        user.email = self.cleaned_data['email']
        user.department = self.cleaned_data['department']
        user.phone = self.cleaned_data['phone']
        user.password = self.cleaned_data['password']
        if commit:
            user.save()
        return user

class CompanyForm(ModelForm):

    class Meta:
        model = Company
        fields = ('name', 'address','website','email')

    # save function will be called on successful registration
    def save(self,commit=True):
        user = super(CompanyForm, self).save(commit=False)
        user.user = self.cleaned_data['user']
        user.name = self.cleaned_data['name']
        user.address = self.cleaned_data['address']
        user.website = self.cleaned_data['website']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class JobForm(ModelForm):

    class Meta:
        model = Job
        fields = ('name', 'designation', 'twelfth_percentage','gpa','salary')

    # save function will be called on successful registration
    def save(self, commit=True):
        user = super(JobForm, self).save(commit=False)
        user.name = self.cleaned_data['name']
        user.designation = self.cleaned_data['designation']
        user.twelfth_percentage = self.cleaned_data['twelfth_percentage']
        user.gpa = self.cleaned_data['gpa']
        user.salary = self.cleaned_data['salary']
        if commit:
            user.save()
        return user


class JobApplicationForm(ModelForm):
    class Meta:
        model = JobApplication
        fields = ('designation', 'description','experience','twelfth_percentage', 'gpa')

    # save function will be called on successful registration
    def save(self, commit=True):
        user = super(JobApplicationForm, self).save(commit=False)
        user.designation = self.cleaned_data['designation']
        user.description = self.cleaned_data['description']
        user.experience = self.cleaned_data['experience']
        user.twelfth_percentage = self.cleaned_data['twelfth_percentage']
        user.gpa = self.cleaned_data['gpa']
        if commit:
            user.save()
        return user