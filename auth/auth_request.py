import os
import json
import asyncio
import sys
import riot_auth

# huge thanks to floxay for lines 9 and 10 #

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

with open(os.path.join(os.path.dirname(__file__), "details.json")) as file:
    data = json.load(file)

credentials = data['username'], data['password']
try:
    auth = riot_auth.RiotAuth()
    asyncio.run(auth.authorize(*credentials))
    print("Authentication successful")
except riot_auth.RiotAuthenticationError as e:
    print(f"Failed to authenticate: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

riot_details = {
    "token_type": auth.token_type,
    "access_token": auth.access_token,
    "entitlements_token": auth.entitlements_token,
    "uuid": auth.user_id,
}

with open(os.path.join(os.path.dirname(__file__), "riot_details.json"), "w") as data:
    json.dump(riot_details, data, indent=4)

asyncio.run(auth.reauthorize())