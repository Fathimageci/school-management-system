# Generated by Django 5.1.1 on 2024-12-15 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_librarian_custom_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='office_staff',
            name='custom_id',
            field=models.CharField(blank=True, editable=False, max_length=10, unique=True),
        ),
    ]
