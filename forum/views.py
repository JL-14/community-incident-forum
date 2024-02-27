from django.shortcuts import render
from django.views import generic
from .models import Issue


class IssueList (generic.ListView):
    # model = Issue
    queryset = Issue.objects.order_by('-date_of_issue')
    # template_name = 'issue_list.html'
    template_name = 'forum/index.html'
    paginate_by = 6
