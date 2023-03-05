from django import forms
from . import models


class OrderCommentForm(forms.ModelForm):
    class Meta:
        model = models.OrderComment
        fields = ('order', 'client', 'comment')
        widgets = {'order': forms.HiddenInput(), 'client': forms.HiddenInput(),
        'comment': forms.Textarea(attrs={
                'class': 'comment-field',
                'placeholder': 'Type your comment here...'
            })}

class OrderLineForm(forms.ModelForm):
    class Meta:
        model = models.OrderLine
        fields = ('order', 'service', 'quantity')

    def __init__(self, *args, client=None, **kwargs):
        super().__init__(*args, **kwargs)
        if client:
            self.fields['order'].queryset = models.Order.objects.filter(car__client=client)













