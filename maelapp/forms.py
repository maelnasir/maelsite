from django.forms import ModelForm, Textarea
from maelapp.models import Feedback

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        widgets = {
            'feedback': Textarea(attrs={'cols': 80, 'rows': 5}),
        }