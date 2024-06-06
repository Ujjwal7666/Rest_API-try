from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework import serializers

from user import global_function


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    username = serializers.CharField(error_messages={"required":"Usename must be written"})
    password = serializers.CharField(write_only = True, error_messages={"required":"password must be written"})
    email = serializers.EmailField(error_messages={"required":"Enail must be written"})
    first_name = serializers.CharField(error_messages={"required":"first name must be written"})
    last_name = serializers.CharField(error_messages={"required":"last name must be written"})

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.password = make_password(validated_data.get("password")) if validated_data.get("password") else  instance.password 
        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.save()
        return instance

    def validate_password(self, password):
        is_password = global_function.password_validation(password)
        if not is_password:
            raise serializers.ValidationError("Password must be contain 8 digiti length.")
       