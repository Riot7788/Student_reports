from collections import defaultdict
from statistics import median


class MedianCoffeeReport:

    def __init__(self, rows):
        self.rows = rows

    def generate(self):

        students = defaultdict(list)

        for row in self.rows:
            student = row["student"]
            coffee = float(row["coffee_spent"])
            students[student].append(coffee)

        result = []

        for student, values in students.items():

            result.append({
                "student": student,
                "median_coffee": median(values)
            })

        result.sort(
            key=lambda x: x["median_coffee"],
            reverse=True
        )

        return result