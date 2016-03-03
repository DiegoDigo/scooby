from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'scooby.principal.views.index',name='home'),
]
