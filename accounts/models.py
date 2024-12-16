from django.db import models
import re
from django.contrib.auth.models import Permission,Group
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.forms import ValidationError
from django.utils import timezone
import random
from django.core.validators import RegexValidator
import phonenumbers
from django.conf import settings
from django.db import models
from PIL import Image
from django.core.exceptions import ValidationError
import uuid
# Create your models here.

phone_regex = RegexValidator(
        regex=r'^\d{9,15}$', 
        message="Phone number must be between 9 and 15 digits."
    )
def validate_file_size(value):
    filesize = value.size
    if filesize > 10485760:  # 10 MB
        raise ValidationError("The maximum file size that can be uploaded is 10MB")
    return value

class Country_Codes(models.Model):
    country_name = models.CharField(max_length=100,unique=True)
    calling_code = models.CharField(max_length=10,unique=True)

    def __str__(self):
        return f"{self.country_name} ({self.calling_code})"
    
    class Meta:
        ordering = ['calling_code']



class UserManager(BaseUserManager):
    def create_user(self, email=None, phone_number=None, password=None, **extra_fields):
        if not email and not phone_number:
            raise ValueError('Either email or phone number must be provided')

        # Normalize the email if provided
        if email:
            email = self.normalize_email(email)

        # Handle phone number validation if provided and not a superuser
        if phone_number and not extra_fields.get('is_superuser'):
            full_number = f"{extra_fields.get('country_code')}{phone_number}"
            try:
                parsed_number = phonenumbers.parse(full_number, None)
                if not phonenumbers.is_valid_number(parsed_number):
                    raise ValidationError("Invalid phone number.")
                phone_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
            except phonenumbers.NumberParseException:
                raise ValidationError("Invalid phone number format.")

        # Create and return the user object
        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, phone_number=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if email is None:
            raise ValueError('Superuser must have an email address.')

        return self.create_user(email=email, phone_number=phone_number, password=password, **extra_fields)

class User(AbstractBaseUser):
    created_at = models.DateTimeField(auto_now_add=True)
    # Role-based fields
    is_office_staff = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default=False)
    
    # Admin-related fields
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # Any other fields common to both roles
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True,validators=[phone_regex], null=True, blank=True)
    address = models.CharField(max_length=30)
    place = models.CharField(max_length=20,blank=True,null=True)
    joining_date = models.DateField(null=True,blank=True)
    


    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = []

    objects = UserManager()
    
    groups = models.ManyToManyField(
        Group,
        related_name='app1_user_groups',  # Add a unique related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    # Override user_permissions field with a unique related_name
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='app1_user_permissions'  # Add a unique related_name
    )
    
    def __str__(self):
        return self.email if self.email else self.phone_number

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

class Student(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    class_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.roll_number})"   

class LibraryHistory(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE) 
    book_name = models.CharField(max_length=255)
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[('Borrowed', 'Borrowed'), ('Returned', 'Returned')],
        default='Borrowed'
    )

    def __str__(self):
        return f"{self.book_name} - {self.student.first_name} ({self.status})"

class FeesHistory(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.fee_type} - {self.student.first_name} (${self.amount})"


class Office_staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='office_staff')
    custom_id = models.CharField(max_length=10, unique=True, editable=False, blank=True) 
    about = models.TextField()
    profile_image = models.ImageField(upload_to='f-profile_images/', null=True, blank=True, validators=[validate_file_size])  # Profile image field    
    verification_id = models.CharField(max_length=255, blank=True, null=True)  
    verificationid_number = models.CharField(max_length=50, blank=True, null=True)  # ID number field


    def save(self, *args, **kwargs):
        if not self.custom_id:
            # Generate the custom ID format
            self.custom_id = f'FR{self.user.id}'  # Format: FR{id}

        super(Office_staff, self).save(*args, **kwargs)


    def __str__(self):
        return self.custom_id         

class Librarian(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='librarian')
    custom_id = models.CharField(max_length=10, unique=True, editable=False, blank=True) 
    about = models.TextField()
    profile_image = models.ImageField(upload_to='d-profile-images/', null=True, blank=True, validators=[validate_file_size])  # Profile image field

    verification_id = models.CharField(max_length=255, blank=True, null=True)  
    verificationid_number = models.CharField(max_length=50, blank=True, null=True)  # ID number field
    created_date = models.DateTimeField(default=timezone.now,blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.custom_id:
            # Generate the custom ID format
            self.custom_id = f'LR{self.user.id}'  # Format: LR{id}

        super(Librarian, self).save(*args, **kwargs)

    def __str__(self):
        return self.custom_id    
    
 

