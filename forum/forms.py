from django import forms
from .models import Comment, Issue

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_issue', 'comment_content']

    def __init__(self, *args, **kwargs):
        report = kwargs.pop('issue', None)
        super().__init__(*args, **kwargs)
        if report:
            self.fields['comment_issue'].initial = report
            self.fields['comment_issue'].widget = forms.HiddenInput()

    def clean_comment_issue(self):
        return self.cleaned_data['comment_issue']


class AdminCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        issue = kwargs.pop('issue', None)
        super().__init__(*args, **kwargs)
        self.fields['comment_issue'].queryset = Issue.objects.all()
        self.fields['comment_issue'].label_from_instance = lambda obj: obj.issue_title