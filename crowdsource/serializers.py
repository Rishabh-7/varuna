from rest_framework import serializers
from . models import EmbData

class EmbDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmbData
        # print("hello")
        # fields = ['lat','lon']
        fields = '__all__'
