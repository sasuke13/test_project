from revenue.interfaces import RevenueRepositoryAndServiceInterface
from revenue.models import RevenueStatistic


class RevenueInteractor:
    def __init__(self, revenue_service: RevenueRepositoryAndServiceInterface):
        self.revenue_service = revenue_service

    def get_all_revenues(self) -> RevenueStatistic:
        return self.revenue_service.get_all_revenues()

    def sort_by_date_and_name(self) -> dict:
        revenues = self.revenue_service.get_all_revenues()

        return self.revenue_service.sort_by_date_and_name(revenues)

    def sort_by_date(self) -> dict:
        revenues = self.revenue_service.get_all_revenues()

        return self.revenue_service.sort_by_date(revenues)

    def sort_by_name(self) -> dict:
        revenues = self.revenue_service.get_all_revenues()

        return self.revenue_service.sort_by_name(revenues)
