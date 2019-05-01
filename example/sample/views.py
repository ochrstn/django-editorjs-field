from django.shortcuts import render
from django.views.generic import FormView

from .forms import ArticleEditorForm


class SampleFormView(FormView):
    template_name = 'form.html'
    form_class = ArticleEditorForm
