# Generated by Django 4.2.1 on 2023-05-23 16:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('uploader', '0002_rename_upfile_dbffile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DBFFile',
            new_name='UPFile',
        ),
    ]