from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework_extensions.mixins import DetailSerializerMixin

from apps.farm_one.models import FarmOne
from apps.farm_one.serializers.farmone import FarmOneSerializer, GetFarmOneSerializer, PostFarmOneSerializer, \
    PutFarmOneSerializer, PatchFarmOneSerializer, ListFarmOneSerializer
from utils.mixin import StandardResultsSetPagination


class FarmOneViewSet(DetailSerializerMixin, viewsets.ModelViewSet):
    queryset = FarmOne.objects.all()
    max_paginate_by = 100
    serializer_class = FarmOneSerializer
    pagination_class = StandardResultsSetPagination
    # permission_classes = (IsAuthenticated,)
    #
    # def get_queryset(self):
    #     return Student.objects
    # @extend_schema(
    #     request=StudentSerializer,
    #     responses={201: StudentSerializer,
    #                200: StudentSerializer},
    # )
    def create(self, request):
        # your non-standard behaviour
        return super().create(request)

    def get_serializer_class(self):
        if self.action == 'list':
            return ListFarmOneSerializer
        elif self.action == 'retrieve':
            return GetFarmOneSerializer
        elif self.action == 'create':
            return PostFarmOneSerializer
        elif self.action == 'update':
            return PutFarmOneSerializer
        elif self.action == 'partial_update':
            return PatchFarmOneSerializer
        # elif self.action == 'destroy':
        #     return StudentSerializer
        else:
            return FarmOneSerializer


#
# `    def create(self, request):
#         # your non-standard behaviour
#         return super().create(request)