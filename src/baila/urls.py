from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'baila.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'content_manager.views.home', name='home'),
    url(r'^about/$', 'content_manager.views.about', name='about'),
    url(r'^art/$', 'content_manager.views.art', name='art'),
    

    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<slug>[\w-]+)/$', 'content_manager.views.memoir', name='memoir'),
)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	