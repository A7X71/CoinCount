# Arman Jadoon
# Computer Science GCSE [11d1]
# All code is written by me and my own.

import ast
import time
import re

CoinWeight = { # Contains the weight of each individual coin. (Will be used for calculations)
    "£2": 12.00,
    "£1": 8.75,
    "50p": 8.00,
    "20p": 5.00,
    "10p": 6.50,
    "5p": 3.25,
    "2p": 7.12,
    "1p": 3.56
}

BagWeight = { # Data Structure that contains the BagWeights and Values.
    "£2": {"Weight": CoinWeight["£2"] * 10, 
           "TotalValue": 2 * 10},
    "£1": {"Weight": CoinWeight["£1"] * 20, 
           "TotalValue": 1 * 20},
    "50p": {"Weight": CoinWeight["50p"] * 20, 
           "TotalValue": 0.5 * 20},
    "20p": {"Weight": CoinWeight["20p"] * 50, 
           "TotalValue": 0.2 * 50},
    "10p": {"Weight": CoinWeight["10p"] * 50, 
           "TotalValue": 0.1 * 50},
    "5p": {"Weight": CoinWeight["5p"] * 100, 
           "TotalValue": 0.05 * 100},
    "2p": {"Weight": CoinWeight["2p"] * 50, 
           "TotalValue": 0.02 * 50},
    "1p": {"Weight": CoinWeight["1p"] * 100, 
           "TotalValue": 0.01 * 100}
}



# The function that handles all input validation.
# I make use of different parameters and create my own validation criteria which I assign to different inputs.
        
    
def menu():
    print("-----------------------")
    print("Coin System\n")
    print("1. Input Details")
    print("2. Running Totals")
    print("3. Volunteer Accuracy Report\n")
    print("0. Exit")

    while True:  # Start an infinite loop
        try:
            Selection = int(input("Please Select an Integer 0-3: "))
            if 0 <= Selection <= 3:  # Check if it's within the valid range
                break  # Exit the loop if a valid input is received
            else:
                print("Please select a number between 0 and 3.")
        except ValueError:
            print("It must be an Integer, Try again!")

    return Selection



Selection = menu()

def save_results(results):
    with open("CoinCount.txt", "a") as file:
        file.write("Volunteer: {}, CorrectWeight: {}, AccuracyScore: {}%, CoinsOff: {}, TotalRaised: £{}, BagsChecked: {}\n".format(
    results["VolunteerName"], results["CorrectWeight"], results["AccuracyScore"], results["CoinsOff"], Results["TotalRaised"], Results["BagsChecked"]
))


def read_results(value, type):
    string = value

    # Updated regex pattern to match your specific format
    pattern = r"Volunteer: (.*?), CorrectWeight: (.*?), AccuracyScore: ([\d.]+)%\, CoinsOff: ([\d.]+), TotalRaised: £([\d.]+), BagsChecked: (\d+)"

    match = re.search(pattern, string)

    if match:       
        if type == 1:
            return match.group(1)
        elif type == 2:
            return match.group(2)
        elif type == 3:
            return match.group(3)
        elif type == 4:
            return match.group(4)
        elif type == 5:
            return match.group(5)
        elif type == 6:
            return match.group(6)


