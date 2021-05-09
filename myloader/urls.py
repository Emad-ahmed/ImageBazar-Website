from django.urls import path
from myloader.views import HomeView, showcat, SignView, LoginView, user_logout, addphoto

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup', SignView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('showcat/<int:id>/', showcat, name='showcat'),
    path('logout', user_logout, name='logout'),
    path('addphoto', addphoto, name='addphoto'),
]
