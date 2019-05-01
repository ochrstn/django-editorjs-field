from django.forms import widgets
from django.template.loader import render_to_string


class EditorJsWidget(widgets.TextInput):
    class Media:
        js = (
            'editorjs/editor.js',
            'editorjs/header.js',
            'editorjs/checklist.js',
            'editorjs_field.js',
        )
        css = {'all': ('editorjs_field.css', )}

    def __init__(self, *args, **kwargs):
        super(EditorJsWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, **kwargs):
        ctx = {
            'name': name,
            'id': kwargs['attrs']['id'],
            'value': value
        }

        return render_to_string('editorjs_widget.tpl', ctx)
