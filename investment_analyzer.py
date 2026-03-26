initial_money = float(input("Enter initial_money:"))
interest_rate = float(input("Enter interest_rate(%):"))
time = float(input("Enter time(days):"))
rate = interest_rate/100
time_years = time/365
interest = initial_money*rate*time_years
print("interest earned :", round(interest, 2))
final = initial_money+interest
print("---Investment Summary---")
print("Initial Investment:", initial_money)
print("Interest Rate:", interest_rate, "%")
print("Duration:", time , "days")
print("---------------------------------------")
print("Interest Earned:", round(interest, 2))
print("Final amount:", round(final, 2))
print("You invested:", initial_money)
print("At", interest_rate, "% for", time, "days")
profit_rate = (interest / initial_money)*100
print("Profit Rate:", round(profit_rate, 2), "%")
if profit_rate>10:
    print("Good Investment")
else:
    print("Low return")
    