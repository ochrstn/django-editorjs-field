from django.conf.urls import url
from .views import SampleFormView


urlpatterns = [
    url('', SampleFormView.as_view(), name='form'),
]
