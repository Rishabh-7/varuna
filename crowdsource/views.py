from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import EmbData
from . serializers import EmbDataSerializer

def index(request):
    return HttpResponse("Crowdsource pe aa gaye.")

class EmbDataList(APIView):

    def get(self,request):
        embarks = EmbData.objects.all()
        # print(type(embarks[0]));

        serializer = EmbDataSerializer(embarks, many=True)
        # print(serializer.data)
        return Response(serializer.data)

    def post(self):
        pass