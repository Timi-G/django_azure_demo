# college_placement_system/urls

# from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'college_placement_system'

urlpatterns = [
    path('', views.login_request, name='login'),
    path('<user_role>', views.registration, name='user_home')
]
