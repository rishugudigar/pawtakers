# Generated by Django 4.2 on 2023-06-17 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caretaker', '0014_service_alter_userprofile_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='price',
        ),
        migrations.RemoveField(
            model_name='servicedescription',
            name='price',
        ),
    ]