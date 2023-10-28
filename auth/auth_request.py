# credits to floxay
import os
import json
import asyncio
import sys
import riot_auth

# huge thanks to floxay #

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

with open(os.path.join(os.path.dirname(__file__), "details.json")) as file:
    data = json.load(file)

credentials = data['username'], data['password']

auth = riot_auth.RiotAuth()
asyncio.run(auth.authorize(*credentials))

riot_details = {
    "Access Token Type": auth.token_type,
    "Access Token": auth.access_token,
    "Entitlements Token": auth.entitlements_token,
    "User ID": auth.user_id,
}
with open(os.path.join(os.path.dirname(__file__), "riot_details.json")) as data:
    json.dump(riot_details, data, indent=4)

asyncio.run(auth.reauthorize())