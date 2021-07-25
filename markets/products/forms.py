from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'score']
        widgets = {
            'score': forms.RadioSelect(attrs={"style": "display:inline"})
        }


class CartProductForm(forms.Form):
    count = forms.IntegerField()