from abc import ABC, abstractmethod

from spend.models import SpendStatistic


class SpendRepositoryAndServiceInterface(ABC):
    @abstractmethod
    def get_all_spends(self) -> SpendStatistic:
        pass

    @abstractmethod
    def sort_by_date_and_name(self, spends: SpendStatistic) -> dict:
        pass

    @abstractmethod
    def sort_by_date(self, spends: SpendStatistic) -> dict:
        pass

    @abstractmethod
    def sort_by_name(self, spends: SpendStatistic) -> dict:
        pass
