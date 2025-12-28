from rest_framework import serializers
from .models import users
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined']  
        read_only_fields = ['id', 'date_joined']    