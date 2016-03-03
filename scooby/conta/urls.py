from django.conf.urls import include, url


urlpatterns = [
    url(r'^login/$','django.contrib.auth.views.login',{'template_name':'conta/index.html'},name='login'),
    url(r'^logout/$','django.contrib.auth.views.logout',{'next_page':'apresenta:apresenta'},name='logout'),
]
