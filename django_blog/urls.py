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
        url(r'^$', 'blog.views.main_page'),
        url(r'^$', 'blog.views.create', name='blog-create'),
    # url(r'^new$', blog.views.CreateContactView.as_view(),
    #     name='contacts-new',),
)

urlpatterns += staticfiles_urlpatterns()
