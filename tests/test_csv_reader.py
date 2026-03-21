from utils.csv_reader import read_csv_files


def test_read_csv(tmp_path):
    file = tmp_path / "test.csv"

    file.write_text(
        "student,coffee_spent\n"
        "Ivan,100\n"
        "Anna,200\n",
        encoding="utf-8"
    )

    rows = read_csv_files([str(file)])

    assert len(rows) == 2
    assert rows[0]["student"] == "Ivan"
    assert rows[1]["coffee_spent"] == "200"

def test_read_multiple_files(tmp_path):
    file1 = tmp_path / "file1.csv"
    file2 = tmp_path / "file2.csv"

    file1.write_text("student,coffee_spent\nIvan,100\n", encoding="utf-8")
    file2.write_text("student,coffee_spent\nAnna,200\n", encoding="utf-8")

    rows = read_csv_files([str(file1), str(file2)])

    assert len(rows) == 2
