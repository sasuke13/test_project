from django.urls import path

from revenue.views import SortRevenueByDateAPIView, SortRevenueByNameAPIView, SortRevenueByDateAndNameAPIView

urlpatterns = [
    path("sort_by_date_and_name/", SortRevenueByDateAndNameAPIView.as_view(), name="sort_revenue_by_date_and_name"),
    path("sort_by_date/", SortRevenueByDateAPIView.as_view(), name="sort_revenue_by_date"),
    path("sort_by_name/", SortRevenueByNameAPIView.as_view(), name="sort_revenue_by_name")
]
