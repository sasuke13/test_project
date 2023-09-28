from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from config.serializers import RevenueDTOSerializer
from config.base_api import ApiBaseView
from config.containers import RevenueContainer


class SortRevenueByDateAndNameAPIView(APIView, ApiBaseView):
    def get(self, request):
        revenue_interactor = RevenueContainer.interactor()

        data = revenue_interactor.sort_by_date_and_name()

        if data:
            self._serialize_nested_dict(data, RevenueDTOSerializer)
        else:
            data = "There is no any revenue yet"

        return Response({"response": data}, status=status.HTTP_200_OK)


class SortRevenueByDateAPIView(APIView, ApiBaseView):
    def get(self, request):
        revenue_interactor = RevenueContainer.interactor()

        data = revenue_interactor.sort_by_date()

        if data:
            self._serialize_dict(data, RevenueDTOSerializer)
        else:
            data = "There is no any revenue yet"

        return Response({"response": data}, status=status.HTTP_200_OK)


class SortRevenueByNameAPIView(APIView, ApiBaseView):
    def get(self, request):
        revenue_interactor = RevenueContainer.interactor()

        data = revenue_interactor.sort_by_name()

        if data:
            self._serialize_dict(data, RevenueDTOSerializer)
        else:
            data = "There is no any revenue yet"

        return Response({"response": data}, status=status.HTTP_200_OK)
