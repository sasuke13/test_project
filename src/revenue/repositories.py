from config.DTO import RevenueDTO
from config.base_repositori import BaseTestRepository
from revenue.interfaces import RevenueRepositoryAndServiceInterface
from revenue.models import RevenueStatistic


class RevenueRepository(BaseTestRepository, RevenueRepositoryAndServiceInterface):
    def get_all_revenues(self) -> RevenueStatistic:
        revenue = RevenueStatistic.objects.all().select_related('spend')

        return revenue

    def sort_by_date_and_name(self, revenues: RevenueStatistic) -> dict:
        divided_revenue_dict = {}
        revenues = revenues.order_by('date')

        self._sort_by_date_and_name(revenues, divided_revenue_dict, RevenueDTO)

        return divided_revenue_dict

    def sort_by_date(self, revenues: RevenueStatistic) -> dict:
        divided_revenue_dict = {}
        revenues = revenues.order_by('date')

        self._sort_by_date(revenues, divided_revenue_dict, RevenueDTO)

        return divided_revenue_dict

    def sort_by_name(self, revenues: RevenueStatistic) -> dict:
        divided_revenue_dict = {}
        revenues = revenues.order_by('name')

        self._sort_by_name(revenues, divided_revenue_dict, RevenueDTO)

        return divided_revenue_dict
