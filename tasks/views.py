from django.http import HttpResponse
from django.shortcuts import redirect, render
from tasks.models import Collection, Task
from django.utils.html import escape
from django.contrib import messages

# Create your views here.
def index(request):
    context ={}
    
    collection = Collection.get_default_collection()
    context['collections'] = Collection.objects.order_by("-slug")
    context['tasks'] = Task.objects.order_by("description")
    return render(request, 'tasks/index.html', context=context)
  
def add_collection(request):
    collection_name = escape(request.POST.get("Collection-name"))
    collection, created = Collection.objects.get_or_create(name=collection_name)
    if not created:
        return HttpResponse("A collection with that name already exists!", status=409)
  
 

    return HttpResponse(collection_name)
  
def add_task(request):
  collection = Collection.get_default_collection()
  description = escape(request.POST.get("task-description"))
  Task.objects.create(description=description, collection=collection)
  
  return HttpResponse(description)