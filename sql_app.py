# Product Management System (SQL Edition)
# Built by: [YOUR NAME]
# Full CRUD + persistence with SQLite


import sqlite3

conn = sqlite3.connect("products.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price INTEGER NOT NULL
        )""")
conn.commit()
while True:
    print("1.Add Product")
    print("2.Show All Products")
    print("3.Find One Product")
    print("4.Update Price")
    print("5.Delete Product")
    print("6.Quit")
    choice = input("Type a number:")

    if choice == "1":
        name = input("what is the product name?")
        try:
            price = int(input("what is the price?"))
            cursor.execute("INSERT INTO products(name,price) VALUES (?,?)",(name,price))
            conn.commit()
            print("Product added!")
        except ValueError:
            print("Invalid price! Please enter a number.")
    elif choice == "2":
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    elif choice == "3":
        name = input("what is the product name?")
        cursor.execute("SELECT * FROM products WHERE name=?",(name,))
        row = cursor.fetchone()
        if row == None:
            print("Product not found")
        else:
            print(row)
    elif choice == "4":
        name = input("What is the product name?")
        try:
            new_price = int(input("What is the new price?"))
            cursor.execute("UPDATE products SET price = ? WHERE name = ?", (new_price,name))
            conn.commit()
            if cursor.rowcount >0:
                print("Price Updated Successfully!")
            else:
                print("Product not found")
        except ValueError:
            print("Invalid price! please enter a number!")
    elif choice =="5":
        name = input("What is the product name?")
        cursor.execute("DELETE FROM products WHERE name = ?",(name,))
        conn.commit()
        if cursor.rowcount > 0:
            print("Product Deleted Successfully!")
        else:
            print("Product not found")
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid option,Please type 1,2,3,4,5 or 6")
conn.close()