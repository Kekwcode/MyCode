
birth_month = int(input("Enter your birth Month: "))
birth_day = int(input("Enter first Date: "))
num_days = 0

rest = birth_month % 2
calc2 = birth_month // 2
calc0 = birth_month / 2                                             #check if february
if calc0 > 1 and rest != 1:
    num_days = calc2 * 31 + (calc2-1)*30 - 2 + birth_day

elif calc0 > 1 and rest == 1:
    num_days = calc2 * 61 - 2 + birth_day

elif calc2 == 1 and rest == 0:
    num_days = 31 + birth_day

else:
    num_days = birth_day


if num_days % 7 == 1:
    print("Sunday")
if num_days % 7 == 2:
    print("Monday")
if num_days % 7 == 3:
    print("Tuesday")
if num_days % 7 == 4:
    print("Wednesday")
if num_days % 7 == 5:
    print("Thursday")
if num_days % 7 == 6:
    print("Friday")
if num_days % 7 == 0:
    print("Saturday")
print(num_days)


