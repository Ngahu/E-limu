from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework.views import APIView



from rest_framework.generics import (
        CreateAPIView,
        ListAPIView ,
        RetrieveAPIView,
        UpdateAPIView,
        DestroyAPIView,
        RetrieveUpdateAPIView
        )

from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
    )


User = get_user_model()



from .serializers import (
        UserCreateSerializer,
        UserLoginSerializer
        )

########end of imports ###################


class UserCreateApiView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset =  User.objects.all()
    permission_classes = [AllowAny]



class UserLoginApiView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request,*args,**kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data =serializer.data
            return Response(new_data, status=HTTP_200_OK)  #A django_rest framwerok response and not a regular django response
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
