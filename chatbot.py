import json
with open ('api/ireland_atm.json') as f:
    atm_data = json.load(f)
print(atm_data["meta"])