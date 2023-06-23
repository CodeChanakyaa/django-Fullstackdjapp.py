from django.shortcuts import render
from .serializers import *
from.models import *
from rest_framework.mixins import *
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView

# Blog View Functions
class Blog_API_L(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class Blog_API_R(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


# Comment View Functions
class Comment_API_CL(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class Comment_API_RUD(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# Contact View Functions
class Contact_API_C(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer