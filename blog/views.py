from django.shortcuts import render
from django.utils import timezone
from .models import Post

#added, 20220607
from rest_framework import viewsets
from .serializers import PostSerializer

class IntruderImage(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer    

    
def post_list(request):
    posts = Post.objects.order_by('-created_date')
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

