from django.conf.urls import url
from views import test, main, popular, question, ask, answer, signup, signin

urlpatterns = [
    url(r'^$', main),
    url(r'^popular/', popular),
    url(r'^login/', signin),
    url(r'^signup/', signup),
    url(r'^question/(?P<id>\d+)/', question),
    url(r'^ask/', ask),
    url(r'^new/', test),
    url(r'answer/', answer),
]
