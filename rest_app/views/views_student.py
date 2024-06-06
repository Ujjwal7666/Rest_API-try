from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_app.models import Student
from rest_app.serializer import StudentSerializer
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_app import globalmessage

class StudentListApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try: 
            student = Student.objects.filter(is_delete= False)
            serializer = StudentSerializer(student, many=True)
            message = {
                    globalmessage.RESPONSE_KEY: "Data retrerive",
                    "data": serializer.data
                }
            return Response(message, status=200)
        except Exception as exe:
            message= {

            }
            return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class StudentCreateApiView(APIView):   
    def post(self, request):
        try:
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                message = {
                    "response": "Data successfully save",
                }
                return Response(message, status=200)
            message = {"response": serializer.errors}
            return Response(message, status=400)
        except Exception as exe:
            message ={"response":"OPs somthing is error"}
            return Response()
        
#to update best practice is patch, put but can also done by post

class StudentUpdateApiView(APIView):   
    def put(self, request, pk):
        try:
            instance = Student.objects.get(id=pk, is_delete = False)
            serializer = StudentSerializer(instance ,data=request.data)
            if serializer.is_valid():
                serializer.save()
                message = {
                    "response": "Data successfully updated",
                }
                return Response(message, status=200)
            message = {"response": serializer.errors}
            return Response(message, status=400)
        except Student.DoesNotExist as exe:
            message={"response": "No such result in the database"}
            return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as exe:
        
            message ={"response":"OPs somthing is error"}
            return Response(message)
        
class StudentDeleteApiView(APIView):   
    def delete(self, request, pk):
        try:
            instance = Student.objects.get(id=pk, is_delete = False)
            instance.is_delete = True
            instance.save()
            message = {
                    "response": "Data successfully deleted",
                }
            return Response(message, status=200)
            
        except Student.DoesNotExist as exe:
            message={"response": "No such result in the database"}
            return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as exe:
            message ={"response":"OPs somthing is error"}
            return Response(message)
        