# Generated by Django 4.2.1 on 2023-05-23 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0003_rename_dbffile_upfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upfile',
            name='file',
            field=models.FileField(upload_to='upload_files/years/'),
        ),
    ]
