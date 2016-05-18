from django.shortcuts import render

# Create your views here.

"""
from blogpost.models import BlogPost, Comment
from rest_framework.views import APIView
from blogpost.serializers import BlogPostSerializer, CommentSerializer


class BlogPostViewSet(APIView):
    
#    API endpoint that allows users to be viewed or edited.
#    API кінцевих точок, що дозволяє користувачам переглядати або редагувати
    
    queryset = BlogPost.objects.all().order_by('-date_joined')
    serializer_class = BlogPostSerializer


class CommentViewSet(APIView):
    
#    API endpoint that allows groups to be viewed or edited.
#    API кінцевих точок, що дозволяє групам переглядати або редагувати.
    
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
"""
#	http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset:
#from django.contrib.auth.models import User
from blogpost.models import Blogpost, Comment
#from blogpost.models import User, Blogpost, Comment

#from django.shortcuts import get_object_or_404
#from myapps.serializers import UserSerializer
from blogpost.serializers import BlogpostSerializer, CommentSerializer
#from blogpost.serializers import UserSerializer, BlogpostSerializer, CommentSerializer

from rest_framework import viewsets
#from rest_framework.response import Response

from django.views.generic.base import TemplateView
class RootView(TemplateView):
    template_name = "base.html"


"""
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
"""



class BlogpostViewSet(viewsets.ModelViewSet):
    serializer_class = BlogpostSerializer
    queryset = Blogpost.objects.all()
    """
    A simple ViewSet for listing or retrieving users.
    
    def list(self, request):
        queryset = Blogpost.objects.all()
        serializer = BlogpostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Blogpost.objects.all()
        blogpost = get_object_or_404(queryset, pk=pk)
        serializer = BlogpostSerializer(blogpost)
        return Response(serializer.data)
"""

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    """
    A simple ViewSet for listing or retrieving users.
    
    def list(self, request):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Comment.objects.all()
        comment = get_object_or_404(queryset, pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
"""

#blogpost_list = BlogPostViewSet.as_view({'get': 'list'})
#blogpost_detail = BlogPostViewSet.as_view({'get': 'retrieve'})

