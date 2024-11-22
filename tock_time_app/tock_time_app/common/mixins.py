from django.db import models


class DescriptionMixin(models.Model):
    description = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class CreatedAtMixin(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
    )

    class Meta:
        abstract = True


class FieldHandlerMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for method_name in ['make_fields_readonly', 'make_fields_disabled', 'remove_help_text']:
            method = getattr(self, method_name, None)
            if callable(method):
                method()

    def set_field_attribute(self, field_names, attribute, value):
        for field_name in field_names:
            if field_name in self.fields:
                if attribute == 'readonly':
                    self.fields[field_name].widget.attrs['readonly'] = value
                elif attribute == 'disabled':
                    self.fields[field_name].disabled = value
                elif attribute == 'help_text':
                    self.fields[field_name].help_text = None if value is None else value


class DisabledFieldMixin(FieldHandlerMixin):
    disabled_field = []

    def make_fields_disabled(self):
        self.set_field_attribute(self.disabled_field, 'disabled', True)


class NoHelpTextMixin(FieldHandlerMixin):
    help_text_fields = []

    def remove_help_text(self):
        self.set_field_attribute(self.help_text_fields, 'help_text', None)