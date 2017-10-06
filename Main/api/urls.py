from django.conf.urls  import url



from .views import (
    EventListApiView
)



urlpatterns = [
    url(r'^$', EventListApiView.as_view(), name='list'),
]