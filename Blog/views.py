from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Blogs,Profile
from .serializers import BlogSerializer,BlogDetailedSerialiser,CategorySerializer,RegisterSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status


# Create your views here.

@api_view(['GET'])
def MYBlogs(request):
    blogs=Blogs.objects.all()
    serializer=BlogSerializer(blogs,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Blogpage(request,slug):
    blogs=Blogs.objects.get(slug=slug)
    serializer=BlogDetailedSerialiser(blogs)
    return Response(serializer.data)

@api_view(['GET'])
def Getcategory(request):
    blogs=Blogs.objects.all()
    serializer=CategorySerializer(blogs)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetCurrentUser(request):
    user = request.user
    return Response({
        "username": user.username,
       
    })
@api_view(['POST'])
@permission_classes([AllowAny])  # Anyone should be able to register
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
