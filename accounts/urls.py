from django.urls import path

from .views import home_view, register_view, logout_view, login_view

app_name = 'account'
urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
]
