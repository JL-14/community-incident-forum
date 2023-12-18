from django.shortcuts import render
from django.views import generic
from .models import Issue


class ReportList (generic.ListView):
    model = Issue
    queryset = Issue.objects.filter(approved = 1).order_by('-date_of_issue')
    template_name = 'index.html'
    paginate_by = 6
