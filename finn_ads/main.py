import sys

from finn_ads.analyze_ads import analyze_ads
from finn_ads.rw_ads import load_ads, write_ads


def main():
    filename = sys.argv[sys.argv.index("--file") + 1]
    should_write = False
    try:
        write_index = sys.argv.index("--write")
        print("argv", len(sys.argv))
        writefile = (
            "adStats.txt"
            if len(sys.argv) <= write_index + 1
            else sys.argv[write_index + 1]
        )
        should_write = True
    except ValueError:
        pass

    ads = load_ads(filename)
    analyzed = analyze_ads(ads)

    if should_write:
        return write_ads(analyzed, writefile)
    print(analyzed)


if __name__ == "__main__":
    main()
