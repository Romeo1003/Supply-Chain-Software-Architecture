# final code:

import mysql.connector

# Constants
HOST = "127.0.0.1"
HOST2 = "10.0.0.87"
# ... other constants if needed


# Function to establish a connection to the database
def connect_to_db():
    try:
        # Establish connection
        cnx = mysql.connector.connect(
            host=HOST, user="root", password="s", database="alphahomes"
        )
        return cnx
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


# Function to display the menu options
def display_menu():
    print("MENU:")
    print("1. View Product Table")
    print("2. View Customer Info Table")
    print("3. View Sales Records")
    print("4. Place an Order")
    print("Q. Quit")


# Main function
def main():
    connection = connect_to_db()
    if connection:
        # Loop to display menu until user chooses to quit
        while True:
            display_menu()
            choice = input("Enter your choice: ")
            if choice.upper() == "1":
                # Option 1: View Product Table
                # ... fetch and display product table
                pass
            elif choice.upper() == "2":
                # Option 2: View Customer Info Table
                # ... fetch and display customer info table
                pass
            elif choice.upper() == "3":
                # Option 3: View Sales Records
                # ... fetch and display sales records
                pass
            elif choice.upper() == "4":
                # Option 4: Place an Order
                # ... logic for placing an order
                pass
            elif choice.upper() == "Q":
                break
            else:
                print("Invalid choice. Please choose again.")

        connection.close()


# Execute the main function
if __name__ == "__main__":
    main()
