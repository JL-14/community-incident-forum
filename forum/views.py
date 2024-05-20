from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Issue
from .forms import CommentForm


class IssueList (generic.ListView):
    queryset = Issue.objects.order_by('-date_of_issue')
    template_name = 'forum/index.html'
    paginate_by = 6

def report_detail(request, slug):
    # queryset = Issue.objects.all()
    report = get_object_or_404(Issue, slug=slug)
    comments = report.comments.all().order_by("-created_on")
    comment_count = report.comments.filter(approved=True).count()
    # comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, issue=report)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.comment_author = request.user
            comment.comment_issue = report
            comment.save()
            messages.success(request, 'Comment submitted and awaiting approval.')
        else:
            messages.error(request, 'Error submitting comment, please try again.')
    else:
        comment_form = CommentForm(issue=report)

    return render(
        request,
        "forum/report_detail.html",
        {
            "issue": report,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )
