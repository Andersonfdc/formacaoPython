MAJORITY = 18

age = int(input("What's your age: "))

if age >= 18:
    print("You're old enough to drive")
    status = "Approved" if age > 20 else "filed"
    print (f"Driving test: {status}")
else:
    print("Sorry, you can't drive yet.")

