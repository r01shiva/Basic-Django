from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [

	path('',views.main,name='main'),

    path('contact/',views.contact,name='contact'),

	path('login/',views.mainin,name='mainin'),

    path('contactlogin/',views.contactin,name='contactin'),

	path('signin/',views.signin,name='signin'),

    url(r'^register/$',views.UserFormView.as_view(),name='register'),

 	url(r'^product/$',views.IndexView.as_view(),name='index'),

    url(r'^product/add/$',views.SumitProduct.as_view(),name='submit_pro'),

	url(r'^product/(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),

	url(r'^recycle$', views.RecycleProduct.as_view(), name='recycle_pro'),

	url(r'^recycle/(?P<pk>[0-9]+)/$',views.DetailViewRecycle.as_view(),name='detail_recycle'),

	url(r'^login_user/$', views.login_user, name='login_user'),

    url(r'^logout_user/$', views.logout_user, name='logout_user'),

	url(r'^buynow/$', views.buynow, name='buynow'),
	]
