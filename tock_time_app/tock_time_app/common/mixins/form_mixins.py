class FieldHandlerMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for method_name in ['remove_help_text', 'set_placeholders']:
            method = getattr(self, method_name, None)
            if callable(method):
                method()

    def set_field_attribute(self, field_names, attribute, value):
        for field_name in field_names:
            if field_name in self.fields:
                setattr(self.fields[field_name], attribute, value)

    def update_widget_attrs(self, field_names, attribute, value):
        for field_name in field_names:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs.update({attribute: value})


class PlaceholderMixin(FieldHandlerMixin):
    placeholder_fields = {}

    def set_placeholders(self):
        for field_name, placeholder_text in self.placeholder_fields.items():
            if field_name in self.fields:
                self.fields[field_name].widget.attrs.update({'placeholder': placeholder_text})


class NoHelpTextMixin(FieldHandlerMixin):
    help_text_fields = []

    def remove_help_text(self):
        self.set_field_attribute(self.help_text_fields, 'help_text', None)
