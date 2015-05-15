from django.conf.urls import patterns, include, url
from django.contrib import admin
from bookings.views import HomeView, GalleryView, AboutView, TestimonyView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pavone.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^gallery/', GalleryView.as_view(), name='gallery'),
    url(r'^about/', AboutView.as_view(), name='about'),
    url(r'^testimony/', TestimonyView.as_view(), name='testimony'),
    url(r'^admin/', include(admin.site.urls)),
)