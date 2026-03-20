from reports.median_coffee import MedianCoffeeReport


REPORTS = {
    "median-coffee": MedianCoffeeReport
}


def build_report(report_name, rows):

    report_class = REPORTS.get(report_name)

    if not report_class:
        raise ValueError(f"Unknown report: {report_name}")

    report = report_class(rows)

    return report.generate()