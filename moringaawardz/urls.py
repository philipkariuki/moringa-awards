from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^new/project$', views.new_project, name='new-project'),
    url(r'^project/(\d+)',views.project, name='project'),
    url(r'^profile/',views.profile,name ='profile'),
    url(r'^profile_update/',views.profile_update,name='profile_update'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new_comment/', views.new_comment, name='new_comment'),
]



if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)