from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from config.serializers import SpendDTOSerializer
from config.base_api import ApiBaseView
from config.containers import SpendContainer


class SortRevenueByDateAndNameAPIView(APIView, ApiBaseView):
    def get(self, request):
        revenue_interactor = SpendContainer.interactor()

        data = revenue_interactor.sort_by_date_and_name()

        if data:
            self._serialize_nested_dict(data, SpendDTOSerializer)
        else:
            data = "There is no any revenue yet"

        return Response(data, status=status.HTTP_200_OK)


class SortSpendByDateAPIView(APIView, ApiBaseView):
    def get(self, request):
        revenue_interactor = SpendContainer.interactor()

        data = revenue_interactor.sort_by_date()

        if data:
            self._serialize_dict(data, SpendDTOSerializer)
        else:
            data = "There is no any spend yet"

        return Response(data, status=status.HTTP_200_OK)


class SortSpendByNameAPIView(APIView, ApiBaseView):
    def get(self, request):
        revenue_interactor = SpendContainer.interactor()

        data = revenue_interactor.sort_by_name()

        if data:
            self._serialize_dict(data, SpendDTOSerializer)
        else:
            data = "There is no any spend yet"

        return Response(data, status=status.HTTP_200_OK)
