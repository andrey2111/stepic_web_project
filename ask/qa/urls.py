from django.conf.urls import url
from views import test, main, popular, question, ask, answer

urlpatterns = [
    url(r'^$', main),
    url(r'^popular/', popular),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^question/(?P<id>\d+)/', question),
    url(r'^ask/', ask),
    url(r'^new/', test),
    url(r'answer/', answer),
]
