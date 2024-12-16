from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import*
from Admin.serializers import*
# Create your views here.

#Student
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

    def post(self, request, *args, **kwargs):
        # Deserialize and validate the incoming data
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            # Save the new student record
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Return errors if validation fails
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentRetrieveUpdateDeleteView(APIView):
    """
    Handles retrieving, updating, and deleting a specific student.
    """

    def get_object(self, pk):
        try:
            # Fetch the student by primary key
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            # Return 404 if not found
            return None

    def get(self, request, pk, *args, **kwargs):
        # Retrieve a specific student
        student = self.get_object(pk)
        if student is None:
            return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)
        # Serialize and return the student
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        # Retrieve the student for update
        student = self.get_object(pk)
        if student is None:
            return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)
        # Deserialize and validate the data
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            # Save the updated student
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        # Return validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        # Retrieve the student for deletion
        student = self.get_object(pk)
        if student is None:
            return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)
        # Delete the student
        student.delete()
        return Response({"message": "Student deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


#libraryHistory
class LibraryHistoryListCreateView(APIView):
    """
    Handles listing all library records and creating a new library record.
    """

    def get(self, request, *args, **kwargs):
        library_records = LibraryHistory.objects.all()  # Query all records
        serializer = LibraryHistorySerializer(library_records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = LibraryHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LibraryHistoryDetailView(APIView):
    """
    Handles retrieving, updating, and deleting a specific library record.
    """

    def get_object(self, pk):
        try:
            return LibraryHistory.objects.get(pk=pk)
        except LibraryHistory.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        record = self.get_object(pk)
        if record is None:
            return Response({"error": "Library record not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = LibraryHistorySerializer(record)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        record = self.get_object(pk)
        if record is None:
            return Response({"error": "Library record not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = LibraryHistorySerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        record = self.get_object(pk)
        if record is None:
            return Response({"error": "Library record not found."}, status=status.HTTP_404_NOT_FOUND)
        record.delete()
        return Response({"message": "Library record deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    

#Fee History
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
    
#librarian
class LibrarianListCreateView(APIView):
    """
    View to list and create Librarian accounts.
    """

    def get(self, request):
        librarians = Librarian.objects.all()
        serializer = LibrarianSerializer(librarians, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LibrarianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LibrarianDetailView(APIView):
    """
    View to retrieve, update, or delete a Librarian account.
    """

    def get_object(self, pk):
        try:
            return Librarian.objects.get(pk=pk)
        except Librarian.DoesNotExist:
            return None

    def get(self, request, pk):
        librarian = self.get_object(pk)
        if librarian is None:
            return Response({"error": "Librarian not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = LibrarianSerializer(librarian)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        librarian = self.get_object(pk)
        if librarian is None:
            return Response({"error": "Librarian not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = LibrarianSerializer(librarian, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        librarian = self.get_object(pk)
        if librarian is None:
            return Response({"error": "Librarian not found."}, status=status.HTTP_404_NOT_FOUND)
        librarian.delete()
        return Response({"message": "Librarian deleted successfully."}, status=status.HTTP_204_NO_CONTENT)    
    

#Office staff    
class OfficeStaffListCreateView(APIView):
    """
    View to list and create Office Staff accounts.
    """

    def get(self, request):
        office_staff = Office_staff.objects.all()
        serializer = OfficeStaffSerializer(office_staff, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OfficeStaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OfficeStaffDetailView(APIView):
    """
    View to retrieve, update, or delete an Office Staff account.
    """

    def get_object(self, pk):
        try:
            return Office_staff.objects.get(pk=pk)
        except Office_staff.DoesNotExist:
            return None

    def get(self, request, pk):
        office_staff = self.get_object(pk)
        if office_staff is None:
            return Response({"error": "Office Staff not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = OfficeStaffSerializer(office_staff)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        office_staff = self.get_object(pk)
        if office_staff is None:
            return Response({"error": "Office Staff not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = OfficeStaffSerializer(office_staff, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        office_staff = self.get_object(pk)
        if office_staff is None:
            return Response({"error": "Office Staff not found."}, status=status.HTTP_404_NOT_FOUND)
        office_staff.delete()
        return Response({"message": "Office Staff deleted successfully."}, status=status.HTTP_204_NO_CONTENT)    