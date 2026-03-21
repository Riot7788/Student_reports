import pytest

from reports.median_coffee import MedianCoffeeReport
from report_builder import build_report


def test_median_coffee_basic():
    rows = [
        {"student": "Ivan", "coffee_spent": "100"},
        {"student": "Ivan", "coffee_spent": "200"},
        {"student": "Ivan", "coffee_spent": "300"},
    ]

    report = MedianCoffeeReport(rows)
    result = report.generate()

    assert len(result) == 1
    assert result[0]["student"] == "Ivan"
    assert result[0]["median_coffee"] == 200

def test_median_coffee_sorting():
    rows = [
        {"student": "Ivan", "coffee_spent": "100"},
        {"student": "Ivan", "coffee_spent": "200"},
        {"student": "Anna", "coffee_spent": "500"},
        {"student": "Anna", "coffee_spent": "600"},
    ]

    report = MedianCoffeeReport(rows)
    result = report.generate()

    assert result[0]["student"] == "Anna"
    assert result[1]["student"] == "Ivan"

def test_median_even_count():
    rows = [
        {"student": "Ivan", "coffee_spent": "100"},
        {"student": "Ivan", "coffee_spent": "200"},
        {"student": "Ivan", "coffee_spent": "300"},
        {"student": "Ivan", "coffee_spent": "400"},
    ]

    report = MedianCoffeeReport(rows)
    result = report.generate()

    assert result[0]["median_coffee"] == 250

def test_unknown_report():
    with pytest.raises(ValueError):
        build_report("unknown-report", [])