from spend.interfaces import SpendRepositoryAndServiceInterface
from spend.models import SpendStatistic


class SpendInteractor:
    def __init__(self, spend_service: SpendRepositoryAndServiceInterface):
        self.spend_service = spend_service

    def get_all_spends(self) -> SpendStatistic:
        return self.spend_service.get_all_spends()

    def sort_by_date_and_name(self) -> dict:
        spends = self.spend_service.get_all_spends()

        return self.spend_service.sort_by_date_and_name(spends)

    def sort_by_date(self) -> dict:
        spends = self.spend_service.get_all_spends()

        return self.spend_service.sort_by_date(spends)

    def sort_by_name(self) -> dict:
        spends = self.spend_service.get_all_spends()

        return self.spend_service.sort_by_name(spends)
