from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    
   url(r'^$', 'mysite1.views.home', name='home'),
   url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
