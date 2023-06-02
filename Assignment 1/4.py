days = int(input("Enter number of late days:  "))

if (days > 0 and days < 8):
    fine = days*0.75
    print(fine)
elif (days > 7 and days < 16):
    fine = 7*0.75 + (days-7)*1
    print(fine)
elif (days > 15 and days < 22):
    fine=7*0.75 + 8*1 + (days-15)*2.5
    print(fine)
elif (days > 21 and days < 31):
    fine=7*0.75 + 8*1 + 6*2.5 + (days-21)*5
    print(fine)
else:
    print("Library membership cancelled.")
