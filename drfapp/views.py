from django.shortcuts import render
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from drfapp.serializers import StudentSerializer
from drfapp.models import Student

# Create your views here.
class ListStudentAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
        

class CreateStudentAPIView(CreateAPIView):
    """This endpoint allows for creation of a Student"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UpdateStudentAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific Student by passing in the id of the Student to update"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class DeleteStudentAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Student from the database"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer