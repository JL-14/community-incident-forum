from django.test import TestCase
from django.contrib.auth.models import User
from .forms import CommentForm, AdminCommentForm
from .models import Issue, Comment

class FormsTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.issue = Issue.objects.create(issue_title='Test Issue')
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_comment_form_initialization(self):
        # Test initialization without issue parameter
        form = CommentForm()
        self.assertIsInstance(form.fields['comment_issue'].widget, forms.HiddenInput)

        # Test initialization with issue parameter
        form = CommentForm(issue=self.issue)
        self.assertEqual(form.fields['comment_issue'].initial, self.issue)

    def test_comment_form_validation(self):
        # Test valid data
        data = {'comment_issue': self.issue.id, 'comment_content': 'Test comment content'}
        form = CommentForm(data=data)
        self.assertTrue(form.is_valid())

        # Test invalid data
        data['comment_issue'] = ''  # Empty comment_issue should fail validation
        form = CommentForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('comment_issue', form.errors)

    def test_admin_comment_form_customization(self):
        # Test queryset and label_from_instance customization
        form = AdminCommentForm()
        self.assertTrue(form.fields['comment_issue'].queryset.exists())
        self.assertEqual(form.fields['comment_issue'].label_from_instance(self.issue), 'Test Issue')

    def test_comment_form_cleaning(self):
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
