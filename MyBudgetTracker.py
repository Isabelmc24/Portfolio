
import json

def add_expense(purchases, details, amount):
    purchases.append({"details": details, "amount": amount})
    print("Purchase: {details}, Amount: {amount}")

def total_purchases(purchases):
    sum = 0
    for purchase in purchases:
        sum += purchase["amount"]
    return sum

def display_balance(budget, purchases):
    return budget - total_purchases(purchases)
def display_budget(budget, purchases):
    print(f"Budget: {budget}")
    print("Purchases:")
    for purchase in purchases:
        print(f"- {purchase['details']}: {purchase['amount']}")
        print(f"Current budget balance: {get_balance(budget, purchases)}")

def budget_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data["initial_budget"], data ["purchases"]
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []

def budget_details(filepath, initial_budget, purchases):
    data = {
        'initial_budget': initial_budget,
        'purchases': purchases
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
#User opening app msg
def main():
    print("Welcome to your budget tracker!")
    filepath = 'budget_data.json'
    initial_budget, purchases = budget_data(filepath)
    if initial_budget == 0:
        initial_budget = float(input("Please enter budget amount: "))
    budget = initial_budget
    purchases = []
#setting user selections when entering app
    while True:
        print("\nChoose one of the following:")
        print("A. Add purchase")
        print("B. Display budget amount")
        print("C. Quit")
        selection = input("Enter your selection (A, B, C): ")

        if selection == "A":
            details = input("Enter purchase details: ")
            amount = input("Enter purchase amount: ")
            add_purchase (purchases, details, amount)
        elif selection == "B":
            display_budget(budget, purchases)
        elif selection == "C":
            budget_details(filepath, initial_budget, purchases)
            print("Thank you for using your budget tracker!")
            break
        else:
            print("Invalid selection, please try again.")

if __name__ == "__main__":
    main()