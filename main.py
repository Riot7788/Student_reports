import argparse
from tabulate import tabulate

from utils.csv_reader import read_csv_files
from report_builder import build_report


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Paths to csv files"
    )

    parser.add_argument(
        "--report",
        required=True,
        help="Report name"
    )

    args = parser.parse_args()

    rows = read_csv_files(args.files)

    report = build_report(args.report, rows)

    table = [
        [r["student"], r["median_coffee"]]
        for r in report
    ]

    print(tabulate(table, headers=["Student", "Median coffee spent"]))


if __name__ == "__main__":
    main()