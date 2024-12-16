from rest_framework import serializers
from accounts.models import*

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class LibraryHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryHistory
        fields = '__all__'

class FeesHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FeesHistory
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)  # Explicitly add password field

    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'phone_number', 'address', 'place', 'joining_date', 'is_office_staff', 'is_librarian', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password', None)  # Extract the password from the data
        user = User(**validated_data)
        if password:
            user.set_password(password)  # Hash the password
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)  # Extract the password from the data
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)  # Hash the new password
        instance.save()
        return instance


# class LibraryManagementSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Librarian
#         fields = '__all__'

# class OfficeStaffSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Office_staff
#         fields = '__all__'
        
class LibrarianSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Use the corrected UserSerializer

    class Meta:
        model = Librarian
        fields = ['id', 'user', 'about', 'profile_image', 'verification_id', 'verificationid_number', 'created_date']

    def create(self, validated_data):
        user_data = validated_data.pop('user')  # Extract nested user data
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save(is_librarian=True)  # Mark user as librarian

        librarian = Librarian.objects.create(user=user, **validated_data)
        return librarian
    
class OfficeStaffSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Use the corrected UserSerializer

    class Meta:
        model = Office_staff
        fields = ['id', 'user', 'about', 'profile_image', 'verification_id', 'verificationid_number']

    def create(self, validated_data):
        user_data = validated_data.pop('user')  # Extract nested user data
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save(is_office_staff=True)  # Mark user as office staff

        office_staff = Office_staff.objects.create(user=user, **validated_data)
        return office_staff    