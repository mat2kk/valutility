import json 
import os
import requests
import time

with open(os.path.join(os.path.dirname(__file__), '..', 'auth', 'details.json')) as file:
    details = json.load(file)

with open(os.path.join(os.path.dirname(__file__), '..', 'auth', 'riot_details.json')) as file:
    riot_details = json.load(file)

shard = details["shard"]
uuid = riot_details["uuid"]
entitlements_token = riot_details["entitlements_token"]
access_token = riot_details["access_token"]

urlStorefront = f"https://pd.{shard}.a.pvp.net/store/v2/storefront/{uuid}"
urlPrices = f"https://pd.{shard}.a.pvp.net/store/v1/offers"
urlWallet = f"https://pd.{shard}.a.pvp.net/store/v1/wallet/{uuid}"

headers = {
    "X-Riot-Entitlements-JWT": entitlements_token,
    "Authorization": f"Bearer {access_token}",
}

# Call GET Storefront
response = requests.get(urlStorefront, headers=headers)

if response.status_code == 200:
    rawStorefrontData = response.json()
else:
    print(f"Error: {response.status_code} - {response.text}")

offer_ids = [offer['OfferID'] for offer in rawStorefrontData['SkinsPanelLayout']['SingleItemStoreOffers']]


for offer_id in offer_ids:
    # Name data
    name_data = requests.get(f"https://valorant-api.com/v1/weapons/skinlevels/{offer_id}").json()
    offer_name = name_data["data"]["displayName"]
    # Price data
    price_data = requests.get(urlPrices, headers=headers).json()
    vp_id = "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"
    offer_price = "N/A"
    for offer in price_data['Offers']:
        if offer['OfferID'] == offer_id:
            offer_price = f"{offer['Cost'][vp_id]} VP"
            break
    print(f"{offer_name} - {offer_price}")

# Wallet data

response = requests.get(urlWallet, headers=headers)

if response.status_code == 200:
    rawWalletData = response.json()
else:
    print(f"Error: {response.status_code} - {response.text}")

currentBalance = rawWalletData['Balances'][vp_id]

print(f"Current balance: {currentBalance} VP")

# Time remaining data

print(f"Time remaining: {time.strftime("%H:%M:%S", time.gmtime(rawStorefrontData['SkinsPanelLayout']['SingleItemOffersRemainingDurationInSeconds']))}")