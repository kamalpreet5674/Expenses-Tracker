from datetime import date

import file_handler

import json



def add_expenses():
    todaydate = date.today()  
    formatted_date = todaydate.strftime("%Y-%m-%d") 
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
    

  

def view_expenses():
    
    expenses = file_handler.load_data()
        
    for index, expense in enumerate(expenses, start=1):
         print(f"\n--- Expense #{index} ---")
         for key, value in expense.items():
          print(f"{key}: {value}")

     
       
def filter_by_category():

    expenses = file_handler.load_data()

    if not expenses:
        print("No expenses found.")
        return

    found = False
    use_category = input("Enter the category you want to search: ")

    for each in expenses:
        if each["Category"] == use_category:

            print("=======================================")

            for key, value in each.items():
                print(f"{key}: {value}")

            print("=======================================")
            print()

            found = True

    if not found:
        print("No item found with this category.")
  

  
def monthly_summary():
    expenses = file_handler.load_data()

    if not expenses:
        print("No expenses found.")
        return

    month = input("Enter month (YYYY-MM): ")
    total = 0

    for cash in expenses:
        # print(cash["Date"])
        # print(cash["Date"][:7], month)
        if cash["Date"][:7] == month:
            total += cash["Amount"]

    if total == 0:
        print("No expenses found for this month.")
    else:
        print("===================================")
        print("          Monthly Summary                          ")
        print("===================================")
        print(f"Month: {month}")
        print(f"Total Expenses: {total}")
        print("===================================")
        
monthly_summary()        
        
