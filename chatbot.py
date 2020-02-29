import json
import requests
with open ('api/ireland_atm.json') as f:
    atm_data = json.load(f)
print(atm_data["meta"])
 
# printing location
res = requests.get("https://ipinfo.io/")
loc_data = res.json()
print(loc_data["loc"])