from .models import (
    MakerModel,
    MakerModelImage,
    MakerModelFile,
    Favorite,
    Comment,
    Tag,
    MkrdbUser
)

from django.contrib import admin

admin.site.register(MakerModel)
admin.site.register(MakerModelImage)
admin.site.register(MakerModelFile)
admin.site.register(Favorite)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(MkrdbUser)
