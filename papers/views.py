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
from django.shortcuts import render, get_object_or_404

from xhtml2pdf import pisa
from io import StringIO, BytesIO
from django.template.loader import get_template
from django.template import Context


def search_form(request):
    return render(request, 'search_form.html')


def search(request):
    error = False
    if 'nodes' in request.GET:
        title = request.GET['title']
        year = request.GET['year']
        author = request.GET['author']
        node = request.GET['nodes']

        papers_list = Paper.objects.filter(Title__contains=title) & Paper.objects.filter(Date__contains=year) & (Paper.objects.filter(Author__first_name__contains=author) | Paper.objects.filter(Author__last_name__contains=author)) & (Paper.objects.filter(Author__Node__Name__contains=node) |Paper.objects.filter(Author__Node__NodeID__contains=node) | Paper.objects.filter(Author__Node__Location__contains=node) )
        papers_list =papers_list.distinct()
        if papers_list:
            return render(request, 'search_form.html',{'papers': papers_list, 'query': title})
        else:
            error= True
            return render(request, 'search_form.html', {'error': error})
    else:
        return render(request, 'search_form.html', {'error': error})

def Pdf_search(request):
    error = False
    if 'nodes' in request.GET:
        title = request.GET['title']
        year = request.GET['year']
        author = request.GET['author']
        node = request.GET['nodes']

        papers_list = Paper.objects.filter(Title__contains=title) & Paper.objects.filter(Date__contains=year) & (Paper.objects.filter(Author__first_name__contains=author) | Paper.objects.filter(Author__last_name__contains=author)) & (Paper.objects.filter(Author__Node__Name__contains=node) |Paper.objects.filter(Author__Node__NodeID__contains=node) | Paper.objects.filter(Author__Node__Location__contains=node) )
        papers_list =papers_list.distinct()
        if papers_list:
            return papers_list
        else:
            error= True
            return papers_list


def paper_form(request):
    if request.method == "POST":
        form = UploadPaper(request.POST, request.FILES)
        if form.is_valid():
            paper = form.save(commit=False)
            paper.Date = timezone.now()
            paper.save()
            form.save_m2m()
            return redirect('paper_detail' , pk = paper.pk)
    else:
        form = UploadPaper()
    return render(request, 'paper_form.html', {'form': form})

def paper_detail(request, pk):
    paper = get_object_or_404(Paper, pk=pk)
    return render(request, 'paper_confirmation.html', {'paper': paper})

def paper_edit(request, pk):
    paper = get_object_or_404(Paper, pk=pk)
    if request.method == "POST":
        form = UploadPaper(request.POST, request.FILES, instance=paper)
        if form.is_valid():
            paper = form.save(commit=False)
            paper.save()
            form.save_m2m()
            return redirect('paper_detail', pk=paper.pk)
    else:
        form = UploadPaper(instance=paper)
    return render(request, 'paper_form.html', {'form': form})

def pdf_form(request):
    return render(request, 'generate_report_form.html')

def html_to_pdf_view(request):
    template = get_template("pdf_view.html")
    context = {'pagesize':'A4', 'papers':Pdf_search(request)}
    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(StringIO(html), dest=result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse('Errors')