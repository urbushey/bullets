from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bullets.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'bullet_app.views.home_page', name='home'),
    url(r'^bullets/(\d+)/$',
        'bullet_app.views.view_bullets',
        name='view_bullets'),
    url(r'^bullets/new$',
        'bullet_app.views.new_bullet',
        name='new_bullet'),
    url(r'^bullets/(\d+)/add_bullet$',
        'bullet_app.views.add_bullet',
        name='add_bullet'),
)
