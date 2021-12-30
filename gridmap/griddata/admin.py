from django.contrib import admin

# Register your models here.
from .models import GridNode,GridArea,GridMember,GridSupport

admin.site.register(GridNode)
admin.site.register(GridArea)
admin.site.register(GridMember)
admin.site.register(GridSupport)