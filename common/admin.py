from django.contrib import admin
from common.models import Post, Tag, Profile, Image, UserImage

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(UserImage)
