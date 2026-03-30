from data_processing import add_data, get_total, save_data
from predict import predict_performance
from visualization import plot
from data_processing import data

def menu():
    while True:
        print("\n1. Add Data")
        print("2. Total Hours")
        print("3. Save Data")
        print("4. Show Graph")
        print("5. Predict Performance")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_data()
        elif choice == '2':
            print("Total Hours:", get_total())
        elif choice == '3':
            save_data(data)
            print("Data saved!")
        elif choice == '4':
            plot()
        elif choice == '5':
            total = get_total()
            print(predict_performance(total))
        elif choice == '6':
            break
