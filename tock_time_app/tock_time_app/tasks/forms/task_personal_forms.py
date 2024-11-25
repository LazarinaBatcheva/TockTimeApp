from django import forms
from tock_time_app.common.mixins.form_mixins import MarkRequiredFieldsMixin
from tock_time_app.tasks.models import PersonalTask


class PersonalTaskBaseForm(forms.ModelForm):
    class Meta:
        model = PersonalTask
        fields = ['title', 'priority', 'deadline', 'description', 'note']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'note': forms.Textarea(attrs={'rows': 3}),
        }


class PersonalTaskCreateForm(MarkRequiredFieldsMixin, PersonalTaskBaseForm):
    required_indicator = '<span class="required-indicator">*</span>'


class PersonalTaskEditForm(PersonalTaskBaseForm):
    class Meta(PersonalTaskBaseForm.Meta):
        fields = ['title', 'priority', 'deadline', 'description', 'note', 'is_completed']