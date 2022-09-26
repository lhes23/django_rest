from django.urls import path, include
from .views import *

urlpatterns = [
    path('',getAllPosts, name='allPosts'),
    path('<int:id>/',getSinglePost, name='singlePost')
]