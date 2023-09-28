from django.urls import path

from spend.views import SortSpendByDateAPIView, SortSpendByNameAPIView, SortRevenueByDateAndNameAPIView

urlpatterns = [
    path('sort_by_date_and_name/', SortRevenueByDateAndNameAPIView.as_view(), name='sort_spend_by_date_and_name'),
    path('sort_by_date/', SortSpendByDateAPIView.as_view(), name='sort_spend_by_date'),
    path('sort_by_name/', SortSpendByNameAPIView.as_view(), name='sort_spend_by_name'),
]
