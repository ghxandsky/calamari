from django.conf.urls import patterns, include, url

from settings import STATIC_DOC_ROOT

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'calamari.views.home'),

    url(r'^api/v1/', include('ceph.urls')),
    url(r'^api/v1/auth/login', 'calamari.views.login'),
    url(r'^api/v1/auth/logout', 'calamari.views.logout'),
    url(r'^api/v1/auth2/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/info', 'calamari.views.info'),

    url(r'^admin/(?P<path>.*)$', 'calamari.views.serve_dir_or_index',
        {'document_root': '%s/admin/' % STATIC_DOC_ROOT}),

    url(r'^login/$', 'django.views.static.serve',
        {'document_root': '%s/login/' % STATIC_DOC_ROOT, 'path': "index.html"}),

    url(r'^login/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '%s/login/' % STATIC_DOC_ROOT}),

    url(r'^dashboard/(?P<path>.*)$', 'calamari.views.dashboard',
        {'document_root': '%s/dashboard/' % STATIC_DOC_ROOT},
        name='dashboard'),

    url(r'^render/?', include('graphite.render.urls')),
    url(r'^metrics/?', include('graphite.metrics.urls')),

)
