from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.admin.sites import AdminSite
from django.urls import reverse
from .models import Issue, Comment
from .admin import IssueDetails, CommentAdmin

class AdminTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.user = User.objects.create_superuser(username='admin', email='admin@example.com', password='adminpassword')
        self.client.force_login(self.user)  # Log in admin user
        self.issue = Issue.objects.create(issue_title='Test Issue', issue_content='Test content', user=self.user)
        self.comment = Comment.objects.create(comment_issue=self.issue, comment_author=self.user, comment_content='Test comment')

    def test_issue_admin_page(self):
        # Test issue list page
        response = self.client.get(reverse('admin:forum_issue_changelist'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Issue')  # Check if test issue is displayed

        # Test issue detail page
        response = self.client.get(reverse('admin:forum_issue_change', args=[self.issue.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Issue')  # Check if test issue details are displayed

    def test_comment_admin_page(self):
        # Test comment list page
        response = self.client.get(reverse('admin:forum_comment_changelist'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test comment')  # Check if test comment is displayed

        # Test comment detail page
        response = self.client.get(reverse('admin:forum_comment_change', args=[self.comment.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test comment')  # Check if test comment details are displayed

    def test_custom_admin_methods(self):
        # Test custom method in CommentAdmin
        comment_admin = CommentAdmin(Comment, AdminSite())
        self.assertEqual(comment_admin.comment_issue_title(self.comment), 'Test Issue')  # Check if issue title is displayed correctly
