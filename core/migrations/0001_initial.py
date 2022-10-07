# Generated by Django 4.1.1 on 2022-10-07 19:14

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MakerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Upload date', models.DateTimeField(auto_now_add=True)),
                ('Last edited', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('variant', models.CharField(choices=[('3d_model', '3D model'), ('stencil', 'Stencil')], max_length=32)),
                ('description', models.FileField(upload_to='')),
                ('Thumbnail', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='MkrdbUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('models', models.ManyToManyField(to='core.makermodel')),
            ],
        ),
        migrations.CreateModel(
            name='MakerModelImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.makermodel')),
            ],
        ),
        migrations.CreateModel(
            name='MakerModelFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('variant', models.CharField(choices=[('model', 'Model file'), ('source', 'Source file'), ('code', 'Code file'), ('info', 'Info file')], max_length=32)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.makermodel')),
            ],
        ),
        migrations.AddField(
            model_name='makermodel',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.mkrdbuser'),
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.makermodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.mkrdbuser')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('commented_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.mkrdbuser')),
                ('commented_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.makermodel')),
            ],
        ),
    ]