def StartCoinSystemProcess():

    while True:

        try:
            VolunteerName = str(input("ENTER Volunteer Name: "))

            if VolunteerName.isalpha():
                break
            else:
                print("Must be Alphabetical (No Integers allowed), try again. \n")
        except ValueError:
            print("Your input must be a string! Try again.")
        



    CoinType = input("ENTER Type of Coin (e.g £2 or 50p): ")
    WeightOfBag = float(input("ENTER Bag Weight: "))

    AccuracyResults = { # Interchangable values based on the volunteer's results. (Will be returned)
        "VolunteerName": VolunteerName,
        "CorrectWeight": False,
        "AccuracyScore": 0,
        "CoinsOff": 0,
        "TotalRaised": 0,
        "BagsChecked": 1
    } 


    ExpectedWeight = BagWeight[CoinType]["Weight"]

    ActualWeight = WeightOfBag


    if ExpectedWeight == ActualWeight:
        print("Your weight is accurate. You may close the system.")
        AccuracyResults["CorrectWeight"] = True
        
        # To calculate accuracy score (percentage)
        ExpectedCoinAmount = ExpectedWeight / CoinWeight[CoinType]
        ActualCoinAmount = float(ActualWeight / CoinWeight[CoinType])

        TotalAccuracyScore = (ExpectedCoinAmount / ActualCoinAmount) * 100
        CoinsOff = (ExpectedCoinAmount - ActualCoinAmount)

        AccuracyResults["AccuracyScore"] = TotalAccuracyScore
        AccuracyResults["CoinsOff"] = CoinsOff
        AccuracyResults["TotalRaised"] = float(BagWeight[CoinType]["TotalValue"])

        return AccuracyResults
    else:
        ExpectedCoinAmount = ExpectedWeight / CoinWeight[CoinType]
        ActualCoinAmount = float(ActualWeight / CoinWeight[CoinType])

        TotalAccuracyScore = (1 - ((ExpectedCoinAmount / ActualCoinAmount) - 1)) * 100
    

        CoinsOff = (ExpectedCoinAmount - ActualCoinAmount)
        print(ExpectedCoinAmount)
        print(ActualCoinAmount)

        AccuracyResults["AccuracyScore"] = round(TotalAccuracyScore)
        AccuracyResults["CoinsOff"] = CoinsOff
        AccuracyResults["TotalRaised"] = float(BagWeight[CoinType]["TotalValue"]) - CoinsOff

        return AccuracyResults

def GetRunningTotals():
    mode = str(input("all/specific: "))

    if mode == "all":
        with open("CoinCount.txt", "r") as file:
            Lines = file.readlines()
            for Line in Lines:
                print(f"Volunteer: {read_results(Line, 1)}, TotalRaised: {'£' + str(read_results(Line, 5))}")


def FetchAccuracyReport(data, sort_by_index, ascending=True):
    
    pattern = r"Volunteer: (.*?), CorrectWeight: (.*?), AccuracyScore: (\d+\.\d+)%, CoinsOff: (\d+\.\d+), TotalRaised: £(\d+), BagsChecked: (\d+)"
    
    extracted_data = []
    
    # Extract data from each entry
    for entry in data:
        match = re.match(pattern, entry)
        if match:
            volunteer, correct_weight, accuracy_score, coins_off, total_raised, bags_checked = match.groups()
            extracted_data.append({
                'Volunteer': volunteer,
                'CorrectWeight': bool(correct_weight),
                'AccuracyScore': float(accuracy_score),
                'CoinsOff': float(coins_off),
                'TotalRaised': int(total_raised),
                'BagsChecked': int(bags_checked)
            })
    
    # Sort the extracted data
    sorted_data = sorted(extracted_data, key=lambda x: list(x.values())[sort_by_index], reverse=not ascending)
    
    return sorted_data



        


if Selection == 1:
    print("Buss' My Nines\n")
    Results = StartCoinSystemProcess()

    with open("CoinCount.txt", "r") as yes:
        lines = yes.readlines()
        name_exists = False

        for line in lines:
            loop = -1
            loop+= 1
            if Results["VolunteerName"] in line:
                print("Bruh its all there!!")
                name_exists = True 

                time.sleep(1)

                CorrectWeight = read_results(line, 2)
                AccuracyScore = read_results(line, 3)
                CoinsOff =      read_results(line, 4)
                TotalRaised =   read_results(line, 5)
                BagsChecked =   read_results(line, 6)
                
                print(Results["TotalRaised"])
                lines[loop] = f"Volunteer: {Results['VolunteerName']}, CorrectWeight: {Results['CorrectWeight']}, AccuracyScore: {str(Results['AccuracyScore'])}%, CoinsOff: {Results['CoinsOff']}, TotalRaised: {'£'+str((float(TotalRaised) + Results['TotalRaised']))}, BagsChecked: {str(int(BagsChecked) + 1)}"


                with open("CoinCount.txt", "w") as file:
                    Lines = file.writelines(lines)
                break

        if not name_exists:
            save_results(Results)
            print("Saved in datastore")
elif Selection == 2:
    GetRunningTotals()
elif Selection == 3:

    with open("CoinCount.txt", 'r') as file:
        x = file.readlines()

        sorted_report = FetchAccuracyReport(x, sort_by_index=2, ascending=True)
        for item in sorted_report:
            print(item)
