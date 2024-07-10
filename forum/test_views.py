from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Issue, Comment

class ViewsTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.issue = Issue.objects.create(issue_title='Test Issue', issue_content='Test content', user=self.user, date_of_issue=timezone.now())
        self.comment = Comment.objects.create(comment_issue=self.issue, comment_author=self.user, comment_content='Test comment')

    def test_comment_edit_view(self):
        # print(f"Slug: {self.issue.slug}, Comment ID: {self.comment.id}")
        # Test POST request
        data = {'comment_content': 'Edited comment'}
        self.client.force_login(self.user)  # Log in user
        response = self.client.post(reverse('comment_edit', args=[self.issue.slug, self.comment.id]), data=data)
        self.assertEqual(response.status_code, 302)  # Redirect after form submission
        edited_comment = Comment.objects.get(pk=self.comment.id)

        print(f"Original comment content: {self.comment.comment_content}")
        print(f"Edited comment content: {edited_comment.comment_content}")

        self.assertEqual(edited_comment.comment_content, 'Edited comment')

    def test_comment_delete_view(self):
        # print(f"Slug: {self.issue.slug}, Comment ID: {self.comment.id}")
        # Test POST request
        self.client.force_login(self.user)  # Log in user
        response = self.client.post(reverse('comment_delete', args=[self.issue.slug, self.comment.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after form submission
        self.assertFalse(Comment.objects.filter(pk=self.comment.id).exists())  # Ensure comment is deleted
