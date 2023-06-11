from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    ##
=======
>>>>>>> parent of 293c1e2 (Revert)
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),
]