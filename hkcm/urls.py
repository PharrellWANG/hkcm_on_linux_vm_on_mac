from django.conf.urls import urlfrom django.contrib.staticfiles.urls import staticfiles_urlpatternsfrom django.views.generic import RedirectViewfrom django.views.generic import TemplateViewfrom . import viewsurlpatterns = [    # url(r'^$', views.index, name='index'),    url(r'^$', views.map_page, name='map')]# urlpatterns += staticfiles_urlpatterns()# urlpatterns += [#     url(r'.*$', RedirectView.as_view(url='/hkcm/', permanent=True)),# ]