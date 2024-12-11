from django.utils.html import format_html


class FieldHandlerMixin:
    """Base mixin providing utility methods for manipulating form fields and their attributes."""
    def set_field_attribute(self, field_names, attribute, value):
        """ Sets a specified attribute for the given fields. """

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
        """ Adds placeholders to the fields defined in 'placeholder_fields'. """

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
        """ Removes the help text from the fields defined in 'help_text_fields'. """

        self.set_field_attribute(self.help_text_fields, 'help_text', None)


class MarkRequiredFieldsMixin(FieldHandlerMixin):
    """
    Mixin for marking required fields with an indicator in their label.
    The 'required_indicator' specifies the text (e.g., '*') to prepend to required field labels.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mark_required_fields()

    def mark_required_fields(self):
        """ Adds the 'required_indicator' to the labels of required fields. """

        for field_name, field in self.fields.items():
            if field.required and field.label:
                field.label = format_html('<span class="required-label">{}</span>', field.label)
                current_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f"{current_classes} required".strip()
