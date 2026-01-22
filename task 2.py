# TODO решите задачу
import json
from pathlib import Path

def task() -> float:
    with open("input.json") as json_file:
        json_data = json.load(json_file)

    sum_values = sum(i["scores"] * i["weights"] for i in json_data)
    return round(sum_values, 3)

if __name__ == "__main__":
    print(task())
