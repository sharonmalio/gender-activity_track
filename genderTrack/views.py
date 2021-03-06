from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from genderTrack.models import Activity, CalculateTotals


def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_activities = Activity.objects.all().count()
    # num_instances = OutcomeInstance.objects.all().count()
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    # Available books (status = 'a')
    # num_instances_available = OutcomeInstance.objects.filter(status__exact='F').count()

    context = {
        'num_activities': num_activities,
        # 'num_instances': num_instances,
        # 'num_instances_available': num_instances_available,
        'num_visits': num_visits
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class ActivityListView(generic.ListView):
    model = Activity
    paginate_by = 10

    def get_queryset(self):
        return Activity.objects.all()


class ActivityDetailView(generic.DetailView):
    model = Activity
    paginate_by = 10


class ActivityCreate(CreateView):
    model = Activity
    fields = '__all__'
    initial = {'date_of_creation': '05/01/2018'}


# @method_decorator(login_required, name='ActivityCalculateView')
class ActivityCalculateView(CreateView):
    model = CalculateTotals
    fields = ['outcome']

    def savecalculate(request):
        if request.method == 'POST':
            form = CalculateTotals(request.POST)
            if form.is_valid():
                calculateinstance = form.save()
                calculateinstance.calculate()
                calculateinstance.save()
            return HttpResponseRedirect('activity_list')


class ActivityUpdate(UpdateView):
    model = Activity
    fields = ['outcome', 'activity', 'sub_activity']


class ActivityDelete(DeleteView):
    model = Activity
    success_url = reverse_lazy('activities')
