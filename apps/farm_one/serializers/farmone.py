from rest_framework import serializers

from apps.farm_one.models import FarmOne


class FarmOneSerializer(serializers.ModelSerializer):
    """
    Farm One Serializer
    """
    class Meta:
        model = FarmOne
        fields = '__all__'
        # read_only_fields = ('id', 'created_at', 'updated_at', 'user')

class GetFarmOneSerializer(serializers.ModelSerializer):
    """
    Farm One Serializer
    """
    class Meta:
        model = FarmOne
        exclude = ('created_at',)

class PostFarmOneSerializer(GetFarmOneSerializer):
    pass

class PutFarmOneSerializer(GetFarmOneSerializer):
    pass

class PatchFarmOneSerializer(GetFarmOneSerializer):
    pass

class ListFarmOneSerializer(GetFarmOneSerializer):
    class Meta:
        model = FarmOne
        fields = ('id', 'ph', 'temperature', 'humidity')