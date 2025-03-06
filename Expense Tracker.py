import csv
import os

class Expense:
    def __init__(self, date, category, amount):
        self.date = date
        self.category = category
        self.amount = amount

class ExpenseTracker:
    def __init__(self, filename="expenses.csv"):
        self.expenses = []
        self.filename = filename
        self.budget = 0
        self.load_expenses()

    def set_budget(self, amount):
        """Set a monthly budget."""
        self.budget = amount
        print(f"Monthly budget set to ${self.budget:.2f}")

    def check_budget(self):
        total = self.total_expenses(False)
        if self.budget > 0 and total > self.budget:
            print(f"Warning! You have exceeded your budget of ${self.budget:.2f}")

    def add_expense(self, expense):
        self.expenses.append(expense)
        self.save_expenses()
        print("Expense has been added successfully!")
        self.check_budget()

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            self.save_expenses()
            print("Expense has been removed.")
        else:
            print("Invalid Expense Entered.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found.")
        else:
            print("Expense List:")
            for i, expense in enumerate(self.expenses, start=1):
                print(f"{i}. Date: {expense.date}, Category: {expense.category}, Amount: ${expense.amount:.2f}")

    def view_expenses_by_month(self, month):
        """View expenses for a specific month (YYYY-MM)."""
        filtered_expenses = [e for e in self.expenses if e.date.startswith(month)]
        if not filtered_expenses:
            print(f"No expenses found for {month}.")
        else:
            print(f"Expenses for {month}:")
            for i, expense in enumerate(filtered_expenses, start=1):
                print(f"{i}. Date: {expense.date}, Category: {expense.category}, Amount: ${expense.amount:.2f}")
    
    def total_expenses(self, print_output=True):
        total = sum(expense.amount for expense in self.expenses)
        if print_output:
            print(f"Total Expense: ${total:.2f}")
        return total

    def save_expenses(self):
        """Save expenses to a CSV file."""
        with open(self.filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount"])  # Write header
            for expense in self.expenses:
                writer.writerow([expense.date, expense.category, expense.amount])

    def load_expenses(self):
        """Load expenses from a CSV file."""
        if os.path.exists(self.filename):
            with open(self.filename, mode="r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    date, category, amount = row
                    self.expenses.append(Expense(date, category, float(amount)))

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expenses")
        print("4. View Expenses by Month")
        print("5. Set Monthly Budget")
        print("6. View Total Expenses")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ").strip()
            category = input("Enter the expense category (Food, Transport, Bills, etc.): ").strip()
            
            try:
                amount = float(input("Enter the amount: ").strip())
                expense = Expense(date, category, amount)
                tracker.add_expense(expense)
            except ValueError:
                print("Invalid amount! Please enter a valid number.")

        elif choice == "2":
            try:
                index = int(input("Enter the expense index to remove: ").strip()) - 1
                tracker.remove_expense(index)
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        elif choice == "3":
            tracker.view_expenses()

        elif choice == "4":
            month = input("Enter the month (YYYY-MM): ").strip()
            tracker.view_expenses_by_month(month)

        elif choice == "5":
            try:
                budget = float(input("Enter your monthly budget: ").strip())
                tracker.set_budget(budget)
            except ValueError:
                print("Invalid amount! Please enter a valid number.")

        elif choice == "6":
            tracker.total_expenses()

        elif choice == "7":
            print("Goodbye! See you soon!")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()