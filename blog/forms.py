from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        # Setting Model used and field displayed
        model = Comment
        # trailing comma is neccessary for python 
        # to interpret as a tuple not a string
        fields = ('body',)
