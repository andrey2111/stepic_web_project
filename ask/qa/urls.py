from django.conf.urls import url
from qa.views import test, main, popular, question

urlpatterns = [
    url(r'^$', main),
    url(r'^popular/', popular),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^question/(?P<id>\d+)/', question),
    url(r'^ask/', test),
    url(r'^new/', test)
]
