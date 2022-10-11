# Generated by Django 4.1.1 on 2022-10-11 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makermodel',
            name='description',
            field=models.FileField(upload_to='data/md/'),
        ),
        migrations.AlterField(
            model_name='makermodelfile',
            name='file',
            field=models.FileField(upload_to='data/models/'),
        ),
        migrations.AlterField(
            model_name='makermodelimage',
            name='image',
            field=models.ImageField(upload_to='data/img/'),
        ),
    ]