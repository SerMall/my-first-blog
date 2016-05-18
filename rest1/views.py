from django.shortcuts import render

# Create your views here.

#	http://www.django-rest-framework.org/tutorial/quickstart/
#	"Views"


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest1.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    API кінцевих точок, що дозволяє користувачам переглядати або редагувати
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    API кінцевих точок, що дозволяє групам переглядати або редагувати.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



