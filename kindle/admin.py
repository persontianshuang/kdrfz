


from django.contrib import admin

# Register your models here.
from kindle import models

admin.site.register(models.Book)
admin.site.register(models.Mark)
admin.site.register(models.Note)


