from django.db import models
from editorjs_field.fields import EditorJSField


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = EditorJSField()
