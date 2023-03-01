from django import forms
from . import models


class OrderCommentForm(forms.ModelForm):
    class Meta:
        model = models.OrderComment
        fields = ('order', 'client', 'comment')
        widgets = {'order': forms.HiddenInput(), 'client': forms.HiddenInput(),
        'comment': forms.Textarea(attrs={'class': 'comment-field'})}