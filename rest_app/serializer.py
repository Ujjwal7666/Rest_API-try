from rest_framework import serializers
from . models import Student

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only =True)
    name = serializers.CharField()
    address = serializers.CharField()
    mobile_number = serializers.CharField()
    roll_no = serializers.IntegerField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.address = validated_data.get("address", instance.address)
        instance.mobile_number = validated_data.get("mobile_number", instance.mobile_number)
        instance.roll_no = validated_data.get("roll_no", instance.roll_no)
        instance.save()
        return instance
    
    # def validate(self, attrs):
    #     return super().validate(attrs)
    def validate_mobile_number(self, mobile_number):
        if len(mobile_number) !=10:
            raise serializers.ValidationError("Mobile number must be 10 digits")

        if self.instance:
            if Student.objects.filter(mobile_number = mobile_number).exclude(id = self.instance.id).exists():
                raise serializers.ValidationError("Mobile Number already exits!")

        else:
            if Student.objects.filter(mobile_number = mobile_number).exists():
                raise serializers.ValidationError("Mobile Number already exits!")
        return mobile_number
    def validate_roll_no(self, roll_no):
        if self.instance:
            if Student.objects.filter(roll_no = roll_no).exclude(id = self.instance.id).exists():
                raise serializers.ValidationError("ROll Number already exits!")

        else:
            if Student.objects.filter(roll_no = roll_no).exists():
                raise serializers.ValidationError("ROll Number already exits!")
        
        return roll_no