from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import base64
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class LoginApiView(APIView):
    authentication_classes=[]
    permission_classes = []

    def post(self, request):
        try:
            auth_header = request.META["HTTP_AUTHORIZATION"].split(" ")[1]
            decoded_data = base64.b64decode(auth_header).decode("utf-8")
            decoded_value = decoded_data.split(":")
            username1 = decoded_value[0]
            password1 = decoded_value[1]
            print(decoded_value)
            
            user = authenticate(request, username= username1, password =password1)
            if user is not None:
                token, created= Token.objects.get_or_create(user = user)
                message={
                    "token": token.key,
                    "user_id": user.pk,
                    "email": user.email,
                    "username" : user.username,
                    }
                return Response(message, status=status.HTTP_200_OK)

            message = {
                "response": "No such user!"
            }
            return Response (message, status=status.HTTP_404_NOT_FOUND)
        except Exception as exe:
            message = {"response": "Something erro!"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
