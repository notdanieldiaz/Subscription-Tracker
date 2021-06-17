
# 1) Create Command Line interface asking for arguments about subscriptions (Due date, time periods between payments, price, name.)



def intake(): 
    while True:
        try:
            month = int(input("Please enter month subscribed: "))
            break
        except ValueError:
            print("Value error")
            continue

    while True:
        try:
            if (month <= 0 or month > 12):
                month = int(input("Month cannot be less than or equal to zero or greater than 12: "))
                continue
            else:
                break   
        except ValueError:
            print("Value Error")
            continue

    while True:
        try:
            day = int(input("Please enter the day: "))
            break
        except ValueError:
            print("Value Error")
            continue

#---(OPTIMIZATION NEEDED!!!)---#

    if (month == 1):
        while True: 
            try:
                if (day > 31):
                    day = int(input("January has a maximum of 31 days, please re-enter date: "))
                    continue
                elif (day <= 0):
                    day = int(input("Value cannot be less than or equal to zero: "))
                else:
                    break
            except ValueError:
                print("Value Error"*1)
                continue

          
    elif (month == 2):
        while True:
            try:
                if (day > 29):
                    day = int("February has a maximum of 29 days (leap year) or 28 (common year), please re-enter date: ")
                elif (day <= 0):
                    day = int(input("Value cannot be less than or equal to zero: "))
                else:
                    break
            
            except ValueError:
                print("ValueError"*1)
                continue

    elif (month == 3):
        while True:
            try:
                if (day > 31):
                    day = int(input("March has a maximum of 31 days, please re-enter date: "))
                elif (day <= 0):
                    day = int(input("Value cannot be less than or equal to zero: "))
                else:
                    break
            
            except ValueError:
                print("ValueError"*1)
                continue
            
            
    elif (month == 4):
        while True:
            try:
                if (day > 30):
                    day = int(input("April has a maximum of 30 days, please re-enter date: "))
                elif (day <= 0):
                    day = int(input("Value cannot be less than or equal to zero: "))
                else:
                    break

            except ValueError:
                print("ValueError"*1)
                continue
        
    elif (month == 5):
        while True:
            try:
                if (day > 31):
                    day = int(input("May has a maximum of 31 days, please re-enter date: "))
                elif (day <= 0):
                    day = int(input("Value cannot be less than or equal to zero: "))
                else:
                    break
            
            except ValueError:
                print("ValueError"*1)
                continue
            
    elif (month == 6):
        while True:
            try:
                if (day > 30):
                    day = int(input("June has a maximum of 30 days, please re-enter date: "))
                elif (day <= 0):
                    day = int(input("Value cannot be less than or equal to zero: "))
                else:
                    break
            
            except ValueError:
                print("ValueError"*1)
                continue
    
                  
    elif (month == 7):
        while True:
            try:
                if (day > 31):
                    day = int(input("July has a maximum of 31 days, please re-enter date: "))
                elif (day <= 0):
                    day = int(input("Value cannot be less than or equal to zero: "))
                else:
                    break

            except ValueError:
                print("ValueError"*1)
                continue
            
    elif (month == 8):
        while True:
            try:
                if (day > 31):
                    day = int(input("August has a maximum of 31 days, please re-enter date: "))
                elif (day <= 0):
                    day = int(input("Value cannot be less than or equal to zero: "))
                else:
                    break

            except ValueError:
                print("ValueError"*1)
                continue
            
    elif (month == 9):
        while True:
            try:
                if (day > 30):
                    day = int(input("September has a maximum of 30 days, please re-enter date: "))
                elif (day <= 0):
                    day = int(input("Value cannot be less than or equal to zero: "))
                else:
                    break
            except ValueError:
                print("ValueError"*1)
                continue
                    
    elif (month == 10):
        while True:
            try:
                if (day > 31):
                    day = int(input("October has a maximum of 31 days, please re-enter date: "))
                elif (day <= 0):
                    day = int(input("Value cannot be less than or equal to zero: "))
                else:
                    break
            except ValueError:
                print("ValueError"*1)
                continue
            
    elif (month == 11):
        while True:
            try:
                if (day > 30):
                    day = int(input("November has a maximum of 30 days, please re-enter date: "))
                elif (day <= 0):
                    day = int(input("Value cannot be less than or equal to zero: "))
                else:
                    break
            except ValueError:
                print("ValueError"*1)
                continue
            
    elif (month == 12):
        while True:
            try:
                if (day > 31):
                    day = int(input("December has a maximum of 31 days, please re-enter date: "))
                elif (day <= 0):
                    day = int(input("Value cannot be less than or equal to zero: "))
                else:
                    break
            except ValueError:
                print("ValueError"*1)
                continue

    year = int(input("Please enter the year: "))
    while(year <= 0):
        year = int(input("Entry cannot be smaller than or equal to 0, please re-enter the year: "))
    
    m = month   #idk
    d = day     #why
    y = year    #I did this lol

    return m, d, y





