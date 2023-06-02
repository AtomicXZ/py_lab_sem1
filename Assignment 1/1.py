# bs = basic_salary, da = dearness, tr = travel, hr = house_rent, bonus = performance_incentive
bs = int(input("Enter basic salary:  "))

if bs >= 15000:
    da = 0.1*bs
    tr = 0.05*bs
    hr = 0.07*bs
    bonus = 1500
    salary = bs + da + tr + hr + bonus
elif 10000 <= bs < 15000:
    da = 0.07*bs
    tr = 0.03*bs
    hr = 0.04*bs
    bonus = bs*12*(30/365)
    salary = bs + da + tr + hr + bonus
else:
    tr = 0.02*bs
    bonus = bs*12*(20/365)
    salary = bs + tr + bonus

print(f"The salary is {format(salary, '.2f')}.")
