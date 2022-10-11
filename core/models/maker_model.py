from .user import MkrdbUser

from django.db import models
from django.conf import settings


class MakerModel(models.Model):
    VARIANTS = [
        ('3d_model', '3D model'),
        ('stencil', 'Stencil'),
    ]

    uploaded_by = models.ForeignKey(to=MkrdbUser, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(name='Upload date', auto_now_add=True)
    last_edited = models.DateTimeField(name='Last edited', auto_now=True)

    name = models.CharField(max_length=128)
    variant = models.CharField(max_length=32, choices=VARIANTS)
    description = models.FileField(upload_to=settings.MAKER_MODEL_DESCRIPTION_MD_ROOT)

    thumbnail = models.ImageField(name='Thumbnail', null=True, upload_to=settings.MAKER_MODEL_IMAGE_ROOT)  # generate later

    def __str__(self):
        return f'[{self.uploaded_by.username}:{self.variant}] {self.name}'


class MakerModelFile(models.Model):
    VARIANTS = [
        ('model', 'Model file'),
        ('source', 'Source file'),
        ('code', 'Code file'),
        ('info', 'Info file'),
    ]

    file = models.FileField(upload_to=settings.MAKER_MODEL_MODEL_FILE_ROOT)
    model = models.ForeignKey(to=MakerModel, on_delete=models.CASCADE)
    variant = models.CharField(max_length=32, choices=VARIANTS)

    def __str__(self):
        return f'[{self.model.uploaded_by.username}:{self.variant}] {self.model.name}'


class MakerModelImage(models.Model):
    image = models.ImageField(upload_to=settings.MAKER_MODEL_IMAGE_ROOT)
    model = models.ForeignKey(to=MakerModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.model.uploaded_by.username}:{self.model.variant}] {self.model.name}'


class Favorite(models.Model):
    user = models.ForeignKey(to=MkrdbUser, on_delete=models.CASCADE)
    model = models.ForeignKey(to=MakerModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} -> {self.model.name}'


class Comment(models.Model):
    commented_by = models.ForeignKey(to=MkrdbUser, on_delete=models.SET_NULL, null=True)
    commented_on = models.ForeignKey(to=MakerModel, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.commented_by.username} -> {self.commented_on.name}'


class Tag(models.Model):
    name = models.CharField(max_length=128)
    models = models.ManyToManyField(to=MakerModel)

    def __str__(self):
        return self.name