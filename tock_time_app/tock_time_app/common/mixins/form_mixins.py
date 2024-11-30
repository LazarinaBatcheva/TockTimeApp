from django.utils.safestring import mark_safe


class FieldHandlerMixin:
    """Base mixin providing utility methods for manipulating form fields and their attributes."""
    def set_field_attribute(self, field_names, attribute, value):
        for field_name in field_names:
            if field_name in self.fields:
                setattr(self.fields[field_name], attribute, value)

    def update_widget_attrs(self, field_names, attribute, value):
        """ Updates widget attributes for the specified fields. """
        for field_name in field_names:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs.update({attribute: value})


class PlaceholderMixin(FieldHandlerMixin):
    """ Mixin for adding placeholder attributes to form fields. """

    placeholder_fields = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_placeholders()

    def set_placeholders(self):
        for field_name, placeholder_text in self.placeholder_fields.items():
            if field_name in self.fields:
                self.fields[field_name].widget.attrs.update({'placeholder': placeholder_text})


class NoHelpTextMixin(FieldHandlerMixin):
    """ Mixin for removing help text from specified form fields. """

    help_text_fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.remove_help_text()

    def remove_help_text(self):
        self.set_field_attribute(self.help_text_fields, 'help_text', None)


class MarkRequiredFieldsMixin(FieldHandlerMixin):
    """
    Mixin for marking required fields with an indicator in their label.
    The 'required_indicator' specifies the text (e.g., '*') to prepend to required field labels.
    """

    required_indicator = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mark_required_fields()

    def mark_required_fields(self):
        for field_name, field in self.fields.items():
            if field.required:
                if field.label:
                    field.label = mark_safe(f"{self.required_indicator} {field.label}")
