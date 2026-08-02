from datetime import date

import file_handler

import json



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
    

  

def view_expenses():
    
    expenses = file_handler.load_data()
        
    for index, expense in enumerate(expenses, start=1):
         print(f"\n--- Expense #{index} ---")
         for key, value in expense.items():
          print(f"{key}: {value}")
        
       
    
    
    
# view_expenses()        
  