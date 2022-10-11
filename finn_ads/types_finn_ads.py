from typing import TypedDict


class FinnAd(TypedDict):
    ad_id: int
    ad_type: str
    ad_price: float


class AnalyzedType(TypedDict):
    ad_type: str
    count: int
    duplicates: int
    lowest_value_ad: FinnAd
    highest_value_ad: FinnAd
