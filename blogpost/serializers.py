from django.core.urlresolvers import reverse  
from rest_framework import serializers 
from blogpost.models import Blogpost, Comment 

class BlogpostSerializer(serializers.HyperlinkedModelSerializer): 
    comments = serializers.HyperlinkedModelSerializer(many=True)
  
    class Meta:
        model = Blogpost  
        fields = ('id', 'created', 'title', 'content', 'url', 'comments',) 
        ordering = ('-created',)  #
        
    def comments(self, instance):  #
        return reverse('comments', kwargs={'blogpost':instance.id})  #

 
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment  
        fields = ('id', 'created', 'comment', 'url', 'blogpost',)
        ordering = ('-created',)  #
  
    def blogpost(self, instance):  #
        return reverse('blogpost', kwargs={'id':instance.blogpost.id})  #

