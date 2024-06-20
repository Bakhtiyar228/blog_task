from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.http import JsonResponse

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            return JsonResponse({'error': 'Passwords do not match'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username is already taken'}, status=400)
        new_user = User.objects.create_user(username=username, password=password1)
        new_user.save()
        return JsonResponse({'message': 'User registered successfully!'})
    else:
        return render(request, 'registration_form.html')