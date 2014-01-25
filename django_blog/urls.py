from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_blog.views.home', name='home'),
    # url(r'^django_blog/', include('django_blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^$', contacts.views.ListContactView.as_view(),
    #     name='contacts-list',),
    # url(r'^new$', contacts.views.CreateContactView.as_view(),
    #     name='contacts-new',),
        url(r'^$', 'blog.views.index'),
        url(r'^blog/$', 'blog.views.index'),
        url(r'^blog/new$', 'blog.views.new', name='blog-new'),
        url(r'^blog/create', 'blog.views.create'),
        url(r'^blog/(?P<id>\w+)/', 'blog.views.show'),
        url(r'^picture/$', 'picture.views.index'),
        url(r'^picture/new$', 'picture.views.new', name='blog-new'),
        url(r'^picture/create', 'picture.views.create'),
        url(r'^picture/(?P<id>\w+)/$', 'picture.views.show'),
        url(r'^picture/(?P<id>\w+)/delete/$', 'picture.views.delete'),
    # url(r'^new$', blog.views.CreateContactView.as_view(),
    #     name='contacts-new',),
)

urlpatterns += staticfiles_urlpatterns()
