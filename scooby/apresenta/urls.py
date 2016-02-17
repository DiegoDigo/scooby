from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'scooby.apresenta.views.index',name="home")
]
