# Generated by Django 2.2.7 on 2019-11-23 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_classification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimage',
            name='image',
            field=models.FileField(upload_to='imgs/'),
        ),
    ]
