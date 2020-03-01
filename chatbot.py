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
        
        
        
def make_dict_points():
    with open ("api/sondaj_varste.json") as f:
        data = json.load(f)
    data_dict_Q1 = {}
    data_dict_Q2 = {}
    data_dict_Q3 = {}
    data_dict_Q4 = {}
    answers1 = {"Extremely likely" : 6, "Very likely": 5, "Fairly likely": 4, "Unlikely": 3,
               "NOT USED IN RANKING: Don't know": 2, "NOT USED IN RANKING: Do not recommend": 1}
    answers2 = {"Extremely likely" : 7, "Very likely": 6, "Fairly likely": 5, "Unlikely": 4,
               "NOT USED IN RANKING: Don't know": 3, "NOT USED IN RANKING: Do not recommend": 1,
               "NOT USED IN RANKING: Have not used a branch in the last 3 months": 2}
    answers3 = {"Extremely likely" : 7, "Very likely": 6, "Fairly likely": 5, "Unlikely": 4,
               "NOT USED IN RANKING: Don't know": 3, "NOT USED IN RANKING: Do not recommend": 1,
               "NOT USED IN RANKING: Have not used online or mobile banking in the last 3 months": 2}
    answers4 = {"Extremely likely" : 7, "Very likely": 6, "Fairly likely": 5, "Unlikely": 4,
               "NOT USED IN RANKING: Don't know": 3, "NOT USED IN RANKING: Do not recommend": 1,
               "NOT USED IN RANKING: Have not been overdrawn in the last 12 months": 2}
    data_dict_Q1 = { "Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                      "Royal Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                      "Barclays" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Halifax" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "HSBC UK" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Lloyds Bank" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "NatWest" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Royal Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Santander" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0}
                    
                    }
    data_dict_Q2 = { "Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                      "Royal Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                      "Barclays" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Halifax" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "HSBC UK" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Lloyds Bank" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "NatWest" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Royal Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Santander" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0}
                    
                    }
    data_dict_Q3 = { "Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                      "Royal Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                      "Barclays" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Halifax" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "HSBC UK" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Lloyds Bank" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "NatWest" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Royal Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Santander" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0}
                    
                    }
    data_dict_Q4 = { "Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                      "Royal Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                      "Barclays" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Halifax" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "HSBC UK" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Lloyds Bank" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "NatWest" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Royal Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Santander" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0}
                    
                    }
    for sample in data["Data"]["Brand"][0]["Data"]:
       # print(sample)
        if "PCAQ1All" in sample:
            data_dict_Q1[sample["Brand"]][sample["Age"]] += sample["Weight"] *  answers1[sample["PCAQ1All"]]
        if "PCAQ2All" in sample:
            data_dict_Q2[sample["Brand"]][sample["Age"]] += sample["Weight"] *  answers2[sample["PCAQ2All"]]
        if "PCAQ3All" in sample:
            data_dict_Q3[sample["Brand"]][sample["Age"]] += sample["Weight"] *  answers3[sample["PCAQ3All"]]
        if "PCAQ4All" in sample:
            data_dict_Q4[sample["Brand"]][sample["Age"]] += sample["Weight"] *  answers4[sample["PCAQ4All"]]
    print(data_dict_Q1["Bank of Scotland"]["25-34"])
#print(min(closest_distance_to_atm("api/ireland_atm.json"), closest_distance_to_atm("api/natwest_atm.json")))
#print_benefits("api/natwest_pca.json")
list_minimum_credit_limit = [get_minimum_credit_limit("api/ireland_ccc.json"), get_minimum_credit_limit("api/natwest_ccc.json")]
#bot
make_dict_points()
print("Hello! I am your new friend the CHAAAAT BOT!")
print("I will help you choose the right bank for you!")
print("But firrrrst....enter some information in order to help me")
age = int(input("How old are you?"))
income = float(input("What is your income/month?"))
for val in list_minimum_credit_limit:
    if (val > income/3):
        list_minimum_credit_limit.remove(val)
#print(list_minimum_credit_limit)