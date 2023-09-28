from revenue.interfaces import RevenueRepositoryAndServiceInterface
from revenue.models import RevenueStatistic


class RevenueService(RevenueRepositoryAndServiceInterface):
    def __init__(self, revenue_repository: RevenueRepositoryAndServiceInterface):
        self.revenue_repository = revenue_repository

    def sort_by_date_and_name(self, revenues: RevenueStatistic) -> dict:
        return self.revenue_repository.sort_by_date_and_name(revenues)

    def get_all_revenues(self) -> RevenueStatistic:
        return self.revenue_repository.get_all_revenues()

    def sort_by_date(self, revenues: RevenueStatistic) -> dict:
        return self.revenue_repository.sort_by_date(revenues)

    def sort_by_name(self, revenues: RevenueStatistic) -> dict:
        return self.revenue_repository.sort_by_name(revenues)
