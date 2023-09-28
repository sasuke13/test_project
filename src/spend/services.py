from spend.interfaces import SpendRepositoryAndServiceInterface
from spend.models import SpendStatistic


class SpendService(SpendRepositoryAndServiceInterface):
    def __init__(self, spend_repository: SpendRepositoryAndServiceInterface):
        self.spend_repository = spend_repository

    def get_all_spends(self) -> SpendStatistic:
        return self.spend_repository.get_all_spends()

    def sort_by_date_and_name(self, spends: SpendStatistic) -> dict:
        return self.spend_repository.sort_by_date_and_name(spends)

    def sort_by_date(self, spends: SpendStatistic) -> dict:
        return self.spend_repository.sort_by_date(spends)

    def sort_by_name(self, spends: SpendStatistic) -> dict:
        return self.spend_repository.sort_by_name(spends)
