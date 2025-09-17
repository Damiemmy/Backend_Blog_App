from .models import Profile,Blogs
from rest_framework import serializers
from django.contrib.auth import get_user_model

 
User=get_user_model()
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blogs
        fields=['id','slug','title','image','subtitle','category','author','created_at','modified_at','description']

class BlogDetailedSerialiser(serializers.ModelSerializer):
    detailed_category=serializers.SerializerMethodField()
    class Meta:
        model=Blogs
        fields=['id','title','image','slug','category','created_at','description','detailed_category']
    def get_detailed_category(self,blog):
        blogs=Blogs.objects.filter(category=blog.category).exclude(id=blog.id)
        serializer=BlogSerializer(blogs,many=True)
        return serializer.data
class CategorySerializer(serializers.ModelSerializer):
    farming=serializers.SerializerMethodField()
    government=serializers.SerializerMethodField()
    education=serializers.SerializerMethodField()
    technology=serializers.SerializerMethodField()
    blogs=serializers.SerializerMethodField()
    

    class Meta:
        model=Blogs
        fields=['farming','technology','education','government','blogs']
    def get_farming(self,farm):
        farm=Blogs.objects.filter(category='FARMING')
        serializer=BlogSerializer(farm,many=True)
        return serializer.data
    def get_government(self,government):
        government=Blogs.objects.filter(category='GOVERNMENT')
        serializer=BlogSerializer(government,many=True)
        return serializer.data
    def get_education(self,education):
        education=Blogs.objects.filter(category='EDUCATION')
        serializer=BlogSerializer(education,many=True)
        return serializer.data
    def get_technology(self,technology):
        technology=Blogs.objects.filter(category='TECHNOLOGY')
        serializer=BlogSerializer(technology,many=True)
        return serializer.data
    def get_blogs(self,blog):
        all_blogs=Blogs.objects.all()
        serializer=BlogSerializer(all_blogs,many=True)
        return serializer.data
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'city', 'state', 'address', 'phone', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  # 🔑 Hash the password
        user.save()
        return user
    


    
