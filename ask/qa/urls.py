from django.conf.urls import url
from qa.views import test
from qa.views import main

urlpatterns = [
    url(r'^$', main),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^question/(?P<ID>\d+)/', test, name='questions'),
    url(r'^ask/', test),
    url(r'^popular/', test),
    url(r'^new/', test)
]
