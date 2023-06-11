from django.urls import path
from . import views

urlpatterns = [
    #KSG comment added
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),
]