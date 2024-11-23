from django import forms

from tock_time_app.common.mixins.form_mixins import MarkRequiredFieldsMixin
from tock_time_app.tasks.models import Task


class TaskBaseForm(MarkRequiredFieldsMixin, forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'priority', 'deadline', 'description', 'assigned_to', 'team', 'note']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'assigned_to': forms.SelectMultiple(attrs={'size': 3}),
            'note': forms.Textarea(attrs={'rows': 3}),
        }


class TaskCreateForm(TaskBaseForm):
    pass