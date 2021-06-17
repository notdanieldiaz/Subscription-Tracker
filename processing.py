import datetime
from datetime import date

def cd(de): #splitting time object
    de_month = de.strftime("%m")
    de_day = de.strftime("%d")
    de_year = de.strftime("%y")

    return de_month, de_day, de_year

def ip(m,d,y): # processing
    subname = str(input("Please enter name of subscription: "))
    price = float(input("Please enter the cost of the subscription: $"))
    timeperiod = str(input("Enter the type of time period for the subcription (Monthly or Yearly): "))
    
    de = date(y,m,d)

    print("Subcription:", str(subname))
    print("Price: $", str(price))
    print("Recurring Period Type:", str(timeperiod))
    
    de.strftime("%m/%d/%y")

    return subname, price, timeperiod, de