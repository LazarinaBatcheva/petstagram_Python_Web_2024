from django import forms
from petstagram.common.models import Comment


class CommentBaseForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Add comment...'}),
        }


class CommentAddForm(CommentBaseForm):
    pass


class SearchForm(forms.Form):
    pet_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Search by pet name...'},
        )
    )