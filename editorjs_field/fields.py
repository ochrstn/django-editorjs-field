from django.db.models import Field
from urllib.parse import unquote

from editorjs_field.widgets import EditorJsWidget


class EditorJSField(Field):
    def __init__(self, *args, **kwargs):
        super(EditorJSField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return 'TextField'

    def clean(self, value, model_instance):
        if value is not None:
            return unquote(super(EditorJSField, self).clean(value, model_instance))
        else:
            return None

    def formfield(self, *args, **kwargs):
        kwargs['widget'] = EditorJsWidget()
        return super(EditorJSField, self).formfield(*args, **kwargs)
