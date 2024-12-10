from django import forms
from tock_time_app.common.mixins import MarkRequiredFieldsMixin
from tock_time_app.tasks.models import PersonalTask


class PersonalTaskBaseForm(forms.ModelForm):
    """
    Base form for PersonalTask model.
    Provides common configurations, including fields and custom widgets.
    """

    class Meta:
        model = PersonalTask
        fields = ['title', 'priority', 'deadline', 'description', 'note']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'note': forms.Textarea(attrs={'rows': 3}),
        }


class PersonalTaskCreateForm(MarkRequiredFieldsMixin, PersonalTaskBaseForm):
    """
    Form for creating a PersonalTask.
    Inherits the base form and adds functionality to mark required fields with an indicator.
    """

    required_indicator = '<span class="required-indicator">*</span>'


class PersonalTaskEditForm(PersonalTaskBaseForm):
    """
    Form for editing a PersonalTask.
    Extends the base form to include the 'is_completed' field.
    """

    class Meta(PersonalTaskBaseForm.Meta):
        fields = ['title', 'priority', 'deadline', 'description', 'note', 'is_completed']
        help_texts = {
            'is_completed': '* If you mark this task as completed, it will be moved to the Archive. *',
        }