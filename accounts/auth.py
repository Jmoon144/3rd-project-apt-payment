from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from indent_corp.models import HouseHold

class BaseAuthKeyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_key = request.META.get('HTTP_AUTHKEY')
        self.auth_key_validation(auth_key)

        unit, password = auth_key[:4], auth_key[4:]
        self.unit_info_validation(unit)

        house_hold = HouseHold.objects.filter(unit=unit, password=password)

        if not house_hold_instance.exists():
            raise exceptions.AuthenticationFailed('no such users')

        return True

    def auth_key_validation(self, auth_key: str) -> None:
        if not auth_key or len(auth_key) != 8:
            raise exceptions.AuthenticationFailed('invalid auth_key')

        try:
            int(auth_key)
        except ValueError:
            raise exceptions.AuthenticationFailed('invalid character in auth_key')

class AdminUserAuthentication(
    def unit_info_validation(self, unit) -> None:
        if unit != '0000':
            raise exceptions.AuthenticationFailed('not admin user')

    def get_house_hold_queryset(self):
        return HouseHold.objects.filter(is_admin=True)

class HouseHoldAuthentication(BaseAuthKeyAuthentication):
    def unit_info_validation(self, unit) -> None:
        if unit == '0000':
            raise exceptions.AuthenticationFailed('not household user')
