from django.conf.urls import url
from . import views

app_name = 'polls'

urlpatterns = [
    # url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^form/$', views.form, name='form'),
    # url(r'^logon/$', views.logon, name='logon'),
    # url(r'^contact/$', views.contactView, name='contact'),
    # url(r'^index1/$', views.index1, name='index1'),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    #
    # # Start DJANGO BOOK models!!!
    # # Start DJANGO BOOK models!!!
    # # Start DJANGO BOOK models!!!
    # url(r'^articles/(\d{4})/$', views.year_archive),
    # url(r'^articles/(\d{4})/(\d{2})/$', views.month_archive),
    # # url(r'^articles/(\d{4})/(\d{2})/(\d+)$', views.article_detail),
]


