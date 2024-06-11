from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Issue, Comment
from .forms import CommentForm


def landing_page(request):
    return render(request, 'forum/index.html')


def contact(request):
    return render(request, 'forum/contact.html')


class IssueList(generic.ListView):
    queryset = Issue.objects.order_by('-date_of_issue')
    template_name = 'forum/report_list.html'
    paginate_by = 6


def report_detail(request, slug):
    report = get_object_or_404(Issue, slug=slug)
    comments = report.comments.all().order_by("-created_on")
    comment_count = report.comments.filter(approved=True).count()
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, issue=report)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.comment_author = request.user
            comment.comment_issue = report
            comment.save()
            messages.success(request, 'Comment submitted and awaiting approval.')
            comment_form = CommentForm(issue=report)
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


def comment_edit(request, slug, comment_id):
    """To edit comments"""
    if request.method == "POST":
        queryset = Issue.objects.all()
        report = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.comment_author == request.user:
            comment = comment_form.save(commit=False)
            comment.report = report
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment')

    return HttpResponseRedirect(reverse('report-detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    View to delete comment
    """
    queryset = Issue.objects.all()
    report = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.comment_author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('report-detail', args=[slug]))
