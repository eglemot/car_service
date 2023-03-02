from django import forms
from . import models


class OrderCommentForm(forms.ModelForm):
    class Meta:
        model = models.OrderComment
        fields = ('order', 'client', 'comment')
        widgets = {'order': forms.HiddenInput(), 'client': forms.HiddenInput(),
        'comment': forms.Textarea(attrs={'class': 'comment-field'})}

class OrderLineForm(forms.ModelForm):
    service = forms.ModelChoiceField(queryset=models.Service.objects.all())
    quantity = forms.IntegerField(min_value=1)

    class Meta:
        model = models.OrderLine
        fields = ('service', 'quantity')
