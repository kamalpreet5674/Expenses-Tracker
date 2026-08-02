from datetime import date

import file_handler

expenses = []

def add_expenses():
    todaydate = date.today()
    formatted_date = todaydate.strftime("%d-%m-%Y")
    category = input("Enter the category :")
    amount = int(input("Enter the Amount :"))
    description = input("Enter the Description :")
    
    expense = {
        "Date": formatted_date,
        "Category" : category,
        "Amount": amount,
        "description": description
    }
    
    message =  file_handler.load_data()
    message.append(expense)
    
    file_handler.save_data(message)
    
if __name__ == "__main__":
    print("--- Expense Tracker Loaded ---")
    add_expenses()    
  