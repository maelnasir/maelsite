# from atexit import register
from django.contrib import admin
from django import forms

from maelapp.models import Feedback, Portfolio, UploadImage

# define textareas for fields in Admin View - Portfolio & Feedback models
class textareaFieldAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        kwargs['widgets'] = {'description': forms.Textarea, 'feedback': forms.Textarea} # use textarea for description & feedback
        return super().get_form(request, obj, **kwargs)

# register all related models with options
admin.site.register(Feedback, textareaFieldAdmin)
admin.site.register(Portfolio, textareaFieldAdmin)
admin.site.register(UploadImage)

