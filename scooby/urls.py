from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'scooby.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^',include('scooby.apresenta.urls',namespace="apresenta")),
    url(r'^acessar/',include('scooby.conta.urls',namespace='conta')),
    url(r'^admin/', include(admin.site.urls)),
]
