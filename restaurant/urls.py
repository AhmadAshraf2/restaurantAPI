from django.conf.urls import url
from . import views

'''
routing rules for urls begining with /restaurant/...
'''
urlpatterns = [
    url(r'^view/$', views.ViewAllRestaurant.as_view()),

    url(r'^view/(?P<pk>[0-9]+)/$', views.ViewRestaurant.as_view(), name='view_restaurant'),

    url(r'^delete/(?P<pk>[0-9]+)/$', views.DeleteRestaurant.as_view(), name='delete_restaurant'),

    url(r'^update/(?P<pk>[0-9]+)/$', views.UpdateRestaurant.as_view(), name='update_restaurant'),

    url(r'^create/$', views.CreateRestaurant.as_view(), name='create_restaurant'),
]
