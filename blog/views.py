from django.shortcuts import render
from .models import Post  # Post 모델을 import
from rest_framework import viewsets
from .serializers import PostSerializer


def post_list(request):
    posts = Post.objects.all()  # Post 모델에서 모든 객체들을 가져옴
    return render(request, 'blog/post_list.html', {'posts': posts})  # 'posts' 변수를 포함하여 템플릿에 전달

class IntruderImage(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer