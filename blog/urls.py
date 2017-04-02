from django.conf.urls import url

from . import views
urlpatterns = [
    #url(r'^$', views.functiaInBlog, name='index'),
url(r'^$', views.post_list, name='post_list'),
]