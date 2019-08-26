
import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class RegisterActivityForm(forms.Form):
    renewal_date = forms.DateField()

    outcome = forms.ChoiceField()
    activity = forms.CharField(max_length=200)

    sub_activity = forms.CharField(max_length=300)

    cost = forms.FloatField(max_length=300)
    description = forms.TextField(max_length=300)

    def register_activity_form(self):
        data = self.cleaned_data['renewal_date']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data
