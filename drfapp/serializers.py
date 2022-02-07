from rest_framework import serializers
from .models import Student, students

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'name','age',
        )