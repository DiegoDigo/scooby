from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'scooby.apresenta.views.index',name="apresenta"),
    url(r'^marca/$', 'scooby.apresenta.views.marca',name="marca"),

]
