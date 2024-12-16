from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import*
from office_staff.serializers import*

# Create your views here.

#Student Details Access
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
    
#Fee history access    
class FeesHistoryListCreateView(APIView):
    """
    Handles listing all fees records and creating a new fees record.
    """

    def get(self, request, *args, **kwargs):
        fees_records = FeesHistory.objects.all()
        serializer = FeesHistorySerializer(fees_records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = FeesHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#FeeHistory
class FeesHistoryDetailView(APIView):
    """
    Handles retrieving, updating, and deleting a specific fees record.
    """

    def get_object(self, pk):
        try:
            return FeesHistory.objects.get(pk=pk)
        except FeesHistory.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        record = self.get_object(pk)
        if record is None:
            return Response({"error": "Fees record not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = FeesHistorySerializer(record)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        record = self.get_object(pk)
        if record is None:
            return Response({"error": "Fees record not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = FeesHistorySerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        record = self.get_object(pk)
        if record is None:
            return Response({"error": "Fees record not found."}, status=status.HTTP_404_NOT_FOUND)
        record.delete()
        return Response({"message": "Fees record deleted successfully."}, status=status.HTTP_204_NO_CONTENT)        
    
#Library history view
class LibraryHistoryListCreateView(APIView):
    """
    Handles listing all library records and creating a new library record.
    """

    def get(self, request, *args, **kwargs):
        library_records = LibraryHistory.objects.all()  # Query all records
        serializer = LibraryHistorySerializer(library_records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)