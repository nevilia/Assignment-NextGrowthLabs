from rest_framework import serializers  
from .models import *

class AndriodAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = AndroidApp
        fields = '__all__'
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'