from dependency_injector import containers, providers

from revenue.interactors import RevenueInteractor
from revenue.repositories import RevenueRepository
from revenue.services import RevenueService
from spend.interactors import SpendInteractor
from spend.repositories import SpendRepository
from spend.services import SpendService


class RepositoryContainer(containers.Container):
    revenue_repository = providers.Factory(
        RevenueRepository
    )

    spend_repository = providers.Factory(
        SpendRepository
    )


class ServiceContainers(containers.Container):
    revenue_service = providers.Factory(
        RevenueService,
        revenue_repository=RepositoryContainer.revenue_repository
    )

    spend_service = providers.Factory(
        SpendService,
        spend_repository=RepositoryContainer.spend_repository
    )


class InteractorContainers(containers.Container):
    revenue_interactor = providers.Factory(
        RevenueInteractor,
        revenue_service=ServiceContainers.revenue_service
    )

    spend_interactor = providers.Factory(
        SpendInteractor,
        spend_service=ServiceContainers.spend_service
    )


class RevenueContainer(containers.Container):
    repository = RepositoryContainer.revenue_repository
    service = ServiceContainers.revenue_service
    interactor = InteractorContainers.revenue_interactor


class SpendContainer(containers.Container):
    repository = RepositoryContainer.spend_repository
    service = ServiceContainers.spend_service
    interactor = InteractorContainers.spend_interactor
