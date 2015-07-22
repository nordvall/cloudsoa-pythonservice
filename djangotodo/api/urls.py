from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from views import ToDoList, ToDoDetail

urlpatterns = [
    url(r'^todo/$', ToDoList.as_view()),
    url(r'^todo/(?P<pk>[0-9]+)/$', ToDoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
