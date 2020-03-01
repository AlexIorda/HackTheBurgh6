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

data_dict_Q1 = {}
data_dict_Q2 = {}
data_dict_Q3 = {}
data_dict_Q4 = {}


def make_dict_points():
    global data_dict_Q1, data_dict_Q2, data_dict_Q3, data_dict_Q4
    with open ("api/sondaj_varste.json") as f:
        data = json.load(f)
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
                       "Santander" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Clydesdale Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "first direct": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Metro Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Nationwide": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Tesco Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "The Co-operative Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "TSB": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Yorkshire Bank":  {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0}

                    }
    data_dict_Q2 = { "Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                      "Royal Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                      "Barclays" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Halifax" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "HSBC UK" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Lloyds Bank" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "NatWest" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Royal Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Santander" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Clydesdale Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "first direct": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Metro Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Nationwide": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Tesco Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "The Co-operative Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "TSB": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Yorkshire Bank":  {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0}
                    }
    data_dict_Q3 = { "Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                      "Royal Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                      "Barclays" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Halifax" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "HSBC UK" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Lloyds Bank" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "NatWest" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Royal Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Santander" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Clydesdale Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "first direct": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Metro Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Nationwide": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Tesco Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "The Co-operative Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "TSB": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Yorkshire Bank":  {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0}

                    }
    data_dict_Q4 = { "Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                      "Royal Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                      "Barclays" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Halifax" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "HSBC UK" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Lloyds Bank" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "NatWest" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Royal Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Santander" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Clydesdale Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "first direct": { "16-24": 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Metro Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Nationwide": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Tesco Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "The Co-operative Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "TSB": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                       "Yorkshire Bank":  {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0}
                    }
    for sample1 in data["Data"]["Brand"]:
        for sample in sample1["Data"]:
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

def best_bank(dictionary, age, income, want_credit = False):
    banks = ["Bank of Scotland", "Royal Bank of Scotland", "Barclays", "Halifax", "HSBC UK",  "Lloyds Bank", "NatWest", "Royal Bank of Scotland",
             "Santander", "Clydesdale Bank", "first direct", "Metro Bank", "Nationwide", "Tesco Bank", "The Co-operative Bank", "TSB", "Yorkshire Bank"]
    credit_dict = generate_credit_dictionary()
    mx = 0
    mxbank = "No bank suitable"
    for bank in banks:
        print(dictionary[bank])
        if (want_credit is True):
            if (bank in credit_dict):
                if (income > 3 * credit_dict[bank]):
                    if (dictionary[bank][age_segment(age)] >= mx):
                        mx = dictionary[bank][age_segment(age)]
                        mxbank = bank
            else:
                if (dictionary[bank][age_segment(age)] >= mx):
                    mx = dictionary[bank][age_segment(age)]
                    mxbank = bank
        else:
            if (dictionary[bank][age_segment(age)] >= mx):
                mx = dictionary[bank][age_segment(age)]
                mxbank = bank
    return mxbank

def age_segment(age):
    if (age <= 24):
        return "16-24"
    elif (age <= 34):
        return "25-34"
    elif (age <= 44):
        return "35-44"
    elif (age <= 54):
        return "45-54"
    elif (age <= 64):
        return "55-64"
    else:
        return "65+"

path_list = ["api/atm/barclays_atm.json", "api/atm/firsttrustbank_atm.json", "api/atm/ireland_atm.json",
             "api/atm/natwest_atm.json", "api/atm/scotland_atm.json", "api/atm/ulster_atm.json", "api/atm/lloyds_atm.json",
             "api/atm/royal_scotland_atm.json", "api/atm/danske_atm.json", "api/atm/first_trust_atm.json", "api/atm/halifax_atm.json",
             "api/atm/hsbc_atm.json", "api/atm/nbs_atm.json", "api/atm/santander_atm.json"]
def closest_distance_to_atm(s):
    MN = 10**101
    for bank in s:
        with open (bank) as f:
            atm_data = json.load(f)
        mn = 10**100
        for atm in atm_data["data"]["Brand"][0]["ATM"]:
            lat_atm = float(atm["Location"]["PostalAddress"]["GeoLocation"]["GeographicCoordinates"]["Latitude"])
            long_atm = float(atm["Location"]["PostalAddress"]["GeoLocation"]["GeographicCoordinates"]["Longitude"])
            #print(lat_atm,long_atm)
            dist = math.sqrt( (lat_atm - current_lat) ** 2 + (long_atm - current_long) ** 2)
            #print(dist)
            if (dist < mn):
                mn = dist
        if mn < MN:
            MN = mn
    return MN

def generate_credit_dictionary():
    credit_dict = {}
    api_to_bank = {"api/ccc/natwest_ccc.json" : "NatWest",  "api/ccc/bank_of_scotland_ccc.json": "Bank of Scotland", "api/ccc/barclays_ccc.json": "Barclays",
                   "api/ccc/hsbc_ccc.json": "HSBC UK", "api/ccc/lloyds_ccc.json": "Lloyds Bank", "api/ccc/royal_scotland_ccc.json": "Royal Bank of Scotland", "api/ccc/santander_ccc.json": "Santander"}
    path_list_ccc = ["api/ccc/natwest_ccc.json", "api/ccc/bank_of_scotland_ccc.json", "api/ccc/barclays_ccc.json", "api/ccc/hsbc_ccc.json",
                 "api/ccc/lloyds_ccc.json", "api/ccc/royal_scotland_ccc.json", "api/ccc/santander_ccc.json"]
    for s in path_list_ccc:
        credit_dict[api_to_bank[s]] = get_minimum_credit_limit(s)
    return credit_dict
print(get_minimum_credit_limit("api/ccc/ireland_ccc.json"))
print(get_minimum_credit_limit("api/ccc/natwest_ccc.json"))
make_dict_points()
print(generate_credit_dictionary())
print(best_bank(data_dict_Q1, 68, 800, True))
