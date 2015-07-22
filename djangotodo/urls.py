from django.conf.urls import include, url
from api.urls import urlpatterns as api_urls

urlpatterns = [
    url(r'^api/', include(api_urls, namespace='api')),
]
