""" Comment form configuration """
from django import forms
from .models import Comment, Issue


class CommentForm(forms.ModelForm):
    """ Set the fields for the Comment Form """
    class Meta:
        """ Meta setting for comment form """
        model = Comment
        fields = ['comment_issue', 'comment_content']

    def __init__(self, *args, **kwargs):
        issue = kwargs.pop('issue', None)
        super().__init__(*args, **kwargs)
        if issue:
            self.fields['comment_issue'].initial = issue
        self.fields['comment_issue'].widget = forms.HiddenInput()
        """ Function to remove the requirement to select issue for comments """

    def clean_comment_issue(self):
        """ Return comment_issue form in clean format (not displayed) """
        return self.cleaned_data['comment_issue']


class AdminCommentForm(forms.ModelForm):
    """ Settings for comment form in admin view """
    class Meta:
        """ Meta settings for form in admin view """
        model = Comment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment_issue'].queryset = Issue.objects.all()
        self.fields['comment_issue'].label_from_instance = (
            lambda obj: obj.issue_title
        )
