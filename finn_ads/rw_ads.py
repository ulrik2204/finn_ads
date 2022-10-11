import csv

from finn_ads.types_finn_ads import AnalyzedType, FinnAd


def load_ads(filename: str) -> list[FinnAd]:
    with open(filename, newline="") as file:
        reader = csv.DictReader(file, fieldnames=["ad_id", "ad_type", "ad_price"])
        data = [
            {
                "ad_id": int(dic["ad_id"]),
                "ad_type": dic["ad_type"],
                "ad_price": float(dic["ad_price"]),
            }
            for dic in reader
        ]
    return data


def write_ads(analyzed_data: dict[str, AnalyzedType], filename="adStats.txt"):
    with open(filename, "w") as f:
        for ad_stats in analyzed_data.values():
            lowest = ad_stats["lowest_value_ad"]
            highest = ad_stats["highest_value_ad"]
            f.write(f"AdType: {ad_stats['ad_type']}\n")
            f.write(f"Current amount of ads: {ad_stats['count']}\n")
            f.write(f"Duplicated ads: {ad_stats['duplicates']}\n")
            f.write(f"Lowest value ad: {lowest['ad_id']} ({lowest['ad_price']} kr)\n")
            f.write(
                f"Highest value ad: {highest['ad_id']} ({highest['ad_price']} kr)\n"
            )
            f.write("\n")
