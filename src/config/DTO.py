from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List


@dataclass(frozen=True)
class RevenueWithoutSpendDTO:
    name: str
    date: datetime
    revenue: float


@dataclass(frozen=True)
class SpendDTO:
    name: str
    date: datetime
    spend: float
    impressions: int
    clicks: int
    conversion: int
    revenue: List[RevenueWithoutSpendDTO] | None


@dataclass(frozen=True)
class SpendWithoutRevenueDTO:
    name: Optional[str]
    date: Optional[datetime]
    spend: Optional[float]
    impressions: Optional[int]
    clicks: Optional[int]
    conversion: Optional[int]


@dataclass(frozen=True)
class RevenueDTO:
    name: str
    spend: SpendWithoutRevenueDTO | None
    date: datetime
    revenue: float
