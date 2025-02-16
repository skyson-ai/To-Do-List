from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from tasks.models import Collection, Task
from django.utils.html import escape
from django.utils.text import slugify
from django.contrib import messages

# Create your views here.
def index(request):
    context ={}

    collection_slug = request.GET.get('collection')
    collection = Collection.get_default_collection()
    if collection_slug:
        collection = get_object_or_404(Collection, slug=collection_slug)

    context['collections'] = Collection.objects.order_by("-slug")
    context['tasks'] = Task.objects.order_by("description")
    return render(request, 'tasks/index.html', context=context)
  
def add_collection(request):
    collection_name = escape(request.POST.get("Collection-name"))
    collection, created = Collection.objects.get_or_create(name=collection_name, slug=slugify(collection_name))
    if not created:
        return HttpResponse("A collection with that name already exists!", status=409)
  
 

    return HttpResponse(collection_name)
  
def add_task(request):
  collection = Collection.get_default_collection()
  description = escape(request.POST.get("task-description"))
  Task.objects.create(description=description, collection=collection)
  
  return HttpResponse(description)

def get_tasks(request, Collection_pk):
    collection = get_object_or_404(Collection, pk=Collection_pk)
    tasks = collection.tasks.order_by("description")
    return HttpResponse("<br>".join(task.description for task in tasks))