# Generated by Django 4.1 on 2023-06-20 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='img',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
