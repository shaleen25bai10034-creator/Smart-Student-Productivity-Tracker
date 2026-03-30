from data_processing import add_data, get_total
from predict import suggest

def menu():
    while True:
        print("1. Add Data")
        print("2. Total Hours")
        print("3. Suggestion")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_data()
        elif choice == '2':
            print(get_total())
        elif choice == '3':
            suggest()
        elif choice == '4':
            break
