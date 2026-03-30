data = []

def add_data():
    subject = input("Subject: ")
    hours = float(input("Hours: "))
    data.append((subject, hours))

def get_total():
    return sum(h for s, h in data)
