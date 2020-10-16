from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login")
    # path("logout", views.logout_view, name="logout")
]
# three different routes
# one index route
# one login route
# one logout route
# all three of these paths need a function
