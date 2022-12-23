total = float(120.62 + 1.32)
print("Welcome to the Global Energy bill calculator!")
accountNumber=int(input("Enter your account number: "))
month=int(input("Enter the month number (e.g., for January, enter 1): "))
while month <= 0 or month > 12:
    print ("Did not enter a valid monthly value. Try again.")
    month=int(input("Enter the month number (e.g., for January, enter 1): "))
elecPlan=(input("Enter your electricity plan (EFIR or EFLR): ")) 
while elecPlan != "EFIR" and elecPlan != "EFLR":
    print ("Did not enter a valid electricity plan. Try again.")
    elecPlan=(input("Enter your electricity plan (EFIR or EFLR): "))
elecUsed= float(input(f"Enter the amount of electricity you used in month {month} (in kWh): "))
while elecUsed <0:
    print ("Please enter a number above or equal to 0.")
    elecUsed= float(input(f"Enter the amount of electricity you used in month {month} (in kWh): "))
gasPlan=(input("Enter your gas plan (GFIR or GFLR): "))
while gasPlan != "GFIR" and gasPlan != "GFLR":
    print ("Did not enter a valid gas plan. Try again.")
    gasPlan=(input("Enter your gas plan (GFIR or GFLR): "))
gasUsed=float(input(f"Enter the amount of gas you used in {month} (in GJ): "))
while gasUsed <0:
    print ("Please enter a number above or equal to 0.")
    gasUsed=float(input(f"Enter the amount of gas you used in {month} (in GJ): "))
province=(input("Enter the abbreviation for your province of residence (two letters): "))
while province != "AB" and province !="BC" and province !="MB" and province !="NT" and province !="NU" and province !="QC" and province !="SK" and province !="YT" and province !="ON" and province !="NB" and province !="NL" and province !="NS" and province !="PE":
    print ("Did not enter a valid province. Make sure its in the format (AB).")
    province=(input("Enter the abbreviation for your province of residence (two letters): "))
if elecPlan == "EFIR": 
    if elecUsed > 1000:
            total += ((8.36*1000)+(9.41*(elecUsed-1000)))*0.01
    else:
            total += (8.36*elecUsed)*0.01
else:
    total += (9.11*elecUsed)*0.01
if gasPlan == "GFIR":
    if gasUsed > 950:
        total += ((950*4.56)+(5.89*(gasUsed-950)))*0.01
    else: total += (4.56*gasUsed)*0.01
else: 
    total += (3.93*gasUsed)*0.01
if province == "AB" or province == "BC" or province == "MB" or province == "NT" or province == "NU" or province == "QC" or province == "SK" or province == "YT":
    total *= 1.05
elif province == "ON":
    total*= 1.13
else:
    total *= 1.15
print ("Thank you!")
print (f"Total amount due now: ${total:.2f}")


