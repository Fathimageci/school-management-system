# Generated by Django 5.1.1 on 2024-12-14 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_librarian_student_remove_office_staff_student_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeshistory',
            name='custom_id',
            field=models.CharField(blank=True, editable=False, max_length=10, unique=True),
        ),
        migrations.AddField(
            model_name='libraryhistory',
            name='custom_id',
            field=models.CharField(blank=True, editable=False, max_length=10, unique=True),
        ),
    ]