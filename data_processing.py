import csv

data = []

def add_data():
    subject = input("Subject: ")
    hours = float(input("Hours: "))
    data.append((subject, hours))

def get_total():
    return sum(h for s, h in data)

def save_data(data):
    with open("data.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Subject", "Hours"])
        writer.writerows(data)
