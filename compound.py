principle = 0
rate = 0
time = 0
while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle amount must be greater than zero.")
while rate <= 0:
    rate = float(input("Enter the rate of interest: "))
    if rate <= 0:
        print("Rate of interest must be greater than zero.")
while time <= 0:
    time = float(input("Enter the time period: "))
    if time <= 0:
        print("Time period must be greater than zero.")
print(f"Principle: {principle}, Rate: {rate}, Time: {time}")
final_amount = principle *( (1 + (rate / 100)) ** time)
print(f"Final amount after {time} years: {final_amount}")