import os
import json

def clearjson(fileName):    
    with open (os.path.join(os.path.dirname(__file__), '..', 'auth', f'{fileName}.json')) as file:
        data = json.load(file)

    for key in data:
        data[key] = ""

    with open(os.path.join(os.path.dirname(__file__), '..', 'auth', f'{fileName}.json'), 'w') as file:
        json.dump(data, file, indent=4)

clearjson("details")
clearjson("riot_details")

print("Successfully cleared all .json files")