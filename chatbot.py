import json
import requests
import math
#print (lat,long)
#print(float(atm_data["data"]["Brand"][0]["ATM"][3]["Location"]["PostalAddress"]["GeoLocation"]["GeographicCoordinates"]["Latitude"]))

# printing current location
res = requests.get("https://ipinfo.io/")
loc_data = res.json()
current_loc = loc_data["loc"].split(",")
current_lat = float(current_loc[0])
current_long = float(current_loc[1])


def closest_distance_to_atm(s):
    #returns the closest atm for bank with the path s (exp api/ireland_atm.json)
    #daca are in json dupa data [] trb scoase de la inceput si final
    with open (s) as f:
        atm_data = json.load(f)    
    mn = 10**100
    for atm in atm_data["data"]["Brand"][0]["ATM"]:
        lat_atm = float(atm["Location"]["PostalAddress"]["GeoLocation"]["GeographicCoordinates"]["Latitude"])
        long_atm = float(atm["Location"]["PostalAddress"]["GeoLocation"]["GeographicCoordinates"]["Longitude"])
        #print(lat_atm,long_atm)
        dist = math.sqrt( (lat_atm - current_lat) ** 2 + (long_atm - current_long) ** 2)
        print(dist)
        if (dist < mn):
            mn = dist
    return mn
def get_minimum_balance_repayment_rate(s): # cat platesti inapoi pe luna minim
    #returns the minimum balance ...  for bank with the path s
    #daca are in json dupa data [] trb scoase de la inceput si final
    with open (s) as f:
        ccc_data = json.load(f)
    #consumer credit compilance
    min_rate = float(ccc_data["data"]["Brand"][0]["CCC"][0]["CCCMarketingState"][0]["Repayment"]["MinBalanceRepaymentRate"])
    return min_rate

def get_minimum_credit_limit(s):  # cat poti sa imprumuti pe luna minim
    #returns the minimum credit limit  for bank with the path s
    #daca are in json dupa data [] trb scoase de la inceput si final
    with open (s) as f:
        ccc_data = json.load(f)
    #consumer credit compilance
    print(ccc_data["data"]["Brand"][0]["CCC"][0]["CCCMarketingState"][0]["CoreProduct"])
    print("\n\n\n\n\n\n\n\n\n")
    if ("MinCreditLimit" in ccc_data["data"]["Brand"][0]["CCC"][0]["CCCMarketingState"][0]["CoreProduct"]):
        min_credit = float(ccc_data["data"]["Brand"][0]["CCC"][0]["CCCMarketingState"][0]["CoreProduct"]["MinCreditLimit"])
        return min_credit
    return -1;

def get_apr(s): #rata anuala folosita pt a se calc rata lunara 
    #returns the anual percentage fee for bank with the path s
    #daca are in json dupa data [] trb scoase de la inceput si final
    with open (s) as f:
        ccc_data = json.load(f)
    #consumer credit compilance
    min_credit = float(ccc_data["data"]["Brand"][0]["CCC"][0]["CCCMarketingState"][0]["CoreProduct"]["APR"])
    return min_credit
def print_benefits(s):#beneficii dubioase
    #prints the benefits of a bank with the path s
    #daca are in json dupa data [] trb scoase de la inc si final
    with open (s) as f:
        pca_data = json.load(f)
    for elem in pca_data["data"]["Brand"][0]["PCA"][0]["PCAMarketingState"][0]["FeaturesAndBenefits"]["FeatureBenefitItem"]:
        print(elem["Name"])
print(min(closest_distance_to_atm("api/ireland_atm.json"), closest_distance_to_atm("api/natwest_atm.json")))
print_benefits("api/natwest_pca.json")
list_minimum_credit_limit = [get_minimum_credit_limit("api/ireland_ccc.json"), get_minimum_credit_limit("api/natwest_ccc.json")]
#bot
print("Hello! I am your new friend the CHAAAAT BOT!")
print("I will help you choose the right bank for you!")
print("But firrrrst....enter some information in order to help me")
age = int(input("How old are you?"))
income = float(input("What is your income/month?"))
for val in list_minimum_credit_limit:
    if (val > income/3):
        list_minimum_credit_limit.remove(val)
print(list_minimum_credit_limit)