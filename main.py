import pandas as pd
import matplotlib.pyplot as plt
import os

# Initialize or load the finance data
def initialize_data():
    if not os.path.exists('finance_data.csv'):
        # Create a new CSV with predefined columns
        df = pd.DataFrame(columns=['Date', 'Category', 'Type', 'Amount'])
        df.to_csv('finance_data.csv', index=False)
        return df
    else:
        return pd.read_csv('finance_data.csv')

# Function to add income or expense
def add_transaction(df, date, category, transaction_type, amount):
    new_transaction = {'Date': date, 'Category': category, 'Type': transaction_type, 'Amount': amount}
    df = df.append(new_transaction, ignore_index=True)
    df.to_csv('finance_data.csv', index=False)
    print(f'{transaction_type} added successfully!')
    return df

# Function to generate reports
def generate_report(df):
    print("\n--- Financial Report ---")
    income = df[df['Type'] == 'Income']['Amount'].sum()
    expenses = df[df['Type'] == 'Expense']['Amount'].sum()
    savings = income - expenses

    print(f"Total Income: ${income}")
    print(f"Total Expenses: ${expenses}")
    print(f"Savings: ${savings}")
    print("\n--- Category Breakdown ---")
    category_breakdown = df.groupby('Category')['Amount'].sum()
    print(category_breakdown)

    # Visualize expenses by category
    category_breakdown.plot(kind='bar', title='Expenses by Category', color='green')
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.show()

# Main menu to interact with the user
def main_menu():
    df = initialize_data()

    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Generate Report")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter income category: ")
            amount = float(input("Enter income amount: "))
            df = add_transaction(df, date, category, 'Income', amount)
        
        elif choice == '2':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            df = add_transaction(df, date, category, 'Expense', amount)
        
        elif choice == '3':
            generate_report(df)
        
        elif choice == '4':
            print("Exiting Personal Finance Tracker.")
            break
        
        else:
            print("Invalid option. Please select again.")

if __name__ == "__main__":
    main_menu()
