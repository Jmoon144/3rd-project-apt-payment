from rest_framework import generics
from accounts.models import User
from accounts.serializers import UserSerializer

#from indent_corp.auth import HouseHoldAuthentication
#from indent_corp.models import HouseHold, DoorUseLog
#from indent_corp.serializers import HouseHoldSerializer

FEE_PER_COUNT = 1

# custom authentication_classes
from rest_framework.authentication import BaseAuthentication

class PublicUserAuthentication(BaseAuthentication):
    def authenticate(self, request):
        print("++")
        print(f"request : {dir(request)}")
        authentication = request.META.get('HTTP_AUTH', 'default')

        params = request.query_params.get('key')
        print(f"auth : {authentication}")
        print(f"params : {params}")

        return 

class PublicUserDetailView(generics.RetrieveAPIView):
    authentication_classes = [PublicUserAuthentication, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer
