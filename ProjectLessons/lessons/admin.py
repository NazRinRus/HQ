from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Users)
admin.site.register(Lesson)
admin.site.register(LessonUsers)
admin.site.register(ProductUsers)