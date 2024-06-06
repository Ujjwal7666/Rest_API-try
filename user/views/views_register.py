from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.serializer1 import UserSerializer
from django.contrib.auth.models import User

class RegisterApiview(APIView):
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                message ={
                    "response": "User succesfully create"
                }
                return Response(message, status=status.HTTP_201_CREATED)
            
            message={
                "response": serializer.errors
            }
            return Response (message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        except Exception as exe:
            message={"response": "something erros occrs"}
            return Response(message, status= status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
            try :
                user = User.objects.filter(is_active=True) #extract data save in models or database
                serializer = UserSerializer(user, many= True) # show all
                message = { 
                    "response": "Datat found successfully",
                    "Data" : serializer.data
                        }
                return Response( message , status= status.HTTP_200_OK ) 
            except Exception as exe:
                message={
                    "response": "Cannot found the data"
            }
            return Response( message, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class RegisterUpdateApiView(APIView):
     def put (self, request, pk):
          try:
                instance = User.objects.get(id=pk)
                serializer = UserSerializer(instance, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    message ={"response": "Data updated successfuly"}
                    return Response(message, status=status.HTTP_200_OK)
               
                message = {"response ": serializer.errors}
                return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
          except Exception as exe:
                message = {"response ": "Ops Sorry soemthing error"}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)

