from django.shortcuts import render

# Create your views here.

from blogpost.models import Blogpost, Comment
from blogpost.serializers import BlogpostSerializer, CommentSerializer
from rest_framework import viewsets

from rest_framework import  permissions

class BlogpostViewSet(viewsets.ModelViewSet):

    serializer_class = BlogpostSerializer
    queryset = Blogpost.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]


class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

