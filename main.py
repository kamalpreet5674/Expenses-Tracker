import expense_manager

def menu():
 print("===== Expenses Tracker System =====")   
 print("         Operation starting") 
 menu_options = [
     "Add Expense",
     "View Expense",
     "Search Expenses",
     "Update Expeses",
     "Delete Expeses",
     "Monthly Summary",
     "Exit",
      
 ]
 
 
 for index, options in enumerate(menu_options,start = 1):
    print(f" {index}:{options}")
    
 print("=======================================")    






def main():

    while True:
        menu()

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                expense_manager.add_expenses()

            elif choice == 2:
                expense_manager.view_expenses()

            elif choice == 3:
              expense_manager.search_expenses()

            elif choice == 4:
                expense_manager.update_expenses()
                
            elif choice == 5:
                expense_manager.delete_expenses()
                
            elif choice == 6:
                expense_manager.monthly_summary()
                
                
            elif choice == 7:
                print("Thank you for using Expenses management System.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
            

            


if __name__ == "__main__":
  main()

