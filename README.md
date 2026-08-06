# 🏆 Personal Expense Tracker (CLI Application)

A command-line based Personal Expense Tracker built with Python. This project helps users manage daily expenses by storing data in a JSON file.

---

## 📌 Project Goal

Build a real-world expense management system where users can:

* Add daily expenses
* View all saved expenses
* Filter expenses by category *(In Progress)*
* View monthly expense summary *(Planned)*

The project is focused on improving **Python logic building**, **problem-solving**, and **file handling** skills.

---

# 📂 Project Structure

```text
Expenses-Tracker/

│
├── data/
│   └── expenses.json
│
├── main.py
├── expense_manager.py
├── file_handler.py
├── utils.py
├── README.md
└── .gitignore
```

---

# ✅ Features Completed

## 1. JSON Database

Expenses are stored permanently inside:

```text
data/expenses.json
```

Data format:

```json
[
    {
        "Date": "02-08-2026",
        "Category": "Food",
        "Amount": 250,
        "description": "Burger"
    }
]
```

---

## 2. File Handling

Implemented in:

```text
file_handler.py
```

### Functions

### `load_data()`

Responsibilities:

* Open JSON file
* Read data
* Return list of expenses
* Handle:

  * FileNotFoundError
  * JSONDecodeError

---

### `save_data()`

Responsibilities:

* Save updated expense list
* Write JSON using `json.dump()`

---

## 3. Add Expense

Implemented in:

```text
expense_manager.py
```

### Workflow

```text
User Input
      ↓
Create Expense Dictionary
      ↓
Load Existing Expenses
      ↓
Append New Expense
      ↓
Save Updated List
      ↓
Expense Stored in JSON
```

### Concepts Practiced

* Functions
* Dictionary
* List of Dictionaries
* User Input
* File Handling
* JSON Storage

---

## 4. View Expenses

Implemented in:

```text
expense_manager.py
```

### Workflow

```text
Load Expenses
      ↓
Loop Through List
      ↓
Display Each Expense
```

### Concepts Practiced

* for loop
* enumerate()
* Dictionary iteration
* Nested loop
* File handling

---

## 5. Main Menu

Implemented in:

```text
main.py
```

Menu Options:

1. Add Expense
2. View Expenses
3. Search Expenses
4. Update Expenses
5. Delete expenses
6. Monthly Summary *(Coming Soon)*
7. Exit


Responsibilities:

* Display menu
* Take user choice
* Call corresponding functions
* Handle invalid input

---

# 🧠 Python Concepts Learned

* Functions
* Modules
* Import
* File Handling
* JSON Read & Write
* Exception Handling
* Dictionary
* List of Dictionaries
* Nested Loop
* enumerate()
* Function Calling
* Project Structure
* Separation of Concerns

---



---

# 🎯 Learning Objective

This project follows a **Logic First** approach.

Every feature is developed using the workflow:

```text
Problem Understanding
        ↓
Manual Thinking
        ↓
English Steps
        ↓
Pattern Recognition
        ↓
Pseudocode
        ↓
Python Code
        ↓
Dry Run
        ↓
Reflection
```

The goal is to build strong programming logic before focusing on syntax.

---

# 👨‍💻 Author

**Kamalpreet Singh**

Learning Python by building real-world CLI projects with a focus on logic building and problem-solving.
