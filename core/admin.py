from django.contrib import admin
from .models import About, SocialLink

# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if About.objects.exists():
            return False
        return True

admin.site.register(About, AboutAdmin) 
admin.site.register(SocialLink)
