import json

username = input("Username: ")
password = input("Password: ")

details = {
    "username": username,
    "password": password
}

with open('auth/details.json', 'w') as login:
    json.dump(details, login, indent=4)