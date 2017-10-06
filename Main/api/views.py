from rest_framework.generics  import ListAPIView

from Main.models import Event

class EventListApiView(ListAPIView):
    queryset = Event.objects.all()

