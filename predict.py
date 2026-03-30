def predict_performance(hours):
    if hours < 2:
        return "Low performance risk"
    elif hours < 5:
        return "Average performance"
    else:
        return "High performance"
