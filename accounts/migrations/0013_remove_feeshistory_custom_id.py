# Generated by Django 5.1.1 on 2024-12-15 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_remove_librarian_custom_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feeshistory',
            name='custom_id',
        ),
    ]
