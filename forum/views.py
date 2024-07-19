""" The views available on the website """

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Issue, Comment
from .forms import CommentForm


def landing_page(request):
    """ Set Home page """
    return render(request, 'forum/index.html')


def contact(request):
    """ Set Contact Us page """
    return render(request, 'forum/contact.html')


class IssueList(generic.ListView):
    """ Set report list view """
    queryset = Issue.objects.order_by('-date_of_issue')
    template_name = 'forum/report_list.html'
    paginate_by = 6


def get_navbar_urls():
    """ Set navbar links """
    return {
        'home_url': reverse('home'),
        'reportlist_url': reverse('reportlist'),
        'contact_url': reverse('contact'),
        'logout_url': reverse('account_logout'),
        'signup_url': reverse('account_signup'),
        'login_url': reverse('account_login'),
    }


def report_detail(request, slug):
    """ Set report detail view for more details about each issue """
    report = get_object_or_404(Issue, slug=slug)
    comments = report.comments.all().order_by("-created_on")
    comment_count = report.comments.filter(approved=True).count()
    comment_form = CommentForm()

    return render(
        request,
        "forum/report_detail.html",
        {
            "issue": report,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "issue_title": report.issue_title,
            "issue_content": report.issue_content
        },
    )


def add_comment(request, slug):
    """ Set view for adding comments """
    report = get_object_or_404(Issue, slug=slug)

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, issue=report)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.comment_author = request.user
            comment.comment_issue = report
            comment.save()
            messages.success(
                request,
                'Comment submitted and awaiting approval.'
            )
            return redirect('report-detail', slug=slug)
        else:
            messages.error(
                request,
                'Error submitting comment, please try again.'
            )
    else:
        comment_form = CommentForm(issue=report)

    return render(
        request,
        "forum/add_comment.html",
        {
            "comment_form": comment_form,
            "slug": slug,
            "issue_title": report.issue_title,
            "issue_content": report.issue_content
        }
    )


def comment_edit(request, slug, comment_id):
    """ Set view for editing comments """
    report = get_object_or_404(Issue, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.comment_author == request.user:
            comment = comment_form.save(commit=False)
            comment.report = report
            comment.approved = False  # Mark the comment as not approved
            comment.save()
            messages.success(request, 'Comment updated!')
            return HttpResponseRedirect(
                reverse('report-detail', kwargs={'slug': slug})
            )
        else:
            messages.error(request, 'Error updating comment')
    else:
        comment_form = CommentForm(instance=comment)

    return render(
        request,
        "forum/add_comment.html",
        {
            "comment_form": comment_form,
            "slug": slug,
            "issue_title": report.issue_title,
            "issue_content": report.issue_content,
            "edit_mode": True,
        }
    )


def comment_delete(request, slug, comment_id):
    """ View to delete comment """
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.comment_author == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.error(request, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('report-detail', args=[slug]))


# Custom error handlers
def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def handler500(request):
    """ Error Handler 500 - Internal Server Error """
    return render(request, "errors/500.html", status=500)
