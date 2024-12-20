# импорт модулей
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
     # считать содержимое csv файла
    with open(INPUT_FILENAME, mode="r", encoding="utf-8") as csv_file:
        csv_read = csv.DictReader(csv_file, delimiter=",")
        data = [row for row in csv_read]

    # Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, mode="w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
