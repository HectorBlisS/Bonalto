from django.conf.urls import url
from . import views


urlpatterns=[
	url(r'^$',
		views.Home.as_view(),
		name="home"),

	url(r'^index/$',
		views.Indexar.as_view(),
		name="index"),

]