from django.db import models
from django.forms import ModelForm
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
import uuid
from django.db.models import Sum


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
    # outcome = models.ForeignKey('Outcome', max_length=8, on_delete=models.CASCADE, default="", editable=True)
    activity = models.CharField(max_length=500, help_text="Please Enter the activity you are reporting for")

    sub_activity = models.CharField(max_length=500, help_text="Please Enter the sub_activity of the above activity")

    cost = models.FloatField(max_length=500, help_text="Enter the cost of the gender activity")
    description = models.TextField(max_length=500, help_text="Tell us more here")

    def calculate(self):
        if self.outcome:
            total_sum = self.objects.aggregate(Sum('cost'))
            percentage = (total_sum/self.total_budget) * 100
            if percentage < 15:
                print("Need a Follow Up")
            else:
                print("doing Pretty well")
            return percentage

    def display_outcome(self):
        """Create a string for the Outcome."""
        return ', '.join(outcome.name for outcome in self.outcome.all())

    display_outcome.short_description = 'Outcome'

    def __str__(self):
        """String for representing the Model object."""
        return self.activity

    def get_absolute_url(self):
        """Returns the url to access a detail record for this activity."""
        return reverse('activity-detail', args=[str(self.id)])


class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['outcome', 'total_budget', 'activity', 'sub_activity', 'cost', 'description']


# class CalculateTotals(models.Model):
#     select_outcome = models.ForeignKey(Activity, on_delete=models.PROTECT)
#
#     def calculate(self):
#         if  self.select_outcome:
#             Activity.objects.aggregate(total_sum = Sum('cost'))
#         else:
#             print("An error has occured")
#         return total_sum
#
#     def calculate_percentage(self):
#         percentage = (total_sum/Activity.total_budget)*100
#         if percentage < 15:
#             print("Need a Follow Up")
#         else:
#             print("doing Pretty well")
#         return percentage

