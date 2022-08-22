from atexit import register
from django.contrib import admin
from django import forms

from helloworld.models import Feedback, Portfolio

# define textareas for fields in Admin View - Portfolio & Feedback models
class textareaFieldAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        kwargs['widgets'] = {'description': forms.Textarea, 'feedback': forms.Textarea}
        return super().get_form(request, obj, **kwargs)

# register all related models with options
admin.site.register(Feedback, textareaFieldAdmin)
admin.site.register(Portfolio, textareaFieldAdmin)
