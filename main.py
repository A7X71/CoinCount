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


    Selection = RecurseInputs("Select an option: ", int, None)

    if Selection > 3:
        print("Number is too large")
        Selection = RecurseInputs("Select an option: ", int, None)
    elif Selection < 0:
        print("Too small, (not on the list)")
        Selection = RecurseInputs("Select an option: ", int, None)

    return Selection


Selection = menu()

def save_results(results):
    with open("Database.txt", "a") as file:
        file.write(f"Volunteer: {results["VolunteerName"]}, CorrectWeight: {results['CorrectWeight']}, " f"AccuracyScore: {results['AccuracyScore']}%, CoinsOff: {results['CoinsOff']}, TotalRaised: {Results["TotalRaised"]}\n")

def read_results(value, type):
    string = value

    pattern = r"Volunteer: (.*?), CorrectWeight: (.*?), AccuracyScore: (\d+\.\d+)%, CoinsOff: (\d+\.\d+), TotalRaised: (\d+)"

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

def StartCoinSystemProcess():
    VolunteerName = RecurseInputs("ENTER Volunteer Name: ", str, None)
    CoinType = RecurseInputs("ENTER Type of Coin (e.g £2 or 50p): ", None, "Any")
    WeightOfBag = RecurseInputs("ENTER Bag Weight: ", int, None)

    AccuracyResults = { # Interchangable values based on the volunteer's results. (Will be returned)
        "VolunteerName": VolunteerName,
        "CorrectWeight": False,
        "AccuracyScore": 0,
        "CoinsOff": 0,
        "TotalRaised": 0
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

        AccuracyResults["AccuracyScore"] = TotalAccuracyScore
        AccuracyResults["CoinsOff"] = CoinsOff
        AccuracyResults["TotalRaised"] = ActualCoinAmount

        return AccuracyResults

def GetRunningTotals():
    mode = RecurseInputs("all/specific: ", str, None)

    if mode == "all":
        with open("Database.txt", "r") as file:
            Lines = file.readlines()
            for Line in Lines:
                print(f"Volunteer: {read_results(Line, 1)}, TotalRaised: {"£"+str(read_results(Line, 5))}")


def FetchAccuracyReport():
    print("---------------------------------")
    print("Volunteer Accuracy Sorted from Highest Accuracy to Lowest Accuracy.")
    print("Note: What is displayed is the accuracy of their most recent log.\n")

    with open("Database.txt", "r") as file:
        lines = file.readlines()    
        
        simpleArray = lines

        lines.sort()

        


if Selection == 1:
    print("Buss' My Nines\n")
    Results = StartCoinSystemProcess()

    with open("Database.txt", "r") as yes:
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
                
                print(Results["TotalRaised"])
                lines[loop] = f"Volunteer: {Results['VolunteerName']}, CorrectWeight: {Results["CorrectWeight"]}, AccuracyScore: {str(Results["AccuracyScore"])}%, CoinsOff: {Results["CoinsOff"]}, TotalRaised: {str((float(TotalRaised) + Results["TotalRaised"]))} "

                with open("Database.txt", "w") as file:
                    Lines = file.writelines(lines)
                break

        if not name_exists:
            save_results(Results)
            print("Saved in datastore")
elif Selection == 2:
    GetRunningTotals()
elif Selection == 3:
    FetchAccuracyReport()
