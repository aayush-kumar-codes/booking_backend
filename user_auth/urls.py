from django.urls import path , include
from . import views


urlpatterns = [
    path('register/',views.RegisterView.as_view()),
    path('login/',views.Signin.as_view()),
    path('profile/',views.ProfileView.as_view()),
]