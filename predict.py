from data_processing import data

def suggest():
    total = sum(h for s, h in data)

    if total < 2:
        print("Study more!")
    else:
        print("Good job!")
