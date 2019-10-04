from django.utils.formats import sanitize_separators
from pyexpat import model

from django.db import models
from django.forms import ModelForm
from django.shortcuts import redirect
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
import uuid
from django.db.models import Sum
from django.utils import formats

# class Outcome(models.Model):
#     """Model representing a book genre."""
#     name = models.CharField(max_length=200, help_text='(e.g. Outcome1)')
#
#     def __str__(self):
#         """String for representing the Model object."""
#         return self.name


class Activity(models.Model):

    outcome_entries = [
        ('Outcome1', 'Outcome 1'),
        ('Outcome2', 'Outcome 2'),
        ('Outcome3', 'Outcome 3'),
        ('Outcome4', 'Outcome 4'),
    ]
    outcome = models.CharField(max_length=8, choices=outcome_entries, default='')
    total_budget = models.FloatField(max_length=100, default="", editable=True, help_text="Please enter the total "
                                                                                           "budget for your outcome")
    sanitize_separators(total_budget)
    # outcome = models.ForeignKey('Outcome', max_length=8, on_delete=models.CASCADE, default="", editable=True)
    activity = models.CharField(max_length=500, help_text="Please Enter the activity you are reporting for")

    sub_activity = models.CharField(max_length=500, help_text="Please Enter the sub_activity of the above activity")

    cost = models.FloatField(max_length=500, help_text="Enter the cost of the gender activity")
    sanitize_separators(cost)
    description = models.TextField(max_length=500, help_text="Tell us more here")
    # total_budget = formats.sanitize_separators(total_budget)
    # cost = formats.sanitize_separators(cost)



    def display_outcome(self):
        """Create a string for the Outcome."""
        return ', '.join(outcome.name for outcome in self.outcome.all())

    display_outcome.short_description = 'Outcome'

    def __str__(self):
        """String for representing the Model object."""
        return self.activity

    def get_absolute_url(self):
        """Returns the url to access a detail record for this activity."""
        return reverse('activity_detail', args=[str(self.id)])


class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['outcome', 'total_budget', 'activity', 'sub_activity', 'cost', 'description']


class CalculateTotals(Activity):
    select_outcome = models.ForeignKey(Activity, on_delete=models.PROTECT, default='outcome 1', editable=True,
                                       related_query_name='tag', related_name='tags')

    def __str__(self):
        """String for representing the Model object."""
        return self.activity

    def calculate(self):
        if self.outcome:
            total_sum = self.objects.aggregate(Sum('cost'))
            percentage = (total_sum / self.total_budget) * 100
            if percentage < 15:
                print("Need a Follow Up")
            else:
                print("doing Pretty well")
            return percentage



    def get_absolute_url(self):
        return reverse('activity_create')

#
# class EntryForm(ModelForm):
#     class Meta:
#         model = CalculateTotals

