import json
import os

with open(os.path.join(os.path.dirname(__file__), "descriptions.json")) as file:
    descriptions = json.load(file)

for key, value in descriptions.items():
    print(f"{key} - {value}")