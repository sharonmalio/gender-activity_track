from django.shortcuts import render

from django.http import HttpResponse
from django.views import generic

from genderTrack.models import Activity, Outcome, OutcomeInstance


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_activities = Activity.objects.all().count()
    num_instances = OutcomeInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = OutcomeInstance.objects.filter(status__exact='F').count()

    context = {
        'num_activities': num_activities,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class ActivityListView(generic.ListView):
    model = Activity
    paginate_by = 10

    def get_queryset(self):
        return Activity.objects.all()  # Get 5 books containing the title war


class ActivityDetailView(generic.DetailView):
    model = Activity
    paginate_by = 10
