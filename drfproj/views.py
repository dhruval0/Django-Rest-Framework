import imp
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from drfapp.serializers import StudentSerializer
from drfapp.models import Student
