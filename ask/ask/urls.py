from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('qa.views',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'main'),
    url(r'^popular/.*$', 'popular'),
    url(r'^question/(\d+)/$', 'question_detail'),
    url(r'^login/.*$','test'),
    url(r'^signup/.*$','test'),
    url(r'^question/\d+/.*$','test'),
    url(r'^ask/.*$', 'test'),
    url(r'^popular/.*$', 'test'),
    url(r'^new/.*$', 'test'),
    #url(r'^admin/', include(admin.site.urls)),
)
