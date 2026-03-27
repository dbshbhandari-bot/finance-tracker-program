import csv

transactions = []

# Load existing data
try:
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            transactions.append(float(row[0]))
except FileNotFoundError:
    pass

print("Welcome to Finance Tracker 💰")

while True:
    print("\n1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter income amount: "))
        transactions.append(amount)

        with open("data.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([amount])

        print("Income added!")

    elif choice == "2":
        amount = float(input("Enter expense amount: "))
        transactions.append(-amount)

        with open("data.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([-amount])

        print("Expense added!")

    elif choice == "3":
        balance = sum(transactions)
        print("Current Balance:", balance)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option!")