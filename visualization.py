import matplotlib.pyplot as plt
from data_processing import data

def plot():
    subjects = [s for s, h in data]
    hours = [h for s, h in data]

    if not subjects:
        print("No data to plot")
        return

    plt.bar(subjects, hours)
    plt.xlabel("Subjects")
    plt.ylabel("Hours")
    plt.title("Study Analysis")
    plt.show()
