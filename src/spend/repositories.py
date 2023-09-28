from config.DTO import SpendDTO
from config.base_repositori import BaseTestRepository
from spend.interfaces import SpendRepositoryAndServiceInterface
from spend.models import SpendStatistic


class SpendRepository(BaseTestRepository, SpendRepositoryAndServiceInterface):
    def get_all_spends(self) -> SpendStatistic:
        return SpendStatistic.objects.prefetch_related('revenue').all()

    def sort_by_date_and_name(self, spends: SpendStatistic) -> dict:
        divided_revenue_dict = {}
        spends = spends.order_by('date')

        self._sort_by_date_and_name(spends, divided_revenue_dict, SpendDTO)

        return divided_revenue_dict

    def sort_by_date(self, spends: SpendStatistic) -> dict:
        divided_spends_dict = {}

        spends = spends.order_by('date')

        self._sort_by_date(spends, divided_spends_dict, SpendDTO)

        return divided_spends_dict

    def sort_by_name(self, spends: SpendStatistic) -> dict:
        divided_spends_dict = {}

        spends = spends.order_by('name')

        self._sort_by_name(spends, divided_spends_dict, SpendDTO)

        return divided_spends_dict
