import expense_manager

def menu():
 print("===== Expenses Tracker System =====")    
 menu_options = [
     "Add Expense",
     "View Expense",
     "Filter by Category",
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
                view_expenses()

            elif choice == 3:
                filter_by_category()

            elif choice == 4:
                monthly_summary()


            elif choice == 5:
                print("Thank you for using Expenses management System.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
            

            


if __name__ == "__main__":
    main()
print("Operations done")
