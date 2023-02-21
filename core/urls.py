from django.urls import path
from .views import home, post_detail_view,CreatePost

app_name = 'core'

urlpatterns = [
    path('', home , name ='home'),
    path('detail/<int:id>', post_detail_view, name = 'detail'),
    path('create-post/', CreatePost.as_view(), name = 'create-post')
]