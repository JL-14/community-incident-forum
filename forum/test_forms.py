from django.test import TestCase
from .forms import CommentForm
from .models import Comment, Issue, User
from .forms import forms

class TestCommentForm(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.issue = Issue.objects.create(title='Test Issue')

    def test_form_initialization_with_issue(self):
        form = CommentForm(issue=self.issue)
        self.assertEqual(form.fields['comment_issue'].initial, self.issue)
        self.assertIsInstance(form.fields['comment_issue'].widget, forms.HiddenInput)

    def test_form_initialization_without_issue(self):
        form = CommentForm()
        self.assertNotIn('comment_issue', form.fields)

    def test_form_validation(self):
        # Test valid data
        data = {'comment_issue': self.issue.id, 'comment_content': 'Test comment content'}
        form = CommentForm(data=data)
        self.assertTrue(form.is_valid())

        # Test invalid data
        data['comment_issue'] = ''  # Empty comment_issue should fail validation
        form = CommentForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('comment_issue', form.errors)

    def test_form_cleaning(self):
        # Test cleaning method for comment_issue
        data = {'comment_issue': self.issue.id, 'comment_content': 'Test comment content'}
        form = CommentForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['comment_issue'], self.issue)

        # Test cleaning method for invalid comment_issue
        data['comment_issue'] = 'invalid_issue_id'
        form = CommentForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertNotIn('comment_issue', form.cleaned_data)

        # Test cleaning method for missing comment_issue
        del data['comment_issue']
        form = CommentForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertNotIn('comment_issue', form.cleaned_data)
