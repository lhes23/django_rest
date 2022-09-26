from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view

from post_api.models import Post
from post_api.serializers import PostSerializer

# Create your views here.
@api_view(['GET'])
def getAllPosts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse({'posts': serializer.data})