from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.year_archive),
    url(r'^$', views.mark_list),
]
