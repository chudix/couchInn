from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^ask/(?P<lodgment_id>[0-9]+)/$', views.ask, name='ask'),
]

