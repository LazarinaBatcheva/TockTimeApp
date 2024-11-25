from django import forms
from tock_time_app.common.mixins.form_mixins import MarkRequiredFieldsMixin
from tock_time_app.tasks.models import TeamTask


class TeamTaskCreateForm(MarkRequiredFieldsMixin, forms.ModelForm):
    required_indicator = '<span class="required-indicator">*</span>'

    class Meta:
        model = TeamTask
        fields = ['title', 'deadline', 'assigned_to', 'description', 'note']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'assigned_to': forms.SelectMultiple(attrs={'size': 3}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'note': forms.Textarea(attrs={'rows': 3}),
        }