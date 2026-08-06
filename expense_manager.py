from datetime import date

import file_handler

import json



def add_expenses():
    todaydate = date.today()  
    formatted_date = todaydate.strftime("%Y-%m-%d") 
    category = input("Enter the category :")
    amount = int(input("Enter the Amount :"))
    title = input("Enter the title :")
    expense = {
        "Title": title,
        "Amount": amount,
        "Category": category,
        "Date": date
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

     
def search_expenses():
    expenses = file_handler.load_data()

    if not expenses:
        print("No expenses found.")
        return

    field = input("Search by (1) Category or (2) Title? Enter 1 or 2: ").strip()

    if field == "1":
        key_name = "Category"
    elif field == "2":
        key_name = "Title"
    else:
        print("Invalid choice.")
        return

    query = input(f"Enter the {key_name.lower()} you want to search: ").strip().lower()

    found = False
    for each in expenses:
        if each[key_name].strip().lower() == query:
            print("=======================================")
            for key, value in each.items():
                print(f"{key}: {value}")
            print("=======================================")
            print()
            found = True

    if not found:
        print(f"No item found with this {key_name.lower()}.")
   


   
  
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
        
    
        


def update_expenses():

    expenses = file_handler.load_data()

    if not expenses:
        print("No expenses found.")
        return

    found = False
    title = input("Enter the title you wnat to update : ")

    for each in expenses:
        if each["title"] == title:
            print("1. Date")
            print("2. Category")
            print("3. Amount")
            print("4. Title")
            
            update = int(input("Choose what you want to update: "))
             
             
    
            if update == 1 :
                new_date = input("Enter the new date: ")
                
                each["Date"] = new_date
                
            elif update == 2:
                new_cat = input("Enter the new category: ") 
                
                each["Category"] = new_cat
                
            elif update == 3:
                new_amount =  int(input("Enter the amount: ")) 
                
                each["Amount"] = new_amount 
                   
            elif update == 4:
                new_title = input("Ente the new title: ")
                each["Title"] = new_title
            else :
                print("Invalid input")  

            found = True


    if found:
        file_handler.save_data(expenses)
        print("Expense updated successfully.")
    else:
      print("No item found with this title.") 
    
    
def delete_expenses():
    
    expenses = file_handler.load_data()

    if not expenses:
        print("No expenses found.")
        return
    
    title = input("Enter the title of item you want to delete : ")
    
    found = False

    for each in expenses:
        
        if each["Title"] == title:
             
         choice = input("Are you sure (y/n) : ").lower()
          
         if choice == "y":
           found = True
           expenses.remove(each)
           break
        
         elif choice == "n":
          print("Operation cancelled.")
          break
      
         else:
             print("Invalid input")   
        
    
        
    
    if found:
        file_handler.save_data(expenses)
        print("Expense deleted successfully.")
    else:
      print("No item found with this title.")     
      
     