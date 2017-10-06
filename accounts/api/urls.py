from django.conf.urls import url
from .views import UserCreateApiView, UserLoginApiView

    

urlpatterns = [
	url(r'^login/$',UserLoginApiView.as_view(), name='login'),
	 url(r'^register/$', UserCreateApiView.as_view(),name='register')
]

