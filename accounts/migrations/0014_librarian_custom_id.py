# Generated by Django 5.1.1 on 2024-12-15 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_remove_feeshistory_custom_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='librarian',
            name='custom_id',
            field=models.CharField(blank=True, editable=False, max_length=10, unique=True),
        ),
    ]
