from django.shortcuts import render
from django.http import HttpResponse
from papers.models import Paper
from papers.forms import UploadPaper
from users.models import CustomUser
from itertools import chain
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
import os
from django.shortcuts import redirect
import django.utils.timezone as timezone

def search_form(request):
    return render(request, 'search_form.html')


def search(request):
    error = False
    if 'nodes' in request.GET:
        title = request.GET['title']
        year = request.GET['year']
        author = request.GET['author']
        node = request.GET['nodes']

        papers_list = Paper.objects.filter(title__contains=title) & Paper.objects.filter(date__contains=year) & (Paper.objects.filter(author__first_name__contains=author) | Paper.objects.filter(author__last_name__contains=author)) & (Paper.objects.filter(author__Node__Name__contains=node) |Paper.objects.filter(author__Node__NodeID__contains=node) | Paper.objects.filter(author__Node__Location__contains=node) )
        papers_list =papers_list.distinct()
        if papers_list:
            return render(request, 'search_form.html',{'papers': papers_list, 'query': title})
        else:
            error= True
            return render(request, 'search_form.html', {'error': error})
    else:
        return render(request, 'search_form.html', {'error': error})

def paper_form(request):

    if request.method == "POST":
        form = UploadPaper(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.date = timezone.now()
            post.save()
            return redirect('publications')
    else:
        form = UploadPaper()
    return render(request, 'paper_form.html', {'form': form})

