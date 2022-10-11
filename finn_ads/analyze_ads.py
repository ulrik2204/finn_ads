from finn_ads.types_finn_ads import AnalyzedType, FinnAd


def _categorize_ads(ads: list[FinnAd]) -> dict[str, list[FinnAd]]:
    dic: dict[str, list[FinnAd]] = dict()
    for ad in ads:
        typ = ad["ad_type"]
        if typ in dic:
            dic[typ].append(ad)
        else:
            dic[typ] = [ad]
    return dic


def analyze_ads(ads: list[FinnAd]) -> dict[str, AnalyzedType]:
    analyzed_types: dict[str, AnalyzedType] = dict()
    categorized_ads = _categorize_ads(ads)
    for category in categorized_ads:
        checked_ids: list[str] = []
        # lowest_value_ad: FinnAd = {"ad_id": 0, "ad_price": inf, "ad_type": "x"}
        # highest_value_ad: FinnAd = {"ad_id": 0, "ad_price": 0, "ad_type": "x"}
        for ad in categorized_ads[category]:
            ad_type = ad["ad_type"]
            ad_id = ad["ad_id"]
            ad_price = ad["ad_price"]
            if ad_type not in analyzed_types:
                analyzed_types[ad_type] = {
                    "ad_type": ad_type,
                    "count": 1,
                    "duplicates": 0,
                    "lowest_value_ad": ad,
                    "highest_value_ad": ad,
                }
                # lowest_value_ad = ad
                # highest_value_ad = ad
                continue
            analyzed_types[ad_type]["count"] += 1
            # duplicates
            if ad_id in checked_ids:
                analyzed_types[ad_type]["duplicates"] += 1
            else:
                checked_ids.append(ad_id)
            # lowest_value
            if ad_price < analyzed_types[ad_type]["lowest_value_ad"]["ad_price"]:
                analyzed_types[ad_type]["lowest_value_ad"] = ad
                # lowest_value_ad = ad
            # highest value
            if ad_price > analyzed_types[ad_type]["highest_value_ad"]["ad_price"]:
                analyzed_types[ad_type]["highest_value_ad"] = ad
                # highest_value_ad = ad
    return analyzed_types
