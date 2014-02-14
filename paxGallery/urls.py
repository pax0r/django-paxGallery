from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import GalleryView, GalleryPhotoView, GalleryHomeView

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', GalleryHomeView.as_view(), name='gallery-home'),
                       url(r'^(?P<id>\d+)/(?P<galleryslug>[-\w]+)/(?P<photoslug>[-\w]+)/$', GalleryPhotoView.as_view(),
                           name='photo-view'),
                       url(r'^(?P<id>\d+)/(?P<galleryslug>[-\w]+)/$', GalleryView.as_view(), name='gallery-view'),
)