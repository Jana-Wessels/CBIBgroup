from django.shortcuts import render
from django.http import HttpResponse
from papers.models import Paper
from users.models import CustomUser
from itertools import chain
import os

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
        return render(request, 'search_form.html',{'papers': papers_list, 'query': title})

    else:
        return render(request, 'search_form.html', {'error': error})


#def getPDF(request):
#    path =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#    path =path+"/media/media/Ethics_Form.pdf"
#    image_data = open(path, "rb").read()
#    return HttpResponse(image_data, content_type="application/pdf")

