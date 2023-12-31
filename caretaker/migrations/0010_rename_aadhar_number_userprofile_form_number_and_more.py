# Generated by Django 4.2 on 2023-05-09 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caretaker', '0009_userprofile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='aadhar_number',
            new_name='form_number',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='backup_phonenumber',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='services_description',
            field=models.TextField(null=True),
        ),
    ]
