from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls import include

urlpatterns = [

    path('', views.index, name='Index'),

    path('contact/', include(('contact.urls', 'contact'), namespace='contact')),

    path('<question_id>', views.detail, name='detail'),

    path('', views.index, name="index"),

    url('(?P<question_id>[0-9]+)/detail$', views.detail, name="detail"),

    url('(?P<question_id>[0-9]+)/results$', views.results, name="results"),

    url('(?P<question_id>[0-9]+)/vote$', views.vote, name="vote"),

]