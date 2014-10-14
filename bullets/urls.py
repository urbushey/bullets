from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bullets.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'bullet_app.views.home_page', name='home'),
    url(r'^bullets/', include('bullet_app.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)
