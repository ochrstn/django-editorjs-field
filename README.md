django-editorjs-field
===============

This module integrates the [Editor.js](https://github.com/codex-team/editor.js) widget into model/form fields for [Django](https://www.djangoproject.com).
-------------------------------------

## Warning

This is an early prototyp and work in progress

## Installation

Install with Pip:  
```pip install django-editorjs-field```

## Django Setup

### settings.py

```python
INSTALLED_APPS = [
    ...
    'editorjs_field',
    ...
]
```

## Use in Django admin

### models.py

```python
from django.db import models
from editorjs_field.fields import EditorJSField


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = EditorJSField()
```

### admin.py

```python
from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Article, ArticleAdmin)
```

## Use the widget in a custom form

### forms.py

```python
from django import forms
from editorjs_field.widgets import EditorJsWidget

class ArticleEditorForm(forms.Form):
    title = forms.CharField(label='Title')
    document = forms.CharField(label='Document', widget=EditorJsWidget)
````

## Examples & Development

An example can be found in the example folder. To run them clone the repository and run:

```shell
$ cd django-editorjs-field
$ pipenv install
$ pipenv shell
$ cd example
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

Visit ```http://localhost:8000/admin``` to view the admin widget and 
```http://localhost:8000/``` to view the custom form widget.