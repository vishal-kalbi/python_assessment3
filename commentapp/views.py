from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import CommentApp
from .serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class CreateData(APIView):

    def post(self,request):
        ser_obj=CommentSerializer(data=request.data)
        if ser_obj.is_valid():
            ser_obj.save()
            all_user=list(CommentApp.objects.values())
            ser_new_obj=CommentSerializer(all_user,many=True)
            return Response(data=ser_new_obj.data)
        else:
            ser_obj.errors


class GetData(APIView):
     def get(self,request,pk):
        u1=CommentApp.objects.get(id=pk)
        ser_obj=CommentSerializer(u1)
        return Response(ser_obj.data)


class UpdateData(APIView):
    def put(self,request,pk):
        u1=CommentApp.objects.get(id=pk)
        ser_obj=CommentSerializer(u1=request.data)
        if ser_obj.is_valid():
            ser_obj.save()
            all_user=list(CommentApp.objects.values())
            ser_new_obj=CommentSerializer(all_user,many=True)
            return Response(data=ser_new_obj.data)
        else:
            ser_obj.errors    

class DeleteData(APIView):
    def delete(self,request,pk):
        u1=CommentApp.objects.get(id=pk)
        u1.delete()
        all_user=CommentApp.objects.all()
        ser_new_obj=CommentSerializer(all_user,many=True)
        return Response(data=ser_new_obj.data)

class AllData(APIView):
    def get(self,request):
        all_user=CommentApp.objects.all()                       
        ser_new_obj=CommentSerializer(all_user,many=True)
        return Response(data=ser_new_obj.data)