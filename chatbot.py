import json
with open ('opendata-api-spec-compiled-master/atm.json') as f:
    atm_data = json.load(f)
print(atm_data["title"])