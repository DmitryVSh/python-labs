# TODO решите задачу
import json

INPUT_FILENAME = "input.json"

def task() -> float:
    with open(INPUT_FILENAME, mode="r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    summa = sum(item["score"] * item["weight"] for item in data)
    return round(summa, 3)
print(task())
