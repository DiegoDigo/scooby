from django.conf.urls import include, url


urlpatterns = [
    url(r'^login/$','django.contrib.auth.views.login',{'template_name':'conta/index.html'},name='login'),
]
