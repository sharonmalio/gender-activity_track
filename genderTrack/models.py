from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
import uuid


class Outcome(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter the name of the Outcome (e.g. Outcome1)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Activity(models.Model):
    """Model representing a book (but not a specific copy of a book)."""

    outcome = models.ManyToManyField(Outcome, help_text='Select your Outcome for this activity')
    activity = models.CharField(max_length=200)

    sub_activity = models.CharField(max_length=300, help_text='Enter the sub activity if any')

    cost = models.FloatField(max_length=300, help_text='Enter the actual cost of the activity above')
    description = models.TextField(max_length=300, help_text='Enter a brief description of the activity')

    def display_outcome(self):
        """Create a string for the Outcome. This is required to display genre in Admin."""
        return ', '.join(outcome.name for outcome in self.outcome.all())

    display_outcome.short_description = 'Outcome'

    def __str__(self):
        """String for representing the Model object."""
        return self.activity

    def get_absolute_url(self):
        """Returns the url to access a detail record for this activity."""
        return reverse('activity-detail', args=[str(self.id)])


class OutcomeInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for this particular book across whole library')
    outcome = models.ForeignKey('Outcome', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    Gender_Outcome_Target = (
        ('F', 'Full Target'),
        ('M', 'Medium Target'),
        ('B', 'Below Target'),
    )

    status = models.CharField(
        max_length=1,
        choices=Gender_Outcome_Target,
        blank=True,
        default='m',
        help_text='Status of the target',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.outcome.name})'
