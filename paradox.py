import datetime, random


def getBirthddays(numberofbirthdays):
    birthdays = []
    for i in range(numberofbirthdays):
        startofyear = datetime.date(2001, 1, 1)
        randmnumberofdays = datetime.timedelta(random.randint(0, 364))
        birthday = startofyear + randmnumberofdays
        birthdays.append(birthday)
        return birthdays
    
def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    
    for a , birthdayA in enumerate(birthdays):
        for b , birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA
            

Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', "Dec"]
while True:
    print('How many birthdays shall I generate? (Max 100)')
    response =  input(">")
    if response.isdecimal() and (0 < int(response)<= 100):
        numbdays = int(response)
        break
print()
print("here are", numbdays, "birthdays:")
birthdays = getBirthddays(numbdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(", ", end="")
    monthName = Months[birthday.month - 1]
    dateText = "{} {}".format(monthName, birthday.day)
    print(dateText, end="")    
 
 
 #Determine if there are two birthdays that match.   
match = getMatch(birthdays)
 #display the result
print("In the simulation", end="")
 
if match != None:
    monthname = Months[match.month - 1]
    dateText = "{}{}".format(monthName, birthday.day)    
    print("multiple people have birthdays on", dateText)
else:
    print("there is no matching date")
    
# Run through 100,000 simulations:
print('Generating', numbdays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')


    
    

