from django import forms
from tock_time_app.common.mixins.form_mixins import MarkRequiredFieldsMixin
from tock_time_app.tasks.models import Task


class TaskBaseForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'priority', 'deadline', 'description', 'note']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'note': forms.Textarea(attrs={'rows': 3}),
        }


class TaskCreateForm(MarkRequiredFieldsMixin, TaskBaseForm):
    required_indicator = '<span class="required-indicator">*</span>'


class TaskEditForm(TaskBaseForm):
    class Meta(TaskBaseForm.Meta):
        fields = ['title', 'priority', 'deadline', 'description', 'note', 'is_completed']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'note': forms.Textarea(attrs={'rows': 3}),
        }