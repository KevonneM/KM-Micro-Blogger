from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        """form settings"""
        model = Comment
        fields = ('comment',)