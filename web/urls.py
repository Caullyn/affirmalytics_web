from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^web/', TemplateView.as_view(template_name="web/index.html"),
                   name='web'),
]