from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(' ',
    # Examples:
    #url(r'^$', 'Mysite.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),
    #url(r'^latestnews/',include('Blog.urls')),
                       
#url include in the site
    url(r'^$', include('Blog.urls')),
    url(r'^Blog/', include('Blog.urls')),
    url(r'^Admin/',include(admin.site.urls)),




)
