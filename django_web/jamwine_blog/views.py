# from django.http import HttpResponse
from django.shortcuts import render
import json

def page_view(request, page):
    template_name = f'jamwine_blog/{page}.html'
    return render(request, template_name)


# def epicyclic_data(request):
#     # Generate data for epicyclic gearing graph
#     data = {"nodes": [{"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}], "links": [{"source": 1, "target": 2}, {"source": 2, "target": 3}, {"source": 3, "target": 4}]}
#     return HttpResponse(json.dumps(data), content_type='application/json')
