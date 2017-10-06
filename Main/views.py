from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from .models import Event
from .forms import EventForm
from django.http import Http404 ,HttpResponseRedirect


def index(request):
    context = {
        "title": "HOME PAGE HOME",
        
    }
    return render(request, "index.html",context )



def post_create(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        #successfully created
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
        "title": "Create Event",
    }
    return render(request, "event_create.html", context)




def post_detail(request,slug=None):#   showing details
    instance = get_object_or_404(Event, slug=slug)
    context = {
        "instance": instance,
    }
    return render(request,"event_detail.html", context)


def post_list(request):
    queryset = Event.objects.all()
    context = {
        "event_list":queryset,
        "title":"All Events"
    }
    return render(request, "event_list.html", context)


    
