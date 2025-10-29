from django import forms
from . import models


class FeedbackForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    rating = forms.IntegerField()
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'columns': 15}))

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = models.FeedbackModel
        fields = '__all__'

        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'rating': 'Рейтинг',
            'feedback_text': 'Отзыв',
        }

class EdgarForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()

class EdgarForm(forms.ModelForm):
    class Meta:

        model = models.EdgarModel
        fields = '__all__'