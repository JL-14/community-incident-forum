from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Issue


class IssueList (generic.ListView):
    queryset = Issue.objects.order_by('-date_of_issue')
    template_name = 'forum/index.html'
    paginate_by = 6

def report_detail(request, slug):
    """
    Display an individual :model:`forum.Issue`.

    **Context**

    ``post``
        An instance of :model:`forum.Issue`.

    **Template:**

    :template:`forum/report_detail.html`
    """

    queryset = Issue.objects.filter(approved=1)
    report = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "forum/report_detail.html",
        {"issue": report},
    )