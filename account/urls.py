from django.urls import path
from .views import register,update,profile

app_name = 'account'

urlpatterns = [
    path('register/', register, name = 'register' ),
    path('update/', update, name = 'update'),
    path('profile', profile, name = 'profile')
]