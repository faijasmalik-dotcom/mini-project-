import sqlite3
conn = sqlite3.connect("employee details.db")
c = conn.cursor()
c.execute("PRAGMA foreign_keys = ON")
c.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    );
""")
c.execute("""
    CREATE TABLE IF NOT EXISTS employee (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        email TEXT,
        department TEXT,
        salary REAL,
        experience INTEGER,
        join_date TEXT
    );
""")
c.execute("""
    CREATE TABLE IF NOT EXISTS salary_increment(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id INTEGER,
        location TEXT,
        salary increment REAL,
        FOREIGN KEY (employee_id) REFERENCES employee(id) ON DELETE CASCADE
    );
""")
conn.commit()
def register():
    user = input("Enter username: ")
    password = input("Enter password: ")
    password1 = input("Confirm password: ")

    if password == password1:
        try:
            conn = sqlite3.connect("employee details.db")
            c = conn.cursor()
            c.execute("""
                INSERT INTO user (username, password)
                VALUES (?, ?);
            """, (user, password))
            conn.commit()
            print("User registered successfully")
        except sqlite3.IntegrityError:
            print("Username already exists. Please choose a different one.")
        finally:
            conn.close()
    else:
        print("Passwords don't match")

def login():
    user = input("Enter username: ")
    password = input("Enter password: ")
    conn = sqlite3.connect("employee details.db")
    c = conn.cursor()
    c.execute("SELECT * FROM user WHERE username = ?AND password= ?", (user, password))
    result = c.fetchone()
    conn.close()
    if result:
        print("Login successful")
    else:
        print("Login failed")

def add_employees():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    email = input("Enter your email: ")
    department = input("Enter your department: ")
    salary = float(input("Enter your salary: "))
    experience = int(input("Enter your experience: "))
    join_date = input("Enter your join date(yyyy-mm-dd): ")

    c.execute("""
           INSERT INTO employee (name, age, email, department, salary, experience, join_date)
           VALUES (?, ?, ?, ?, ?, ?, ?);
    """, (name, age, email, department, salary, experience, join_date))

    conn.commit()
    conn.close()
    print("Employee added successfully!")
# add_employees()
def view_employees():
    conn = sqlite3.connect("employee details.db")
    c = conn.cursor()
    c.execute("SELECT *FROM employee")
    for i in c.fetchall():
        print(i)
# view_employees()
def update_employees():
    conn=sqlite3.connect("employee details.db")
    c = conn.cursor()
    c.execute("UPDATE employee SET id='5'WHERE id = 6")
    c.execute("UPDATE employee SET salary='110000' WHERE id = 1")
    conn.commit()
    conn.close()

def delete_employees():
    conn = sqlite3.connect("employee details.db")
    c = conn.cursor()
    c.execute("DELETE FROM employee WHERE id = 5")
    c.execute("DELETE FROM salary_increment WHERE employee_id = 5")
    conn.commit()
delete_employees()

def add_salary_increment():
    conn = sqlite3.connect("employee details.db")
    c = conn.cursor()
    employee_id = input("Enter Employee ID: ")
    location = input("Enter Location: ")
    salary = float(input("Enter Salary: "))
    c.execute("""
        INSERT INTO salary_increment(employee_id, location, salary)
        VALUES (?,?,?)
    """, (employee_id, location, salary))
    conn.commit()
    conn.close()
    print("salary increment added successfully!")

def view_salary_increment():
    conn = sqlite3.connect("employee details.db")
    c = conn.cursor()
    c.execute("SELECT * FROM salary_increment")
    for i in c.fetchall():
        print(i)

def main():
    print("1. Register")
    print("2. Login")

    choice = input("Enter your choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    else:
        print("Invalid choice")
        return

    while True:
        print("\n--- EMPLOYEE MANAGEMENT SYSTEM ---")
        print("1. Add Employees")
        print("2. View Employees")
        print("3. Update Employees")
        print("4. Delete Employees")
        print("5. Add Salary Increment")
        print("6. View Salary Increment")
        print("7. Exit")

        option = input("Enter your choice: ")

        if option == "1":
            add_employees()
        elif option == "2":
            view_employees()
        elif option == "3":
            update_employees()
        elif option == "4":
            delete_employees()
        elif option == "5":
            add_salary_increment()
        elif option == "6":
            view_salary_increment()
        elif option == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

main()
conn.close()