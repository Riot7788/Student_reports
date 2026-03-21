# Student_reports

Скрипт для обработки CSV-файлов

## Проект содержит:
- Python 3.13
- pytest 9.0.2
- tabulate 0.10.0
- README с инструкцией 
## Настройка:

1. Репозиторий:
```bash
git clone https://github.com/Riot7788/Student_reports
```

2. Установка:
```bash
  pip install -r requirements.txt
```

## Запуск кода:

1. Запускает все CSV файлы из папки data
```bash
  python main.py --files data/*.csv --report median-coffee
```

2. Запускает определенные CSV файлы
```bash
  python main.py --files data/math.csv data/physics.csv --report median-coffee
```
## Запуск тестов:
```bash
  python -m pytest -v
```
