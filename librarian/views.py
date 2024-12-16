from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import*
from librarian.serializers import*
# Create your views here.

class StudentListCreateView(APIView):
    """
    Handles listing all students and creating a new student.
    """

    def get(self, request, *args, **kwargs):
        # Query all student records
        students = Student.objects.all()
        # Serialize the data
        serializer = StudentSerializer(students, many=True)
        # Return serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)

class LibraryHistoryListCreateView(APIView):
    """
    Handles listing all library records and creating a new library record.
    """

    def get(self, request, *args, **kwargs):
        library_records = LibraryHistory.objects.all()  # Query all records
        serializer = LibraryHistorySerializer(library_records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)    