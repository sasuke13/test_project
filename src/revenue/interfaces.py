from abc import ABC, abstractmethod

from revenue.models import RevenueStatistic


class RevenueRepositoryAndServiceInterface(ABC):
    @abstractmethod
    def get_all_revenues(self) -> RevenueStatistic:
        pass

    @abstractmethod
    def sort_by_date_and_name(self, revenues: RevenueStatistic) -> dict:
        pass

    @abstractmethod
    def sort_by_date(self, revenues: RevenueStatistic) -> dict:
        pass

    @abstractmethod
    def sort_by_name(self, revenues: RevenueStatistic) -> dict:
        pass
