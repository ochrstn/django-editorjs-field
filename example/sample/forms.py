from django import forms
from editorjs_field.widgets import EditorJsWidget


class ArticleEditorForm(forms.Form):
    title = forms.CharField(label='Title')
    document = forms.CharField(label='Document', widget=EditorJsWidget)
