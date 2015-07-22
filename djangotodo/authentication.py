from django.contrib.auth.models import User
from rest_framework import exceptions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class DummyUserAuthentication(JSONWebTokenAuthentication):
    """
    Inherits JSONWebTokenAuthentication and bypasses Django database user lookup
    """
    def authenticate_credentials(self, payload):
        user_id = payload.get('unique_name')

        if user_id is not None:
            user = User()
            user.pk = user_id
            user.first_name = payload.get('given_name')
            user.last_name = payload.get('family_name')
            user.email = payload.get('email')
        else:
            raise exceptions.AuthenticationFailed('No userid claim found.')

        return user
