def get_amount(text):
    while True:
        amount = input(text)

        if amount.replace(".", "", 1).isdigit():
            return float(amount)

        print("Please enter a valid number.")


def main():

    print("=== Personal Finance Calculator ===")

    name = input("Enter your name: ")

    income = []

    print("\n--- INCOME ---")

    while len(income) < 10:

        amount = get_amount("Enter income amount: ")
        income.append(amount)

        choice = input("Do you want to add another income? (y/n): ")

        if choice != "y":
            break

    expenses = []

    print("\n--- EXPENSES ---")

    while len(expenses) < 10:

        amount = get_amount("Enter expense amount: ")
        expenses.append(amount)

        choice = input("Do you want to add another expense? (y/n): ")

        if choice != "y":
            break

    total_income = sum(income)
    total_expenses = sum(expenses)
    savings = total_income - total_expenses

    if total_income > 0:
        percent_saved = savings / total_income * 100
    else:
        percent_saved = 0

    print("\n------------------------------")
    print("PERSONAL FINANCE REPORT")
    print("Name:", name)
    print("------------------------------")
    print("Total Income:", total_income)
    print("Total Expenses:", total_expenses)
    print("Savings:", savings)
    print("Percent Saved:", percent_saved)

    if total_expenses <= total_income:
        print("Affordable: Yes")
    else:
        print("Affordable: No")


main()