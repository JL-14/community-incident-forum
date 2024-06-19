from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Issue, Comment
from .views import report_detail, comment_edit, comment_delete

class ViewsTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.issue = Issue.objects.create(title='Test Issue', content='Test content')
        self.comment = Comment.objects.create(comment_issue=self.issue, comment_author=self.user, comment_content='Test comment')

    def test_report_detail_view(self):
        # Test GET request
        response = self.client.get(reverse('report-detail', args=[self.issue.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/report_detail.html')
        # Test POST request
        data = {'comment_content': 'Test comment'}
        response = self.client.post(reverse('report-detail', args=[self.issue.slug]), data=data)
        self.assertEqual(response.status_code, 302)  # Redirect after form submission

    def test_comment_edit_view(self):
        # Test POST request
        data = {'comment_content': 'Edited comment'}
        self.client.force_login(self.user)  # Log in user
        response = self.client.post(reverse('comment-edit', args=[self.issue.slug, self.comment.id]), data=data)
        self.assertEqual(response.status_code, 302)  # Redirect after form submission
        edited_comment = Comment.objects.get(pk=self.comment.id)
        self.assertEqual(edited_comment.comment_content, 'Edited comment')

    def test_comment_delete_view(self):
        # Test POST request
        self.client.force_login(self.user)  # Log in user
        response = self.client.post(reverse('comment-delete', args=[self.issue.slug, self.comment.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after form submission
        self.assertFalse(Comment.objects.filter(pk=self.comment.id).exists())  # Ensure comment is deleted