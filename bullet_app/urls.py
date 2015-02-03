from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bullets.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'bullet_app.views.home_page', name='home'),
    url(r'^(\d+)/$', 'bullet_app.views.view_bullets', name='view_bullets'),
    url(r'^new$', 'bullet_app.views.new_bullet_group',name='new_bullet_group'),

)
