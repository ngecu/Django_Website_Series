from django.contrib import admin

# Register your models here.
from .models import *
from tinymce.widgets import TinyMCE

class TutorialAdmin(admin.ModelAdmin):


    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }


admin.site.register(Tutorial,TutorialAdmin)
admin.site.register(Archive,TutorialAdmin)
admin.site.register(TutorialSeries)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Subscription)