import json
import os
import subprocess
import requests

# Shard handling

shard = input("Shard: ")

if shard == "1":
    shard = "ap"
elif shard == "2":
    shard = "na"
elif shard == "3":
    shard = "eu"
elif shard == "4":
    shard = "kr"

username = input("Username: ")
password = input("Password: ")

details = {
    "username": username,
    "password": password,
    "shard": shard,
}

with open('auth/details.json', 'w') as login:
    json.dump(details, login, indent=4)

while True:
    result = subprocess.run(["python", "auth/auth_request.py"], capture_output=True, text=True)
    if "Failed to authenticate" in result.stdout:
        print("Login credentials invalid. Please try again.")
        username = input("Username: ")
        password = input("Password: ")

        details = {
            "username": username,
            "password": password,
            "shard": shard,
        }
        with open('auth/details.json', 'w') as file:
            json.dump(details, file, indent=4)
    else:
        with open('auth/riot_details.json') as file:
            riot_details = json.load(file)
            uuid = riot_details["uuid"]
            headers = {
                'X-Riot-Entitlements-JWT': riot_details["entitlements_token"],
                'Authorization': f"{riot_details["token_type"]} {riot_details["access_token"]}",
            }   
            url = f'https://pd.{shard}.a.pvp.net/name-service/v2/players'
            response = requests.put(url, headers=headers, json=[uuid])
            if response.status_code == 200:
                data = response.json()
                user_data = data[0]
                username = user_data['GameName']
                tag = user_data['TagLine']

        print (f"Authentication successful. Logged in as {username}#{tag}.")
        break 

command = input("$ valutility ")

while command != "quit":
    script_path = f"features/{command}.py"
    if os.path.exists(script_path):
        try:
            subprocess.run(["python", script_path])
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Command not found. Type 'help' for a list of commands.")
    command = input("$ valutility ")