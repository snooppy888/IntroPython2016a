#! /Users/ThomasGaffney/anaconda/bin/python3.5

def sendathankyou(donorDict):
    while(True):
        userselection = input('Please input the name of the donor, list to display a list of current users, or main to return to the main program:')
        if(userselection.lower() == 'main'): break
        elif(userselection.lower() == 'list'):
            for keys in donorDict.keys():
                print(keys)
        else:
            if(userselection in donorDict.keys()):
                user = userselection
            else:
                user = userselection
                donorDict[user] = []
            donationamount = input('Please enter the donation amount for the selected user:')

            #Test if a number was given.
            while (True):
                try:
                    float(donationamount)
                    break
                except:
                    donationamount = input('That was not a number, please try again:')

            donorDict[user].append(float(donationamount))
            thankyou = 'Dear {user}: \n \nThank You For Your Generous Donation of {donationamount}. \n \nThe Charity \n'.format(user = user, donationamount = donationamount)
            print(thankyou)

    return donorDict

def printareport(donorDict):
    report_list = []
    for key in donorDict.keys():
        report_list.append([sum(donorDict[key]), key, len(donorDict[key]), sum(donorDict[key])/len(donorDict[key])])
    report_list.sort()
    str = "|donor\t\t  |donated\t  |donations\t  |avgdonation\t|\n"
    for item in report_list:
        str += '|{donor}\t  |{donated}\t\t  |{donations}\t\t  |{avgdonation}\t\t|\n'.format(donor = item[1],
                                                                               donated = item[0],
                                                                               donations = item[2],
                                                                               avgdonation = round(item[3],1)).expandtabs(8)
        str.format('center align')
    print(str)


if __name__ == '__main__' :
    donorDict = {'Tom Jones' : [25, 10, 15],
             'Brad Hardy' : [5, 9],
             'Manuel Miller' : [4, 21],
             'Josh Benson' : [1],
             'Ashley Scanlon' : [4, 9, 50]}

    while(True):
        userinput = input('Welcome to the mailroom!  Would you like to :\n    1. Send a Thank you  \n    2. Create a report  \n    3. Quit \nChoice 1, 2 or 3?:')
        if (userinput == str(1)):
            donorDict = sendathankyou(donorDict)
        if (userinput == str(2)):
            printareport(donorDict)
        if (userinput == str(3)):
            break


