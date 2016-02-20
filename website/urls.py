from django.conf.urls import include, url
from website import views

urlpatterns = [
    url(r'^$', 'website.views.index', name='index'),
]
