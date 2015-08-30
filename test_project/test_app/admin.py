from django.contrib import admin

# Register your models here.

from .models import Board, Task, List


admin.site.register(Board)
admin.site.register(Task)
admin.site.register(List)
