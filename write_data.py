import argparse
from datetime import datetime
import json
from pathlib import Path
from zoneinfo import ZoneInfo


parser = argparse.ArgumentParser()

parser.add_argument("blood_min", type=int)
parser.add_argument("blood_max", type=int)
parser.add_argument("heart_rate", type=int)
parser.add_argument("heart_pulse", type=int)
parser.add_argument("weight", type=float)


blood_json = Path("docs/blood.json")
weight_json = Path("docs/weight.json")


if __name__ == "__main__":
    today = datetime.now(ZoneInfo("Asia/Tokyo")).date()
    arguments = parser.parse_args()
    blood = json.loads(blood_json.read_text())
    blood[str(today)] = {
        "min": arguments.blood_min,
        "max": arguments.blood_max,
        "heart_rate": arguments.heart_rate,
        "heart_pulse": arguments.heart_pulse,
    }
    blood_json.write_text(json.dumps(blood))
    weight = json.loads(weight_json.read_text())
    weight[str(today)] = {"weight": arguments.weight}
    weight_json.write_text(json.dumps(weight))
