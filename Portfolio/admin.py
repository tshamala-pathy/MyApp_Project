from django.contrib import admin
from .models import Introduction, AboutMe, Education, Skills,Experience, Project

# Register your models here.
admin.site.register(Introduction)
admin.site.register(AboutMe)
admin.site.register(Education)
admin.site.register(Skills)
admin.site.register(Experience)
admin.site.register(Project)