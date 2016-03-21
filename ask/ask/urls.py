from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('qa.views',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'main'),
    url(r'^popular/.*$', 'popular'),
    url(r'^signup/.*$', 'register'),
    url(r'^question/(\d+)/$', 'question_detail',name='question'),
    url(r'^login/.*$','mylogin'),
    url(r'^answer/.*$','answer_add'),    
    url(r'^ask/.*$','quest_add'),
    url(r'^popular/.*$', 'test'),
    url(r'^new/.*$', 'test'),
    #url(r'^admin/', include(admin.site.urls)),
)
