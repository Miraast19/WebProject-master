from django.contrib import admin
from django.contrib.admin import ModelAdmin
from api.models import Car, Model, Basket, User, Comment


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ('id', 'author', 'on_car')
# Register your models here.


# admin.site.register(Comment)
admin.site.register(Car)
admin.site.register(Model)
admin.site.register(Basket)
admin.site.register(User)